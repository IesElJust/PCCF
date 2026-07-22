#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10
    import tomli as tomllib


def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return text
    return parts[1].lstrip()


def normalize_raw_divs_for_pandoc(text: str) -> str:
    text = re.sub(
        r'<div class="page-break"></div>',
        '::: { .page-break }\n:::',
        text,
    )

    table_wrapper_classes = (
        "table-fit-content",
        "table-assessment-compact",
        "table-ra-compact",
        "table-contribucio-ra",
        "table-qualifications",
        "table-qualifications-pdf-fix",
    )
    table_wrapper_pattern = "|".join(re.escape(name) for name in table_wrapper_classes)

    def replace_table_wrapper(match: re.Match[str]) -> str:
        class_attr = match.group("classes")
        classes = [name for name in class_attr.split() if name in table_wrapper_classes]
        comments = match.group("comments") or ""
        table_html = match.group("table")

        if not classes:
            return match.group(0)

        table_class_attr = " ".join(classes)
        table_html = re.sub(
            r"<table(?![^>]*\bclass=)",
            f'<table class="{table_class_attr}"',
            table_html,
            count=1,
        )
        return f"{comments}{table_html}"

    text = re.sub(
        rf'<div class="(?P<classes>[^"]*\b(?:{table_wrapper_pattern})\b[^"]*)">\s*'
        r'(?P<comments>(?:<!--.*?-->\s*)*)'
        r'(?P<table><table.*?</table>)\s*'
        r'</div>',
        replace_table_wrapper,
        text,
        flags=re.DOTALL,
    )

    # Evita que pandoc convertisca marques com "a)" dins de cel·les HTML
    # en llistes ordenades alfabètiques quan genera el PDF.
    text = re.sub(r'(<td>)([a-z])\)\s+', r'\1\2&#41; ', text)
    text = re.sub(r'(<br/>)([a-z])\)\s+', r'\1\2&#41; ', text)
    return text


def load_nav_docs(site_dir: Path) -> list[Path]:
    config_path = site_dir / "zensical.toml"
    data = tomllib.loads(config_path.read_text(encoding="utf-8"))
    nav = data.get("navigation", {}).get("nav", [])

    docs: list[Path] = []
    for item in nav:
        for _, rel_path in item.items():
            docs.append(site_dir / "docs" / rel_path)
    return docs


def load_site_config(site_dir: Path) -> dict:
    config_path = site_dir / "zensical.toml"
    return tomllib.loads(config_path.read_text(encoding="utf-8"))


def build_front_matter(site_dir: Path) -> str:
    config = load_site_config(site_dir)

    site_name = config.get("project", {}).get("site_name", "Programació didàctica")

    return (
        "---\n"
        f"title: {site_name}\n"
        "lang: ca\n"
        "toc: true\n"
        "toc-title: Índex\n"
        "title-prefix: Programació didàctica\n"
        "---\n"
    )


def get_pdf_templates_dir(site_dir: Path) -> Path:
    site_specific = site_dir / "pdf-templates"
    if site_specific.exists():
        return site_specific

    site_root = Path(__file__).resolve().parents[1]
    return site_root / "pdf-templates"


def resolve_site_command(site_dir: Path, command_name: str) -> str:
    local_command = site_dir / ".venv" / "bin" / command_name
    if local_command.exists():
        return str(local_command)
    return command_name


def render_combined_markdown(site_dir: Path) -> str:
    docs = load_nav_docs(site_dir)
    chunks: list[str] = []

    front_matter_path = site_dir / "pdf-templates" / "front-matter.md"
    if front_matter_path.exists():
        front_matter = front_matter_path.read_text(encoding="utf-8")
    else:
        front_matter = build_front_matter(site_dir)
    chunks.append(front_matter.rstrip() + "\n\n")

    for i, doc_path in enumerate(docs):
        content = strip_front_matter(doc_path.read_text(encoding="utf-8")).strip()
        content = normalize_raw_divs_for_pandoc(content)
        chunks.append(content)
        if i < len(docs) - 1:
            chunks.append('\n\n::: { .page-break }\n:::\n\n')

    return "\n".join(chunks) + "\n"


def run_pandoc(markdown_path: Path, html_path: Path, site_dir: Path) -> None:
    templates_dir = get_pdf_templates_dir(site_dir)
    template = templates_dir / "default.html"
    css = templates_dir / "pdf.css"
    cmd = [
        "pandoc",
        "-s",
        f"--template={template}",
        "-f",
        "markdown-smart+raw_html",
        "--toc",
        f"--css={css}",
        str(markdown_path),
        "-o",
        str(html_path),
    ]
    subprocess.run(cmd, check=True)


def run_weasyprint(html_path: Path, pdf_path: Path) -> None:
    cmd = [sys.executable, "-m", "weasyprint", str(html_path), str(pdf_path)]
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Exporta un site Zensical a PDF.")
    parser.add_argument("site_dir", help="Directori del site")
    parser.add_argument(
        "output_pdf",
        nargs="?",
        default="programacio-didactica_SASP.pdf",
        help="Nom o ruta del PDF de sortida",
    )
    parser.add_argument("--keep-html", action="store_true", help="Conserva l'HTML temporal generat")
    parser.add_argument(
        "--no-rebuild",
        action="store_true",
        help="No reconstruix el site abans de generar el PDF",
    )
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    output_pdf = Path(args.output_pdf)
    if not output_pdf.is_absolute():
        output_pdf = site_dir / output_pdf

    if not args.no_rebuild:
        sync_script = site_dir / "rebuild.sh"
        if sync_script.exists():
            subprocess.run([str(sync_script)], check=True, cwd=site_dir)
        else:
            subprocess.run([resolve_site_command(site_dir, "zensical"), "build"], check=True, cwd=site_dir)

    with tempfile.TemporaryDirectory() as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        markdown_path = tmp_dir / "combined.md"
        html_path = tmp_dir / "combined.html"

        markdown_path.write_text(render_combined_markdown(site_dir), encoding="utf-8")
        run_pandoc(markdown_path, html_path, site_dir)
        run_weasyprint(html_path, output_pdf)

        if args.keep_html:
            kept_html = site_dir / "exported-programacio.html"
            kept_html.write_text(html_path.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"PDF generat correctament: {output_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
