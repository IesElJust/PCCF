#!/usr/bin/env python3

from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path


SYNC_TARGETS = {
    "docs/2-relacio-uc.md": {
        "<!-- ODS:qualificacions_professionals_DAW:start -->": ("<!-- ODS:qualificacions_professionals_DAW:end -->", "qualificacions_professionals_DAW"),
        "<!-- ODS:qualificacions_professionals_DAW_incompletes:start -->": ("<!-- ODS:qualificacions_professionals_DAW_incompletes:end -->", "qualificacions_professionals_DAW_incompletes"),
    },
    "docs/3.contribucio_ra.md": {
        "<!-- ODS:contribucio_ra_cp:start -->": ("<!-- ODS:contribucio_ra_cp:end -->", "contribucio_ra_cp"),
    },
    "docs/4.RAs_CAs_Continguts.md": {
        "<!-- ODS:ra_ca:start -->": ("<!-- ODS:ra_ca:end -->", "ra_ca"),
        "<!-- ODS:continguts:start -->": ("<!-- ODS:continguts:end -->", "continguts"),
    },
    "docs/5.esquema_general_up.md": {
        "<!-- ODS:sequenciacio_up_ra:start -->": ("<!-- ODS:sequenciacio_up_ra:end -->", "sequenciacio_up_ra"),
        "<!-- ODS:sequenciacio_up_continguts:start -->": (
            "<!-- ODS:sequenciacio_up_continguts:end -->",
            "sequenciacio_up_continguts",
        ),
        "<!-- ODS:temporalitzacio:start -->": ("<!-- ODS:temporalitzacio:end -->", "temporalització"),
    },
    "docs/10.Avaluacio.md": {
        "<!-- ODS:avaluacio:start -->": ("<!-- ODS:avaluacio:end -->", "avaluacio"),
    },
}


def load_transformer(plugin_dir: Path):
    sys.path.insert(0, str(plugin_dir))
    module = importlib.import_module("add_tables.transformer")
    return module.extract_content_xml, module.transform_sheet_to_html


def postprocess_sheet_html(sheet_name: str, html: str) -> str:
    if sheet_name == "ra_ca":
        return re.sub(r"\.(CA\d+\.[a-z]\))", r".<br/>\1", html)

    if sheet_name == "continguts":
        html = re.sub(r"(C\d+:)<br/>\s*", r"\1 ", html)
        return html.replace("; ", ";<br/>")

    return html


def render_sheet(sheet_name: str, content_xml_path: str, xslt_path: Path, transform_sheet_to_html) -> str:
    html = transform_sheet_to_html(str(xslt_path), content_xml_path, sheet_name)
    if not html:
        raise RuntimeError(f"No s'ha pogut generar la taula '{sheet_name}' des de l'ODS.")
    html = html.replace('<?xml version="1.0"?>\n', "").strip()
    return postprocess_sheet_html(sheet_name, html)


def replace_between_markers(content: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = content.find(start_marker)
    if start == -1:
        raise RuntimeError(f"No s'ha trobat el marcador inicial: {start_marker}")

    end = content.find(end_marker, start)
    if end == -1:
        raise RuntimeError(f"No s'ha trobat el marcador final: {end_marker}")

    start_block = start + len(start_marker)
    return content[:start_block] + "\n" + replacement + "\n" + content[end:]


def sync_file(path: Path, markers: dict[str, tuple[str, str]], content_xml_path: str, xslt_path: Path, transform_sheet_to_html) -> None:
    content = path.read_text(encoding="utf-8")
    for start_marker, (end_marker, sheet_name) in markers.items():
        rendered = render_sheet(sheet_name, content_xml_path, xslt_path, transform_sheet_to_html)
        content = replace_between_markers(content, start_marker, end_marker, rendered)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    if len(sys.argv) < 4:
        raise SystemExit(
            "Ús: sync_ods_tables_site.py <site_dir> <ods_path> <xslt_path> [plugin_dir]"
        )

    site_dir = Path(sys.argv[1]).resolve()
    ods_path = Path(sys.argv[2]).resolve()
    xslt_path = Path(sys.argv[3]).resolve()
    plugin_dir = Path(sys.argv[4]).resolve() if len(sys.argv) > 4 else site_dir / "ods-tools"

    if not site_dir.exists():
        raise FileNotFoundError(f"No existeix el site: {site_dir}")
    if not ods_path.exists():
        raise FileNotFoundError(f"No existeix l'ODS: {ods_path}")
    if not xslt_path.exists():
        raise FileNotFoundError(f"No existeix la transformació XSLT: {xslt_path}")
    if not plugin_dir.exists():
        raise FileNotFoundError(f"No existeix el directori del plugin: {plugin_dir}")

    extract_content_xml, transform_sheet_to_html = load_transformer(plugin_dir)
    content_xml_path = extract_content_xml(str(ods_path))

    for relative_path, markers in SYNC_TARGETS.items():
        sync_file(site_dir / relative_path, markers, content_xml_path, xslt_path, transform_sheet_to_html)

    print("Taules ODS sincronitzades correctament.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
