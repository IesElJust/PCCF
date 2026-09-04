import os
import subprocess
import yaml
import sys
from pathlib import Path
from add_tables.transformer import process_markdown
from weasyprint import HTML

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
        # Si ha generat PDF, no parem l’execució

# 🧹 Neteja del .tex
def clean_tex(tex_file):
    p = Path(tex_file)
    if not p.exists():
        return
    content = p.read_text(encoding="utf-8")
    # Eliminar seqüències que trenquen compilació
    content = content.replace("TableCell", "")
    content = content.replace("Plain(Str(", "")
    content = content.replace("));", "")
    p.write_text(content, encoding="utf-8")
    print(f"🧹 Fitxer {tex_file} netejat.")

def mode_md(nav, output_pdf, keep_html):
    ods_path = "PCCF_FPB.ods"
    xslt_path = "ods2html.xslt"
    front_matter_file = "templates/front-matter.md"
    temp_md = "generated_content.md"
    all_content = ""

    if Path(front_matter_file).exists():
        all_content += Path(front_matter_file).read_text(encoding="utf-8")

    for section in nav:
        for _, file in section.items():
            md_file = Path("docs") / file
            if md_file.exists():
                print(f"Processant fitxer markdown: {md_file}")
                md_content = md_file.read_text(encoding="utf-8")
                html_content = process_markdown(md_content, ods_path, xslt_path)
                all_content += html_content
            else:
                print(f"⚠️ Fitxer no trobat: {md_file}")

    Path(temp_md).write_text(all_content, encoding="utf-8")

    temp_html = "generated_content.html"
    run_cmd(f"pandoc -s --template=templates/default.html -f markdown-smart+raw_html --toc "
            f"-c templates/style-portrait.css {temp_md} -o {temp_html}", "Error en pandoc")

    HTML(filename=temp_html).write_pdf(output_pdf)
    print(f"✅ PDF generat correctament: {output_pdf}")

    if not keep_html:
        Path(temp_md).unlink(missing_ok=True)
        Path(temp_html).unlink(missing_ok=True)

def mode_html(nav, output_pdf):
    print("📁 Generant la web amb MkDocs...")
    run_cmd("mkdocs build", "Error en MkDocs build")
    print("✅ Web generada correctament.")

    combined = "combined.md"
    with open(combined, "w", encoding="utf-8") as outfile:
        preamble_file = Path("preamble.md")
        if preamble_file.exists():
            outfile.write(preamble_file.read_text(encoding="utf-8"))
            outfile.write("\n\n")

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
        f"-o {tex_file}"
    )
    run_cmd(pandoc_cmd, "Error generant TEX")

    # 🔧 Neteja abans de compilar
    clean_tex(tex_file)

    # Compilar a PDF amb xelatex
    run_cmd(f"xelatex -interaction=nonstopmode {tex_file}", "Error en xelatex")
    run_cmd(f"xelatex -interaction=nonstopmode {tex_file}", "Error en xelatex")
    run_cmd(f"xelatex -interaction=nonstopmode {tex_file}", "Error en xelatex")

    pdf_output = Path(tex_file).with_suffix(".pdf")
    if pdf_output.exists():
        # Si el fitxer de destí ja existeix, esborrem-lo abans
        dest = Path(output_pdf)
        if dest.exists():
            dest.unlink()
        pdf_output.rename(dest)

        print(f"✅ PDF generat correctament: {output_pdf}")
    else:
        print("❌ Error: no s'ha generat el PDF")

    for tmp in Path(".").glob("filtered_*.html"):
        tmp.unlink()
    for tmp in Path(".").glob("converted_*.md"):
        tmp.unlink()

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
