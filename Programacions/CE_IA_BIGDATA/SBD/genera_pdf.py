import os
import sys
import subprocess
import yaml
from add_tables.transformer import process_markdown

def load_nav():
    """Llegeix el fitxer mkdocs.yml i retorna l'ordre dels fitxers markdown"""
    with open("mkdocs.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
        ods_path = config['plugins'][1]['add_tables']['ods_path']
    return ods_path, config.get("nav", [])

def render_markdown_to_html(input_file, ods_path, xslt_path):
    """Genera HTML a partir de markdown amb les taules transformades"""
    with open(input_file, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    return process_markdown(markdown_content, ods_path, xslt_path)

def convert_markdown_to_html(input_file, output_file):
    """Convierte el markdown a HTML utilitzant Pandoc i plantilla"""
    cmd = [
        "pandoc",
        "-s",
        "--template=templates/default.html",
        "-f", "markdown-smart+raw_html",
        "--toc",
        "-c", "templates/style-portrait.css",
        input_file,
        "-o", output_file
    ]
    subprocess.run(cmd, check=True)

def generate_pdf_from_html(input_html, output_pdf):
    """Genera el PDF amb WeasyPrint a partir del HTML"""
    python_exec = sys.executable  # Usa el mismo intérprete que ejecuta este script
    cmd = [python_exec, "-m", "weasyprint", input_html, output_pdf]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("❌ Error generant el PDF amb WeasyPrint.")
        print(f"Comando ejecutado: {' '.join(cmd)}")
        print(f"Codi de sortida: {e.returncode}")
        print("Verifica que WeasyPrint esté instalado con:")
        print("  pip install weasyprint")
        sys.exit(1)

def generate_pdf(output_pdf="output.pdf", keep_html=False):
    """Flux principal de generació del PDF"""
    ods_path, nav = load_nav()
    xslt_path = "ods2html.xslt"
    front_matter_file = "templates/front-matter.md"
    temp_markdown = "generated_content.md"
    temp_html = "generated_content.html"

    all_markdown_content = ""

    # Llegeix front-matter si existeix
    if os.path.exists(front_matter_file):
        with open(front_matter_file, "r", encoding="utf-8") as f:
            front_matter = f.read()
        all_markdown_content += front_matter + "\n"

    # Processa cada fitxer markdown
    for section in nav:
        for section_name, files in section.items():
            markdown_file = f"docs/{files}"

            if os.path.isfile(markdown_file) and markdown_file.endswith(".md"):
                print(f"Processant fitxer markdown: {markdown_file}")
                html_content = render_markdown_to_html(markdown_file, ods_path, xslt_path)
                all_markdown_content += html_content + "\n"
            else:
                print(f"Saltant element no vàlid: {markdown_file}")

    # Escriu el markdown temporal
    with open(temp_markdown, "w", encoding="utf-8") as f:
        f.write(all_markdown_content)

    # Converteix a HTML amb Pandoc
    convert_markdown_to_html(temp_markdown, temp_html)

    # Genera PDF amb WeasyPrint
    generate_pdf_from_html(temp_html, output_pdf)

    print(f"✅ PDF generat correctament: {output_pdf}")

    # Neteja fitxers temporals
    if not keep_html:
        for ftmp in [temp_markdown, temp_html]:
            if os.path.exists(ftmp):
                os.remove(ftmp)
                print(f"🗑 Fitxer temporal {ftmp} eliminat.")
    else:
        print(f"ℹ️ Fitxer HTML temporal guardat: {temp_html}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    output_pdf = "output.pdf"
    keep_html = "--keep-html" in sys.argv

    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        output_pdf = sys.argv[1]

    generate_pdf(output_pdf, keep_html)
