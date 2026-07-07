import argparse
import importlib.util
import os
import subprocess
import sys

import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSFORMER_PATH = os.path.join(
    SCRIPT_DIR, "my_plugins", "add_tables", "transformer.py"
)

transformer_spec = importlib.util.spec_from_file_location(
    "add_tables_transformer", TRANSFORMER_PATH
)
transformer = importlib.util.module_from_spec(transformer_spec)
transformer_spec.loader.exec_module(transformer)
process_markdown = transformer.process_markdown


def load_config():
    """Llegeix mkdocs.yml i retorna l'ODS configurat i l'ordre del nav."""
    with open("mkdocs.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    ods_path = None
    for plugin in config.get("plugins", []):
        if isinstance(plugin, dict) and "add_tables" in plugin:
            ods_path = plugin["add_tables"].get("ods_path")
            break

    if not ods_path:
        raise ValueError("No s'ha trobat plugins.add_tables.ods_path en mkdocs.yml")

    return ods_path, config.get("nav", [])


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


def render_markdown_to_html(input_file, ods_path, xslt_path):
    """Genera HTML a partir del markdown amb les taules de l'ODS transformades."""
    with open(input_file, "r", encoding="utf-8") as file:
        markdown_content = file.read()
    return process_markdown(markdown_content, ods_path, xslt_path)


def convert_markdown_to_html(input_file, output_file):
    """Converteix el markdown a HTML utilitzant Pandoc i la plantilla."""
    cmd = [
        "pandoc",
        "-s",
        "--template=templates/default.html",
        "-f",
        "markdown-smart+raw_html",
        "--toc",
        "-c",
        "templates/style-portrait.css",
        input_file,
        "-o",
        output_file,
    ]
    subprocess.run(cmd, check=True)


def generate_pdf_from_html(input_html, output_pdf):
    """Genera el PDF amb WeasyPrint a partir de l'HTML."""
    cmd = [sys.executable, "-m", "weasyprint", input_html, output_pdf]
    subprocess.run(cmd, check=True)


def generate_pdf(output_pdf="output.pdf", keep_html=False):
    ods_path, nav = load_config()
    xslt_path = "ods2html.xslt"
    front_matter_file = "templates/front-matter.md"
    temp_markdown = "generated_content.md"
    temp_html = "generated_content.html"

    all_markdown_content = ""
    if os.path.exists(front_matter_file):
        with open(front_matter_file, "r", encoding="utf-8") as file:
            all_markdown_content += file.read() + "\n"

    for nav_file in iter_nav_files(nav):
        markdown_file = os.path.join("docs", nav_file)
        if os.path.isfile(markdown_file) and markdown_file.endswith(".md"):
            print(f"Processant fitxer markdown: {markdown_file}")
            html_content = render_markdown_to_html(markdown_file, ods_path, xslt_path)
            all_markdown_content += html_content + "\n"
        else:
            print(f"Saltant element no valid: {markdown_file}")

    with open(temp_markdown, "w", encoding="utf-8") as file:
        file.write(all_markdown_content)

    convert_markdown_to_html(temp_markdown, temp_html)
    generate_pdf_from_html(temp_html, output_pdf)

    print(f"PDF generat correctament: {output_pdf}")

    if keep_html:
        print(f"Fitxer HTML temporal guardat: {temp_html}")
        print(f"Fitxer Markdown temporal guardat: {temp_markdown}")
        return

    for temp_file in (temp_html, temp_markdown):
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"Fitxer temporal {temp_file} eliminat.")


def parse_args():
    parser = argparse.ArgumentParser(description="Genera el PDF del projecte MkDocs.")
    parser.add_argument("output_pdf", nargs="?", default="output.pdf")
    parser.add_argument("--keep-html", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    os.chdir(SCRIPT_DIR)
    args = parse_args()
    generate_pdf(args.output_pdf, args.keep_html)
