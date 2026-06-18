import html
import re

try:
    from odf.opendocument import load
    from odf.table import Table, TableCell, TableRow
    from odf.teletype import extractText
    from odf.text import P
except ImportError:  # pragma: no cover - missatge per a entorns sense dependencies
    load = None


def _require_odfpy():
    if load is None:
        raise RuntimeError(
            "Falta la dependencia 'odfpy'. Instal-la amb: pip install odfpy"
        )


def _int_attr(element, name, default=1):
    value = element.getAttribute(name)
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _cell_text(cell):
    paragraphs = []
    for paragraph in cell.getElementsByType(P):
        text = extractText(paragraph).strip()
        if text:
            paragraphs.append(_format_cell_text(text))
    return "<br>".join(paragraphs)


def _format_cell_text(text):
    escaped = html.escape(text)
    match = re.match(r"^([A-Za-zÀ-ÿ0-9]+[.)])\s+(.+)$", escaped)
    if not match:
        return escaped

    marker, content = match.groups()
    return (
        '<span class="ods-list-item">'
        f'<span class="ods-list-marker">{marker}</span> '
        f'<span class="ods-list-content">{content}</span>'
        "</span>"
    )


def _render_cell(cell, tag):
    text = _cell_text(cell)
    colspan = _int_attr(cell, "numbercolumnsspanned", 1)
    rowspan = _int_attr(cell, "numberrowsspanned", 1)

    attrs = []
    if colspan > 1:
        attrs.append(f'colspan="{colspan}"')
    if rowspan > 1:
        attrs.append(f'rowspan="{rowspan}"')

    attr_text = f" {' '.join(attrs)}" if attrs else ""
    return f"<{tag}{attr_text}>{text}</{tag}>", bool(text or attrs), colspan


def _cells_width(cells):
    return sum(width for _, _, width in cells)


def _remaining_repeats(cells, repeat, width, max_columns):
    if max_columns is None:
        return repeat
    remaining = max_columns - _cells_width(cells)
    if remaining <= 0:
        return 0
    return min(repeat, max(1, remaining // max(width, 1)))


def _row_cells(row, tag, max_columns=None):
    cells = []
    for cell in row.childNodes:
        if max_columns is not None and _cells_width(cells) >= max_columns:
            break

        if getattr(cell, "tagName", None) == "table:covered-table-cell":
            if tag == "th":
                cells.append(("<th></th>", False, 1))
            continue
        if getattr(cell, "tagName", None) != "table:table-cell":
            continue

        rendered, has_content, width = _render_cell(cell, tag)
        repeat = _int_attr(cell, "numbercolumnsrepeated", 1)
        repeat = _remaining_repeats(cells, repeat, width, max_columns)

        if has_content or max_columns is not None:
            cells.extend((rendered, has_content, width) for _ in range(repeat))
        else:
            cells.append((rendered, False, width))

    while max_columns is None and cells and not cells[-1][1]:
        cells.pop()

    while max_columns is not None and _cells_width(cells) < max_columns:
        cells.append((f"<{tag}></{tag}>", False, 1))

    return cells


def _row_has_content(row):
    for cell in row.getElementsByType(TableCell):
        if _cell_text(cell):
            return True
    return False


def _skip_rowspans(column, active_rowspans, max_columns):
    while column < max_columns and active_rowspans[column] > 0:
        column += 1
    return column


def _repeat_count(column, repeat, width, max_columns):
    remaining = max_columns - column
    if remaining <= 0:
        return 0
    return min(repeat, max(1, remaining // max(width, 1)))


def _render_row(row, tag, max_columns, active_rowspans):
    rendered_cells = []
    next_rowspans = [max(value - 1, 0) for value in active_rowspans]
    column = 0

    for cell in row.childNodes:
        column = _skip_rowspans(column, active_rowspans, max_columns)
        if column >= max_columns:
            break

        if getattr(cell, "tagName", None) == "table:covered-table-cell":
            column += 1
            continue
        if getattr(cell, "tagName", None) != "table:table-cell":
            continue

        rendered, has_content, width = _render_cell(cell, tag)
        repeat = _int_attr(cell, "numbercolumnsrepeated", 1)
        repeat = _repeat_count(column, repeat, width, max_columns)
        if repeat == 0:
            continue

        rowspan = _int_attr(cell, "numberrowsspanned", 1)
        for _ in range(repeat):
            column = _skip_rowspans(column, active_rowspans, max_columns)
            if column >= max_columns:
                break

            rendered_cells.append(rendered)
            if rowspan > 1:
                for spanned_column in range(column, min(column + width, max_columns)):
                    next_rowspans[spanned_column] = max(
                        next_rowspans[spanned_column], rowspan - 1
                    )
            column += width

    while column < max_columns:
        column = _skip_rowspans(column, active_rowspans, max_columns)
        if column >= max_columns:
            break
        rendered_cells.append(f"<{tag}></{tag}>")
        column += 1

    if not rendered_cells:
        return "", next_rowspans
    return "<tr>" + "".join(rendered_cells) + "</tr>", next_rowspans


def _find_sheet(document, sheet_name):
    for sheet in document.spreadsheet.getElementsByType(Table):
        if sheet.getAttribute("name") == sheet_name:
            return sheet
    return None


def transform_sheet_to_html(ods_path, sheet_name):
    _require_odfpy()

    document = load(ods_path)
    sheet = _find_sheet(document, sheet_name)
    if sheet is None:
        print(f"[ODS ERROR - odfpy] No s'ha trobat el full '{sheet_name}'.")
        return None

    rows = []
    for row in sheet.getElementsByType(TableRow):
        repeat = _int_attr(row, "numberrowsrepeated", 1)
        if repeat > 1 and not _row_has_content(row):
            continue
        rows.extend([row] * repeat)

    rows = [row for row in rows if _row_has_content(row)]
    if not rows:
        print(f"[ODS ERROR - odfpy] El full '{sheet_name}' no te files amb contingut.")
        return None

    column_count = _cells_width(_row_cells(rows[0], "th"))
    active_rowspans = [0] * column_count
    header, active_rowspans = _render_row(rows[0], "th", column_count, active_rowspans)

    body_rows = []
    for row in rows[1:]:
        rendered_row, active_rowspans = _render_row(
            row, "td", column_count, active_rowspans
        )
        if rendered_row:
            body_rows.append(rendered_row)
    body = "\n".join(body_rows)

    return (
        '<table class="pdf-table">\n'
        f"<thead>{header}</thead>\n"
        f"<tbody>{body}</tbody>\n"
        "</table>"
    )


def process_markdown(markdown, ods_path, xslt_path=None):
    """
    Substitueix les marques {nom_full} en el markdown per taules HTML de l'ODS.
    xslt_path es conserva per compatibilitat amb el plugin anterior.
    """
    pattern = re.compile(r'\{([^}]+)\}(?:\s*"([^"]+)")?')

    def replace_match(match):
        sheet_name = match.group(1).strip()
        title = match.group(2)
        try:
            html_table = transform_sheet_to_html(ods_path, sheet_name)
        except Exception as exc:
            print(f"[ODS ERROR - odfpy] Full '{sheet_name}': {exc}")
            return match.group(0)

        if not html_table:
            return match.group(0)
        if title:
            return f"<h3>{html.escape(title)}</h3>\n{html_table}"
        return html_table

    return pattern.sub(replace_match, markdown)
