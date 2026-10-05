import argparse
import re
import subprocess
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "zensical.toml"
DOCS = ROOT / "docs"
PDF_TEMPLATES = ROOT / "pdf-templates"
TEMPLATE = PDF_TEMPLATES / "default.html"
CSS = PDF_TEMPLATES / "pdf.css"
FRONT_MATTER = PDF_TEMPLATES / "front-matter.md"
TOOLS = ROOT / "tools"
SYNC_SCRIPT = TOOLS / "sync_ods_tables_site.py"
ODS = ROOT / "PD_SBD.ods"
XSLT = ROOT / "ods2html.xslt"
ODS_TOOLS = ROOT / "ods-tools"


def strip_front_matter(text):
    if not text.startswith("---\n"):
        return text
    parts = text.split("\n---\n", 1)
    return parts[1].lstrip() if len(parts) == 2 else text


def normalize_raw_divs_for_pandoc(text):
    text = re.sub(r'<div class="page-break"></div>',
                  '::: { .page-break }\n:::', text)
    classes = (
        "table-fit-content", "table-assessment-compact", "table-ra-compact",
        "table-contribucio-ra", "table-qualifications",
        "table-qualifications-pdf-fix",
    )
    pattern = "|".join(re.escape(x) for x in classes)

    def replace_wrapper(match):
        found = [x for x in match.group("classes").split() if x in classes]
        if not found:
            return match.group(0)
        table = re.sub(
            r"<table(?![^>]*\bclass=)",
            f'<table class="{" ".join(found)}"',
            match.group("table"), count=1
        )
        return (match.group("comments") or "") + table

    text = re.sub(
        rf'<div class="(?P<classes>[^"]*\b(?:{pattern})\b[^"]*)">\s*'
        r'(?P<comments>(?:<!--.*?-->\s*)*)'
        r'(?P<table><table.*?</table>)\s*</div>',
        replace_wrapper, text, flags=re.DOTALL
    )
    text = re.sub(r'(<td>)([a-z])\)\s+', r'\1\2&#41; ', text)
    text = re.sub(r'(<br/>)([a-z])\)\s+', r'\1\2&#41; ', text)
    return text


def load_config():
    return tomllib.loads(CONFIG.read_text(encoding="utf-8"))


def extract_nav_files(value):
    result = []
    if isinstance(value, list):
        for item in value:
            result.extend(extract_nav_files(item))
    elif isinstance(value, dict):
        for item in value.values():
            result.extend(extract_nav_files(item))
    elif isinstance(value, str) and value.lower().endswith(".md"):
        result.append(DOCS / value)
    return result


def load_nav_docs():
    nav = load_config().get("navigation", {}).get("nav", [])
    docs = extract_nav_files(nav)
    if not docs:
        raise RuntimeError("No s'han trobat documents en [navigation] nav.")
    return docs


def build_front_matter():
    """Llig pdf-templates/front-matter.md i l'embolcalla com a YAML."""
    if not FRONT_MATTER.exists():
        raise FileNotFoundError(f"No existeix: {FRONT_MATTER}")

    content = FRONT_MATTER.read_text(encoding="utf-8").strip()

    # També admet un fitxer que ja continga els delimitadors YAML.
    if content.startswith("---"):
        return content.rstrip() + "\n"

    return "---\n" + content + "\n---\n"


def check_files(do_sync):
    required = [CONFIG, DOCS, TEMPLATE, CSS, FRONT_MATTER]
    if do_sync:
        required += [SYNC_SCRIPT, ODS, XSLT, ODS_TOOLS]
    missing = [p for p in required if not p.exists()]
    if missing:
        raise FileNotFoundError(
            "Falten:\n" + "\n".join(f"  - {p}" for p in missing))


def sync_ods():
    print("🔄 Sincronitzant les taules ODS...")
    subprocess.run([
        sys.executable, str(SYNC_SCRIPT), str(ROOT),
        str(ODS), str(XSLT), str(ODS_TOOLS)
    ], check=True, cwd=ROOT)


def combined_markdown():
    docs = load_nav_docs()
    chunks = [build_front_matter().rstrip() + "\n\n"]
    print(f"📚 {len(docs)} documents en la navegació.")
    for i, path in enumerate(docs):
        if not path.exists():
            raise FileNotFoundError(f"No existeix: {path}")
        print(f"➡️ {path.relative_to(ROOT)}")
        content = strip_front_matter(path.read_text(encoding="utf-8")).strip()
        chunks.append(normalize_raw_divs_for_pandoc(content))
        if i < len(docs) - 1:
            chunks.append('\n\n::: { .page-break }\n:::\n\n')
    return "\n".join(chunks) + "\n"


def run_pandoc(md, html):
    print("🔄 Generant HTML amb Pandoc...")
    subprocess.run([
        "pandoc", "-s", "--template=pdf-templates/default.html",
        "-f", "markdown-smart+raw_html", "--toc",
        "--css=pdf-templates/pdf.css", str(md), "-o", str(html)
    ], check=True, cwd=ROOT)


def run_weasyprint(html, pdf):
    print("🔄 Generant PDF amb WeasyPrint...")
    result = subprocess.run(
        [sys.executable, "-m", "weasyprint", str(html), str(pdf)],
        cwd=ROOT,
        capture_output=True,
        text=True)
    
    # Mostra stderr excepte els avisos inofensius GLib-GIO de Windows
    if result.stderr:
        lines = result.stderr.splitlines()
        filtered = [
            line for line in lines
            if "GLib-GIO-WARNING" not in line
            and "Unexpectedly, UWP app" not in line
        ]

        if filtered:
            print("\n".join(filtered), file=sys.stderr)

    if result.returncode != 0:
        raise subprocess.CalledProcessError(
            result.returncode,
            result.args
        )


def main():
    parser = argparse.ArgumentParser(
        description="Exporta un projecte Zensical a PDF en Windows.")
    parser.add_argument("output_pdf", nargs="?",
                        default="programacio-didactica_SBD.pdf")
    parser.add_argument("--keep-html", action="store_true")
    parser.add_argument("--no-sync", action="store_true",
                        help="No sincronitza les taules ODS")
    args = parser.parse_args()

    pdf = Path(args.output_pdf)
    if not pdf.is_absolute():
        pdf = ROOT / pdf

    check_files(not args.no_sync)
    if not args.no_sync:
        sync_ods()

    # Els fitxers intermedis es creen a l'arrel del projecte.
    # Això és important perquè les rutes relatives de pdf.css i de les
    # imatges (img/fondo.png, img/portada.png...) es resolguen correctament.
    md = ROOT / "combined.md"
    html = ROOT / "combined.html"

    try:
        md.write_text(combined_markdown(), encoding="utf-8")
        run_pandoc(md, html)
        run_weasyprint(html, pdf)

        if args.keep_html:
            kept_md = ROOT / "exported-programacio.md"
            kept_html = ROOT / "exported-programacio.html"

            kept_md.write_text(
                md.read_text(encoding="utf-8"), encoding="utf-8")
            kept_html.write_text(
                html.read_text(encoding="utf-8"), encoding="utf-8")

            print("ℹ️ Conservats exported-programacio.md i exported-programacio.html")

    finally:
        # combined.md i combined.html només són fitxers de treball.
        for temp_file in (md, html):
            if temp_file.exists():
                temp_file.unlink()

    print(f"\n✅ PDF generat: {pdf}")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, RuntimeError) as exc:
        print(f"\n❌ {exc}")
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        print(f"\n❌ Ha fallat una comanda externa (codi {exc.returncode}).")
        sys.exit(exc.returncode)
