import argparse
import html
import os
import shutil
import tempfile
import tomllib
from dataclasses import dataclass
from datetime import datetime
from importlib.resources import files
from pathlib import Path

from .cli import generate_pdf
from .zensical_cli import build_zensical_site


CYCLE_GROUPS = [
    ("CFGM", "Cicles formatius de grau mitjà", ["SMX"]),
    ("CFGB", "Cicles formatius de grau bàsic", ["FPB"]),
    ("CFGS", "Cicles formatius de grau superior", ["ASIX", "DAM", "DAW"]),
    ("CE", "Cursos d'especialització", ["CE_CIBER", "CE_IA_BIGDATA"]),
]

CYCLE_NAMES = {
    "SMX": "Sistemes Microinformàtics i Xarxes",
    "FPB": "Informàtica d'Oficina",
    "ASIX": "Administració de Sistemes Informàtics en Xarxa",
    "DAM": "Desenvolupament d'Aplicacions Multiplataforma",
    "DAW": "Desenvolupament d'Aplicacions Web",
    "CE_CIBER": "Ciberseguretat en Entorns de les Tecnologies de la Informació",
    "CE_IA_BIGDATA": "Intel·ligència Artificial i Big Data",
}

COURSE_NAMES = {"1r": "Mòduls de primer curs", "2n": "Mòduls de segon curs"}


@dataclass
class Site:
    project_dir: Path
    destination: Path
    title: str
    cycle: str
    course: str | None = None
    code: str | None = None
    kind: str = "module"
    error: str | None = None
    pdf_available: bool = False
    pdf_error: str | None = None

    @property
    def url(self):
        return self.destination.as_posix() + "/"


def site_title(config_path):
    with config_path.open("rb") as file:
        return tomllib.load(file).get("project", {}).get("site_name", config_path.parent.name)


def discover_sites(root_dir):
    sites = []
    for project_dir in sorted(root_dir.glob("PCCF_*")):
        if project_dir.name.endswith("_old"):
            continue
        config = project_dir / "zensical.toml"
        if config.is_file():
            cycle = project_dir.name.removeprefix("PCCF_")
            sites.append(
                Site(
                    project_dir=project_dir,
                    destination=Path("PCCF") / project_dir.name,
                    title=site_title(config),
                    cycle=cycle,
                    kind="pccf",
                )
            )

    programmes = root_dir / "Programacions"
    for config in sorted(programmes.rglob("zensical.toml")):
        if ".venv" in config.parts:
            continue
        relative = config.parent.relative_to(programmes)
        parts = relative.parts
        if parts[0] == "Progamacio_Base":
            continue
        cycle = parts[0]
        course = parts[1] if len(parts) > 2 and parts[1] in COURSE_NAMES else None
        sites.append(
            Site(
                project_dir=config.parent,
                destination=Path("Moduls") / relative,
                title=site_title(config),
                cycle=cycle,
                course=course,
                code=parts[-1],
            )
        )
    return sites


def card(site):
    title = html.escape(site.title)
    code = html.escape(site.code or "Projecte curricular")
    if site.error:
        return (
            '<article class="card card--error">'
            f'<span class="card__code">{code}</span>'
            f'<h5>{title}</h5><p>{html.escape(site.error)}</p>'
            '<span class="card__status">No disponible</span></article>'
        )
    pdf_action = ""
    if site.pdf_available:
        pdf_action = (
            f'<a class="card__action card__action--pdf" '
            f'href="{html.escape(site.url)}document.pdf" download>Descarrega el PDF ↓</a>'
        )
    elif site.pdf_error:
        pdf_action = (
            f'<span class="card__pdf-error" title="{html.escape(site.pdf_error)}">'
            "PDF no disponible</span>"
        )
    return (
        '<article class="card">'
        f'<a class="card__main" href="{html.escape(site.url)}">'
        f'<span class="card__code">{code}</span><h5>{title}</h5></a>'
        '<div class="card__actions">'
        f'<a class="card__action" href="{html.escape(site.url)}">Obri la documentació →</a>'
        f'{pdf_action}</div></article>'
    )


PDF_DOWNLOAD_CSS = """
.pccf-pdf-download {
  margin: 1rem auto 0;
  padding: 0 1rem;
  max-width: 61rem;
}
.pccf-pdf-download a {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  padding: .55rem .9rem;
  border-radius: .4rem;
  color: var(--md-primary-bg-color, #fff);
  background: var(--md-primary-fg-color, #6041a5);
  font-weight: 700;
  text-decoration: none;
  box-shadow: 0 .15rem .4rem rgba(0, 0, 0, .12);
}
.pccf-pdf-download a:hover { filter: brightness(1.08); }
""".strip()


def add_pdf_download_to_site(site_dir):
    index_path = site_dir / "index.html"
    if not index_path.is_file():
        raise FileNotFoundError(f"No s'ha trobat la portada Zensical: {index_path}")
    source = index_path.read_text(encoding="utf-8")
    stylesheet = '<link rel="stylesheet" href="pccf-pdf-download.css">'
    banner = (
        '<aside class="pccf-pdf-download" aria-label="Descàrrega del document">'
        '<a href="document.pdf" download>Descarrega el document complet en PDF ↓</a>'
        "</aside>"
    )
    if "</head>" not in source:
        raise ValueError(f"La portada no conté </head>: {index_path}")
    source = source.replace("</head>", f"  {stylesheet}\n</head>", 1)
    main_start = source.find('<main class="md-main"')
    main_end = source.find(">", main_start)
    if main_start == -1 or main_end == -1:
        raise ValueError(f"La portada no conté el bloc principal esperat: {index_path}")
    source = source[: main_end + 1] + "\n" + banner + source[main_end + 1 :]
    index_path.write_text(source, encoding="utf-8")
    (site_dir / "pccf-pdf-download.css").write_text(PDF_DOWNLOAD_CSS + "\n", encoding="utf-8")


def cycle_section(cycle, sites):
    cycle_sites = [site for site in sites if site.cycle == cycle]
    if not cycle_sites:
        return ""
    name = CYCLE_NAMES.get(cycle, cycle.replace("_", " "))
    pccf = next((site for site in cycle_sites if site.kind == "pccf"), None)
    modules = [site for site in cycle_sites if site.kind == "module"]
    module_count = (
        f"{len(modules)} mòdul" if len(modules) == 1 else f"{len(modules)} mòduls"
    )
    content = [
        '<details class="cycle" open>',
        f'<summary><span class="cycle__code">{html.escape(cycle)}</span>'
        f'<span>{html.escape(name)}</span><span class="cycle__count">{module_count}</span></summary>',
        '<div class="cycle__body">',
    ]
    if pccf:
        content.extend(['<h4>Projecte curricular</h4>', '<div class="cards cards--pccf">', card(pccf), "</div>"])
    if modules:
        content.append("<h4>Programacions didàctiques</h4>")
        course_order = ["1r", "2n", None]
        for course in course_order:
            course_sites = [site for site in modules if site.course == course]
            if not course_sites:
                continue
            heading = COURSE_NAMES.get(course, "Altres mòduls i projectes")
            content.extend(
                [
                    f'<section class="course"><h5>{heading}</h5><div class="cards">',
                    *(card(site) for site in course_sites),
                    "</div></section>",
                ]
            )
    content.extend(["</div>", "</details>"])
    return "".join(content)


def landing_content(sites):
    sections = []
    known_cycles = set()
    for code, title, cycles in CYCLE_GROUPS:
        body = "".join(cycle_section(cycle, sites) for cycle in cycles)
        if body:
            sections.append(
                f'<section class="family" id="{code.lower()}"><div class="section-heading">'
                f'<span>{code}</span><h2>{title}</h2></div>{body}</section>'
            )
        known_cycles.update(cycles)
    other_cycles = sorted({site.cycle for site in sites} - known_cycles)
    other = "".join(cycle_section(cycle, sites) for cycle in other_cycles)
    if other:
        sections.append(
            '<section class="family" id="altres"><div class="section-heading">'
            '<span>Altres</span><h2>Altres programacions</h2></div>' + other + "</section>"
        )
    return "".join(sections)


def publish_directory(staging, destination):
    backup = destination.with_name(f".{destination.name}.backup")
    if backup.exists():
        shutil.rmtree(backup)
    if destination.exists():
        destination.rename(backup)
    try:
        staging.rename(destination)
    except Exception:
        if backup.exists():
            backup.rename(destination)
        raise
    else:
        if backup.exists():
            shutil.rmtree(backup)


def build_full_documentation(
    root_dir,
    output_dir="zensical_full_doc",
    zensical=None,
    strict=False,
    with_pdf=True,
):
    root_dir = Path(root_dir).resolve()
    output_dir = Path(output_dir)
    if not output_dir.is_absolute():
        output_dir = root_dir / output_dir
    output_dir = output_dir.resolve()
    if output_dir == root_dir or root_dir not in output_dir.parents:
        raise ValueError("El directori d'eixida ha d'estar dins de l'arrel del repositori.")
    sites = discover_sites(root_dir)
    if not sites:
        raise RuntimeError("No s'ha trobat cap projecte amb zensical.toml.")

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="pccf-full-", dir=output_dir.parent) as temp_dir:
        staging = Path(temp_dir) / output_dir.name
        staging.mkdir()
        for index, site in enumerate(sites, start=1):
            relative_project = site.project_dir.relative_to(root_dir)
            print(f"[{index}/{len(sites)}] {relative_project}")
            try:
                generated = build_zensical_site(
                    site.project_dir,
                    zensical=zensical,
                    strict=strict,
                )
                destination = staging / site.destination
                shutil.copytree(generated, destination)
                if with_pdf:
                    try:
                        generate_pdf(site.project_dir, destination / "document.pdf")
                        add_pdf_download_to_site(destination)
                        site.pdf_available = True
                    except Exception as exc:
                        site.pdf_error = str(exc).replace(f"{root_dir}{os.sep}", "")
                        print(f"  AVÍS PDF: {site.pdf_error}")
            except Exception as exc:
                site.error = str(exc).replace(f"{root_dir}{os.sep}", "")
                print(f"  ERROR: {site.error}")

        template_dir = files("pccf_pdf").joinpath("resources/templates")
        template = template_dir.joinpath("zensical-index.html").read_text(encoding="utf-8")
        generated_at = datetime.now()
        rendered = (
            template.replace("{{CONTENT}}", landing_content(sites))
            .replace("{{GENERATED_AT}}", generated_at.strftime("%d/%m/%Y %H:%M"))
            .replace("{{BUILD_ID}}", generated_at.strftime("%Y%m%d%H%M%S"))
        )
        (staging / "index.html").write_text(rendered, encoding="utf-8")
        (staging / "index.css").write_bytes(
            template_dir.joinpath("zensical-index.css").read_bytes()
        )
        (staging / "logo_gran.png").write_bytes(
            template_dir.joinpath("img/logo_gran.png").read_bytes()
        )
        (staging / ".nojekyll").touch()
        publish_directory(staging, output_dir)

    failures = [site for site in sites if site.error]
    pdf_failures = [site for site in sites if site.pdf_error]
    print(f"Documentació global generada: {output_dir}")
    print(f"Projectes correctes: {len(sites) - len(failures)}/{len(sites)}")
    if failures:
        print(f"Projectes no disponibles: {len(failures)}")
    if with_pdf:
        print(f"PDF correctes: {len(sites) - len(failures) - len(pdf_failures)}/{len(sites) - len(failures)}")
        if pdf_failures:
            print(f"PDF no disponibles: {len(pdf_failures)}")
    return output_dir, failures


def parse_args():
    parser = argparse.ArgumentParser(
        description="Genera tots els llocs Zensical i una portada global."
    )
    parser.add_argument("--root-dir", default=os.getcwd(), help="Arrel del repositori.")
    parser.add_argument(
        "--output-dir", default="zensical_full_doc", help="Directori global d'eixida."
    )
    parser.add_argument("--zensical", help="Ruta alternativa al binari de Zensical.")
    parser.add_argument("--strict", action="store_true", help="Activa la compilació estricta.")
    parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="No genera els PDF ni els botons de descàrrega.",
    )
    parser.add_argument(
        "--fail-on-error",
        action="store_true",
        help="Retorna un codi d'error si algun projecte no es pot construir.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    _, failures = build_full_documentation(
        args.root_dir,
        output_dir=args.output_dir,
        zensical=args.zensical,
        strict=args.strict,
        with_pdf=not args.no_pdf,
    )
    if failures and args.fail_on_error:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
