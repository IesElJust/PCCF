import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent
PLUGIN_ROOT = PROJECT_ROOT / "my_plugins"

if str(PLUGIN_ROOT) not in sys.path:
    sys.path.insert(0, str(PLUGIN_ROOT))

from add_tables.transformer import process_markdown

def load_mkdocs_config(config_path=PROJECT_ROOT / "mkdocs.yml"):
    """Llegeix el fitxer mkdocs.yml."""
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_nav(config):
    """Retorna l'ordre dels fitxers markdown definit en nav."""
    return config.get("nav", [])


def load_add_tables_config(config):
    """Extreu la configuració del plugin add_tables de mkdocs.yml."""
    for plugin in config.get("plugins", []):
        if isinstance(plugin, dict) and "add_tables" in plugin:
            return plugin["add_tables"] or {}
    return {}

def render_markdown_to_html(input_file, ods_path, xslt_path):
    """Genera HTML a partir de markdown amb les taules transformades"""
    with open(input_file, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Processa les marques amb el plugin
    return process_markdown(markdown_content, ods_path, xslt_path)

def convert_markdown_to_html(input_file, output_file):
    """Convierte el markdown a HTML utilitzant Pandoc i plantilla"""
    cmd = [
        "pandoc", "-s", f"--template={PROJECT_ROOT / 'templates/default.html'}",
        "-f", "markdown-smart+raw_html",
        "--toc",
        "-c", str(PROJECT_ROOT / "templates/style-portrait.css"),
        str(input_file),
        "-o", str(output_file)
    ]
    subprocess.run(cmd, check=True)

def generate_pdf_from_html(input_html, output_pdf):
    """Genera el PDF amb WeasyPrint a partir del HTML"""
    cmd = [sys.executable, "-m", "weasyprint", str(input_html), str(output_pdf)]
    subprocess.run(cmd, check=True)

def generate_pdf(output_pdf="output.pdf", keep_html=False):
    config = load_mkdocs_config()
    nav = load_nav(config)
    plugin_config = load_add_tables_config(config)
    ods_path = PROJECT_ROOT / plugin_config.get("ods_path", "PCCE_CETI.ods")
    xslt_path = PROJECT_ROOT / plugin_config.get("xslt_path", "ods2html.xslt")
    output_pdf = Path(output_pdf)

    front_matter_file = PROJECT_ROOT / "templates/front-matter.md"

    temp_markdown_handle = tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", prefix="generated_content_", dir=PROJECT_ROOT, delete=False, encoding="utf-8"
    )
    temp_markdown = Path(temp_markdown_handle.name)
    temp_html = output_pdf.with_suffix(".html") if keep_html else temp_markdown.with_suffix(".html")

    all_markdown_content = ""
    if front_matter_file.exists():
        with open(front_matter_file, "r", encoding="utf-8") as f:
            front_matter = f.read()
        all_markdown_content += front_matter

    for section in nav:
        for _section_name, files in section.items():
            if files == "index.md":
                continue

            markdown_file = PROJECT_ROOT / "docs" / files

            if markdown_file.is_file() and markdown_file.suffix == ".md":
                print(f"Processant fitxer markdown: {markdown_file}")
                html_content = render_markdown_to_html(markdown_file, ods_path, xslt_path)
                all_markdown_content += html_content.rstrip() + "\n\n"
            else:
                print(f"Saltant element no vàlid: {markdown_file}")

    with temp_markdown_handle as f:
        f.write(all_markdown_content)

    convert_markdown_to_html(temp_markdown, temp_html)
    generate_pdf_from_html(temp_html, output_pdf)

    print(f"PDF generat correctament: {output_pdf}")

    if not keep_html:
        temp_html.unlink(missing_ok=True)
        print(f"Fitxer temporal {temp_html} eliminat.")
    else:
        print(f"Fitxer HTML temporal guardat: {temp_html}")

    temp_markdown.unlink(missing_ok=True)
    print(f"Fitxer temporal {temp_markdown} eliminat.")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Genera un PDF a partir del projecte MkDocs actual.")
    parser.add_argument("output_pdf", nargs="?", default="output.pdf", help="Nom del fitxer PDF de sortida")
    parser.add_argument("--keep-html", action="store_true", help="Conserva l'HTML intermedi")
    return parser.parse_args(argv)

if __name__ == "__main__":
    args = parse_args()
    generate_pdf(args.output_pdf, args.keep_html)
