import os
import subprocess
import yaml
import sys
from add_tables.transformer import process_markdown
from weasyprint import HTML

def yaml_ignore(loader, node):
    """Constructor segur per ignorar etiquetes !!python/name"""
    return str(node.value)

# Cobrir tant multi_constructor com el tag exacte
yaml.SafeLoader.add_multi_constructor("!python/name:", lambda loader, suffix, node: yaml_ignore(loader, node))
yaml.SafeLoader.add_constructor("tag:yaml.org,2002:python/name:material.extensions.emoji.twemoji", yaml_ignore)
yaml.SafeLoader.add_constructor("tag:yaml.org,2002:python/name:material.extensions.emoji.to_svg", yaml_ignore)
yaml.SafeLoader.add_constructor("tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format", yaml_ignore)

def load_nav():
    """Llegeix el fitxer mkdocs.yml i retorna l'ordre dels fitxers markdown"""
    with open("mkdocs.yml", "r", encoding="utf-8") as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
    return config.get("nav", [])

def render_markdown_to_html(input_file, ods_path, xslt_path):
    """Genera HTML a partir de markdown amb les taules transformades"""
    with open(input_file, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Processa les marques amb el plugin
    return process_markdown(markdown_content, ods_path, xslt_path)

def convert_markdown_to_html(input_file, output_file):
    """Convierte el markdown a HTML utilitzant Pandoc i plantilla"""
    cmd = [
        "pandoc", "-s", "--template=templates/default.html", 
        "-f", "markdown-smart+raw_html", 
        "--toc", 
        "-c", "templates/style-portrait.css", 
        input_file, 
        "-o", output_file
    ]
    subprocess.run(cmd, check=True)

def generate_pdf_from_html(input_html, output_pdf):
    """Genera el PDF amb WeasyPrint a partir del HTML"""
    HTML(filename=input_html).write_pdf(output_pdf)

def generate_pdf(output_pdf="output.pdf", keep_html=False):
    # Llegeix la configuració de `mkdocs.yml` i agafa els fitxers Markdown
    nav = load_nav()
    ods_path = "PCCF_FPB.ods"  # O especifica on tens el fitxer ODS
    xslt_path = "ods2html.xslt"  # O especifica el camí correcte al fitxer XSLT

    # Ruta al fitxer de front-matter
    front_matter_file = "templates/front-matter.md"

    # Crea un fitxer Markdown temporal al directori actual
    temp_markdown = "generated_content.md"

    # Llegeix i afegeix front-matter només una vegada
    all_markdown_content = ""
    if os.path.exists(front_matter_file):
        with open(front_matter_file, "r", encoding="utf-8") as f:
            front_matter = f.read()
        all_markdown_content += front_matter  # Afegim el front-matter al principi

    # Processa cada fitxer markdown per generar les taules HTML
    for section in nav:
        for section_name, files in section.items():
            # Si el valor és una cadena (un fitxer) en comptes de llista
            markdown_file = f"docs/{files}"

            # Comprovem que és un fitxer .md
            if os.path.isfile(markdown_file) and markdown_file.endswith(".md"):
                print(f"Processant fitxer markdown: {markdown_file}")
                html_content = render_markdown_to_html(markdown_file, ods_path, xslt_path)
                all_markdown_content += html_content  # Concatenem el resultat HTML
            else:
                print(f"Saltant element no vàlid: {markdown_file}")

    # Guardem el Markdown concatenat amb el front-matter
    with open(temp_markdown, "w", encoding="utf-8") as f:
        f.write(all_markdown_content)

    # Generar el HTML des del Markdown amb taules processades
    temp_html = "generated_content.html"
    convert_markdown_to_html(temp_markdown, temp_html)

    # Genera el PDF a partir de l'HTML amb WeasyPrint
    generate_pdf_from_html(temp_html, output_pdf)

    print(f"PDF generat correctament: {output_pdf}")

    # Eliminar fitxer HTML temporal si no es vol mantenir
    if not keep_html:
        os.remove(temp_html)
        print(f"Fitxer temporal {temp_html} eliminat.")
    else:
        print(f"Fitxer HTML temporal guardat: {temp_html}")

    # Eliminar fitxer Markdown temporal
    if not keep_html:
        os.remove(temp_markdown)
        print(f"Fitxer temporal {temp_markdown} eliminat.")

if __name__ == "__main__":
    # Opcional: passar el nom del fitxer PDF de sortida i controlar si mantenir el fitxer HTML temporal
    output_pdf = "output.pdf"
    keep_html = "--keep-html" in sys.argv

    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        # Si s'ha passat el nom del fitxer PDF per la línia de comandes
        output_pdf = sys.argv[1]

    generate_pdf(output_pdf, keep_html)
