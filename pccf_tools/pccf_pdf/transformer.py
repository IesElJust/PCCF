import html
import re
import xml.etree.ElementTree as ET
import zipfile

try:
    from odf.opendocument import load
    from odf.table import Table, TableCell, TableRow
    from odf.teletype import extractText
    from odf.text import P
except ImportError:  # pragma: no cover
    load = None


def _require_odfpy():
    if load is None:
        raise RuntimeError("Falta la dependencia 'odfpy'. Instal-la amb: pip install odfpy")


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

        rendered, _, width = _render_cell(cell, tag)
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


def _xml_attr(element, namespace, name, default=None):
    return element.attrib.get(f"{{{namespace}}}{name}", default)


def _xml_int_attr(element, namespace, name, default=1):
    value = _xml_attr(element, namespace, name)
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _xml_cell_text(cell, text_ns):
    paragraphs = []
    for paragraph in cell.findall(f".//{{{text_ns}}}p"):
        text = "".join(paragraph.itertext()).strip()
        if text:
            paragraphs.append(_format_cell_text(text))
    return "<br>".join(paragraphs)


def _xml_row_has_content(row, table_ns, text_ns):
    for cell in row:
        if cell.tag == f"{{{table_ns}}}table-cell" and _xml_cell_text(cell, text_ns):
            return True
    return False


def _xml_render_cell(cell, tag, table_ns, text_ns):
    text = _xml_cell_text(cell, text_ns)
    colspan = _xml_int_attr(cell, table_ns, "number-columns-spanned", 1)
    rowspan = _xml_int_attr(cell, table_ns, "number-rows-spanned", 1)

    attrs = []
    if colspan > 1:
        attrs.append(f'colspan="{colspan}"')
    if rowspan > 1:
        attrs.append(f'rowspan="{rowspan}"')

    attr_text = f" {' '.join(attrs)}" if attrs else ""
    return f"<{tag}{attr_text}>{text}</{tag}>", bool(text or attrs), colspan


def _xml_skip_rowspans(column, active_rowspans, max_columns):
    while column < max_columns and active_rowspans[column] > 0:
        column += 1
    return column


def _xml_render_row(row, tag, max_columns, table_ns, text_ns, active_rowspans=None):
    rendered_cells = []
    column = 0
    if max_columns is None:
        active_rowspans = []
        next_rowspans = []
    else:
        active_rowspans = active_rowspans or [0] * max_columns
        next_rowspans = [max(value - 1, 0) for value in active_rowspans]

    for cell in row:
        if max_columns is not None:
            column = _xml_skip_rowspans(column, active_rowspans, max_columns)
        if max_columns is not None and column >= max_columns:
            break

        if cell.tag == f"{{{table_ns}}}covered-table-cell":
            if max_columns is None and tag == "th":
                rendered_cells.append("<th></th>")
                column += 1
            continue
        if cell.tag != f"{{{table_ns}}}table-cell":
            continue

        rendered, has_content, cell_width = _xml_render_cell(cell, tag, table_ns, text_ns)
        repeat = _xml_int_attr(cell, table_ns, "number-columns-repeated", 1)
        rowspan = _xml_int_attr(cell, table_ns, "number-rows-spanned", 1)

        if max_columns is not None:
            remaining = max_columns - column
            if remaining <= 0:
                break
            repeat = min(repeat, max(1, remaining // max(cell_width, 1)))

        if has_content or max_columns is not None:
            for _ in range(repeat):
                if max_columns is not None:
                    column = _xml_skip_rowspans(column, active_rowspans, max_columns)
                    if column >= max_columns:
                        break
                rendered_cells.append(rendered)
                if max_columns is not None and rowspan > 1:
                    for spanned_column in range(column, min(column + cell_width, max_columns)):
                        next_rowspans[spanned_column] = max(
                            next_rowspans[spanned_column], rowspan - 1
                        )
                column += cell_width
        else:
            rendered_cells.append(rendered)
            column += cell_width

    while max_columns is None and rendered_cells and re.match(r"^<th></th>$", rendered_cells[-1]):
        rendered_cells.pop()

    while max_columns is not None and column < max_columns:
        column = _xml_skip_rowspans(column, active_rowspans, max_columns)
        if column >= max_columns:
            break
        rendered_cells.append(f"<{tag}></{tag}>")
        column += 1

    if not rendered_cells:
        return ("", next_rowspans) if max_columns is not None else ""

    rendered_row = "<tr>" + "".join(rendered_cells) + "</tr>"
    return (rendered_row, next_rowspans) if max_columns is not None else rendered_row


def _xml_sheet_rows(ods_path, sheet_name):
    table_ns = "urn:oasis:names:tc:opendocument:xmlns:table:1.0"
    text_ns = "urn:oasis:names:tc:opendocument:xmlns:text:1.0"

    with zipfile.ZipFile(ods_path, "r") as ods:
        content = ods.read("content.xml")

    root = ET.fromstring(content)
    sheet = None
    for table in root.findall(f".//{{{table_ns}}}table"):
        if _xml_attr(table, table_ns, "name") == sheet_name:
            sheet = table
            break

    if sheet is None:
        print(f"[ODS ERROR] No s'ha trobat el full '{sheet_name}'.")
        return None

    rows = []
    for row in sheet.findall(f"{{{table_ns}}}table-row"):
        repeat = _xml_int_attr(row, table_ns, "number-rows-repeated", 1)
        if repeat > 1 and not _xml_row_has_content(row, table_ns, text_ns):
            continue
        repeat = min(repeat, 100)
        rows.extend([row] * repeat)

    return [row for row in rows if _xml_row_has_content(row, table_ns, text_ns)], table_ns, text_ns


def transform_sheet_to_html(ods_path, sheet_name):
    sheet_data = _xml_sheet_rows(ods_path, sheet_name)
    if sheet_data is None:
        return None

    rows, table_ns, text_ns = sheet_data
    if not rows:
        print(f"[ODS ERROR] El full '{sheet_name}' no te files amb contingut.")
        return None

    header = _xml_render_row(rows[0], "th", None, table_ns, text_ns)
    column_count = len(re.findall(r"<th(?:\s|>)", header))
    active_rowspans = [0] * column_count

    body_rows = []
    for row in rows[1:]:
        rendered_row, active_rowspans = _xml_render_row(
            row, "td", column_count, table_ns, text_ns, active_rowspans
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
    """Substitueix les marques {nom_full} per taules HTML de l'ODS."""
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
