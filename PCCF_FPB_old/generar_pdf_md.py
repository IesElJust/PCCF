#!/usr/bin/env python3
import os
import subprocess
import yaml
import sys
from pathlib import Path
from add_tables.transformer import process_markdown
from weasyprint import HTML

# ---------------------------------------------------------
# Helpers per a YAML (ignorar constructors rars de MkDocs)
# ---------------------------------------------------------
def yaml_ignore(loader, node):
    return str(node.value)

yaml.SafeLoader.add_multi_constructor("!python/name:", lambda loader, suffix, node: yaml_ignore(loader, node))
yaml.SafeLoader.add_constructor("tag:yaml.org,2002:python/name:material.extensions.emoji.twemoji", yaml_ignore)
yaml.SafeLoader.add_constructor("tag:yaml.org,2002:python/name:material.extensions.emoji.to_svg", yaml_ignore)
yaml.SafeLoader.add_constructor("tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format", yaml_ignore)

def load_nav():
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
    return config.get("nav", [])

def run_cmd(cmd, msg_error):
    try:
        subprocess.run(cmd, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ {msg_error} (codi retorn: {e.returncode})")
        # No aturem, per si ja ha generat fitxers parcials

# ---------------------------------------------------------
# Inserir front-matter + preamble al principi
# ---------------------------------------------------------
def write_frontmatter_and_preamble(outfile):
    fm = Path("templates/front-matter.md")
    if fm.exists():
        outfile.write(fm.read_text(encoding="utf-8") + "\n\n")

    preamble = Path("preamble.md")
    if preamble.exists():
        outfile.write(preamble.read_text(encoding="utf-8") + "\n\n")



# ---------------------------------------------------------
# Iterar el nav recursivament (suporta subapartats/annexos)
# ---------------------------------------------------------
def iter_nav(nav):
    """
    Itera recursivament sobre el nav de mkdocs.yml
    i retorna tuples (títol, fitxer).
    """
    for section in nav:
        for title, value in section.items():
            if isinstance(value, str):
                yield title, value
            elif isinstance(value, list):
                # Recursió per subapartats
                yield from iter_nav(value)


# ---------------------------------------------------------
# Mode MD (directe sobre docs/*.md)
# ---------------------------------------------------------
def mode_md(nav, output_pdf, keep_html):
    ods_path = "PCCF_FPB.ods"
    xslt_path = "ods2html.xslt"
    temp_md = "generated_content.md"

    with open(temp_md, "w", encoding="utf-8") as f:
        # 🔹 Afegim portada i preàmbul
        write_frontmatter_and_preamble(f)

        for title, file in iter_nav(nav):
            md_file = Path("docs") / file
            if md_file.exists():
                print(f"Processant fitxer markdown: {md_file}")
                md_content = md_file.read_text(encoding="utf-8")
                html_content = process_markdown(md_content, ods_path, xslt_path)
                f.write(html_content + "\n\n")
            else:
                print(f"⚠️ Fitxer no trobat: {md_file}")


    tex_file = "combined_md.tex"
    pandoc_cmd = (
        f"pandoc {temp_md} --template eisvogel --pdf-engine=xelatex "
        f"--resource-path=.:docs --citeproc --bibliography=bibliografia.bib "
        f"--filter ./admonition_filter.py "
        f"--filter ./underscore_filter.py "
        f"-o {tex_file}"
    )
    run_cmd(pandoc_cmd, "Error generant TEX (mode md)")

    # Compilar 3 vegades amb xelatex
    for _ in range(3):
        run_cmd(f"xelatex -interaction=nonstopmode {tex_file}", "Error en xelatex")

    pdf_output = Path(tex_file).with_suffix(".pdf")
    if pdf_output.exists():
        dest = Path(output_pdf)
        if dest.exists():
            dest.unlink()
        pdf_output.rename(dest)
        print(f"✅ PDF generat correctament: {output_pdf}")
    else:
        print("❌ Error: no s'ha generat el PDF")

    if not keep_html:
        Path(temp_md).unlink(missing_ok=True)
        Path(tex_file).unlink(missing_ok=True)

# ---------------------------------------------------------
# Mode HTML (treballar amb site/*.html)
# ---------------------------------------------------------
def mode_html(nav, output_pdf):
    print("📁 Generant la web amb MkDocs...")
    run_cmd("mkdocs build", "Error en MkDocs build")
    print("✅ Web generada correctament.")

    combined = "combined.md"
    with open(combined, "w", encoding="utf-8") as outfile:
        # 🔹 Escriure front-matter (només YAML per a Eisvogel)
        front_matter_file = Path("templates/front-matter.md")
        if front_matter_file.exists():
            outfile.write(front_matter_file.read_text(encoding="utf-8"))
            outfile.write("\n\n")

        # 🔹 Afegir directament el contingut del preamble
        preamble_file = Path("preamble.md")
        if preamble_file.exists():
            outfile.write(preamble_file.read_text(encoding="utf-8"))
            outfile.write("\n\n")

        # 🔹 Ara enganxem la resta de seccions
        for section in nav:
            for _, file in section.items():
                base = file.replace(".md", "").replace("docs/", "").replace("\\", "/")
                html1 = Path("site") / base / "index.html"
                html2 = Path("site") / f"{base}.html"
                html_file = html1 if html1.exists() else html2

                if not html_file.exists():
                    print(f"⚠️ No trobat HTML per {file}")
                    continue

                safe_base = base.replace("/", "__")
                filtered = f"filtered_{safe_base}.html"
                converted = f"converted_{safe_base}.md"

                run_cmd(f"python extract_main_content.py {html_file} {filtered}", "Error en extract_main_content.py")
                run_cmd(f"pandoc --strip-comments --wrap=none {filtered} -o {converted}", "Error en pandoc")

                if Path(converted).exists():
                    content = Path(converted).read_text(encoding="utf-8").replace("\\", "/")
                    outfile.write(content)
                    outfile.write("\n\n")


    tex_file = "combined.tex"
    pandoc_cmd = (
        f"pandoc combined.md --template eisvogel --pdf-engine=xelatex "
        f"--resource-path=.:docs --citeproc --bibliography=bibliografia.bib "
        f"--filter ./table_filter.py "
        f"--filter ./underscore_filter.py "
        f"-o {tex_file}"
    )
    run_cmd(pandoc_cmd, "Error generant TEX")

    # Compilar 3 voltes amb xelatex
    for _ in range(3):
        run_cmd(f"xelatex -interaction=nonstopmode {tex_file}", "Error en xelatex")

    pdf_output = Path(tex_file).with_suffix(".pdf")
    if pdf_output.exists():
        dest = Path(output_pdf)
        if dest.exists():
            dest.unlink()
        pdf_output.rename(dest)
        print(f"✅ PDF generat correctament: {output_pdf}")
    else:
        print("❌ Error: no s'ha generat el PDF")

    # 🧹 Neteja
    for tmp in Path(".").glob("filtered_*.html"):
        tmp.unlink()
    for tmp in Path(".").glob("converted_*.md"):
        tmp.unlink()

# ---------------------------------------------------------
if __name__ == "__main__":
    output_pdf = "output.pdf"
    keep_html = "--keep-html" in sys.argv
    mode = "md"

    for arg in sys.argv[1:]:
        if arg.startswith("--mode="):
            mode = arg.split("=")[1]
        elif not arg.startswith("--"):
            output_pdf = arg

    nav = load_nav()

    if mode == "md":
        mode_md(nav, output_pdf, keep_html)
    elif mode == "html":
        mode_html(nav, output_pdf)
    else:
        print("❌ Mode no reconegut. Usa --mode=md o --mode=html")
