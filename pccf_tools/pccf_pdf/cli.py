import argparse
import os
import shutil
import subprocess
import sys
from importlib.resources import files
from pathlib import Path

import yaml

from .transformer import process_markdown


def resource_path(relative_path):
    return files("pccf_pdf").joinpath("resources", relative_path)


def load_config(project_dir):
    config_path = project_dir / "mkdocs.yml"
    if not config_path.is_file():
        raise FileNotFoundError(f"No s'ha trobat {config_path}")

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    ods_path = None
    xslt_path = None
    for plugin in config.get("plugins", []):
        if isinstance(plugin, dict) and "add_tables" in plugin:
            add_tables = plugin["add_tables"] or {}
            ods_path = add_tables.get("ods_path")
            xslt_path = add_tables.get("xslt_path")
            break

    if not ods_path:
        raise ValueError("No s'ha trobat plugins.add_tables.ods_path en mkdocs.yml")

    return config, project_dir / ods_path, xslt_path


def iter_nav_files(nav):
    for item in nav:
        if isinstance(item, str):
            yield item
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, list):
                    yield from iter_nav_files(value)
                else:
                    yield value


def render_markdown_to_html(markdown_file, ods_path, xslt_path):
    with markdown_file.open("r", encoding="utf-8") as file:
        markdown_content = file.read()
    return process_markdown(markdown_content, str(ods_path), str(xslt_path))


def default_front_matter(config, project_dir):
    title = config.get("site_name") or f"Programació Didàctica {project_dir.name}"
    return f"""---
title: |
  {title}
subtitle: {project_dir.name}
lang: ca
toc: true
toc-own-page: true
toc-title: Índex
listings: true
titlepage-rule-height: 0
titlepage-text-color: "F08A2A"
header-left: Departament d'Informàtica. Curs 2025-2026
footer-left: IES Jaume II el Just. PCCF
---
"""


def pandoc_command(input_file, output_file, template_path, css_path):
    return [
        "pandoc",
        "-s",
        f"--template={template_path}",
        "-f",
        "markdown-smart+raw_html",
        "--toc",
        "-c",
        str(css_path),
        str(input_file),
        "-o",
        str(output_file),
    ]


def ensure_pandoc():
    if shutil.which("pandoc"):
        return
    raise RuntimeError(
        "No s'ha trobat el binari 'pandoc'. Instal-la'l al sistema o amb pypandoc "
        "abans de generar PDFs."
    )


def generate_pdf(project_dir, output_pdf, keep_html=False, template=None, css=None, xslt=None):
    project_dir = project_dir.resolve()
    config, ods_path, configured_xslt = load_config(project_dir)

    if not ods_path.is_file():
        raise FileNotFoundError(f"No s'ha trobat l'ODS configurat: {ods_path}")

    template_path = Path(template) if template else Path(resource_path("templates/default.html"))
    css_path = Path(css) if css else Path(resource_path("templates/style-portrait.css"))
    xslt_path = (
        Path(xslt)
        if xslt
        else project_dir / configured_xslt
        if configured_xslt
        else Path(resource_path("ods2html.xslt"))
    )

    front_matter_file = project_dir / "templates" / "front-matter.md"
    temp_markdown = project_dir / "generated_content.md"
    temp_html = project_dir / "generated_content.html"

    all_markdown_content = ""
    if front_matter_file.exists():
        all_markdown_content += front_matter_file.read_text(encoding="utf-8") + "\n"
    else:
        all_markdown_content += default_front_matter(config, project_dir) + "\n"

    for nav_file in iter_nav_files(config.get("nav", [])):
        markdown_file = project_dir / "docs" / nav_file
        if markdown_file.is_file() and markdown_file.suffix == ".md":
            print(f"Processant fitxer markdown: {markdown_file}")
            all_markdown_content += render_markdown_to_html(markdown_file, ods_path, xslt_path)
            all_markdown_content += "\n\n"
        else:
            print(f"Saltant element no valid: {markdown_file}")

    temp_markdown.write_text(all_markdown_content, encoding="utf-8")

    ensure_pandoc()
    subprocess.run(
        pandoc_command(temp_markdown, temp_html, template_path, css_path),
        check=True,
        cwd=project_dir,
    )

    output_pdf = Path(output_pdf)
    if not output_pdf.is_absolute():
        output_pdf = project_dir / output_pdf
    subprocess.run([sys.executable, "-m", "weasyprint", str(temp_html), str(output_pdf)], check=True)

    print(f"PDF generat correctament: {output_pdf}")

    if keep_html:
        print(f"Fitxer HTML temporal guardat: {temp_html}")
        print(f"Fitxer Markdown temporal guardat: {temp_markdown}")
        return

    for temp_file in (temp_html, temp_markdown):
        if temp_file.exists():
            temp_file.unlink()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Genera el PDF d'un projecte PCCF/Programacio MkDocs."
    )
    parser.add_argument("output_pdf", nargs="?", default="output.pdf")
    parser.add_argument(
        "--project-dir",
        default=os.getcwd(),
        help="Directori del projecte amb mkdocs.yml. Per defecte, el directori actual.",
    )
    parser.add_argument("--keep-html", action="store_true")
    parser.add_argument("--template", help="Plantilla HTML de Pandoc alternativa.")
    parser.add_argument("--css", help="CSS de PDF alternatiu.")
    parser.add_argument("--xslt", help="XSLT alternatiu, conservat per compatibilitat.")
    return parser.parse_args()


def main():
    args = parse_args()
    generate_pdf(
        Path(args.project_dir),
        args.output_pdf,
        keep_html=args.keep_html,
        template=args.template,
        css=args.css,
        xslt=args.xslt,
    )


if __name__ == "__main__":
    main()
