import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

from .transformer import process_markdown


DEFAULT_CONFIG = "zensical.toml"


def relative_project_path(value, name):
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{name} ha de ser una ruta relativa dins del projecte: {path}")
    return path


def load_zensical_config(config_path):
    with config_path.open("rb") as file:
        config = tomllib.load(file)

    project = config.get("project", {})
    docs_dir = relative_project_path(project.get("docs_dir", "docs"), "project.docs_dir")
    site_dir = relative_project_path(project.get("site_dir", "site"), "project.site_dir")

    tables = config.get("pccf", {}).get("tables", {})
    if not tables.get("ods_path"):
        raise ValueError(
            "Falta pccf.tables.ods_path en el fitxer de configuració Zensical."
        )
    ods_path = relative_project_path(tables["ods_path"], "pccf.tables.ods_path")
    xslt_path = tables.get("xslt_path")
    if xslt_path:
        xslt_path = relative_project_path(xslt_path, "pccf.tables.xslt_path")
    return config, docs_dir, site_dir, ods_path, xslt_path


def resolve_zensical(explicit_path=None):
    if explicit_path:
        candidate = Path(explicit_path).expanduser()
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return candidate.resolve()
        raise FileNotFoundError(f"No s'ha trobat un executable de Zensical en: {candidate}")

    executable = shutil.which("zensical")
    if executable:
        return Path(executable).resolve()

    sibling = Path(sys.executable).resolve().parent / "zensical"
    if sibling.is_file() and os.access(sibling, os.X_OK):
        return sibling

    candidate = Path.home() / ".local" / "zensicalenv" / "bin" / "zensical"
    if candidate.is_file() and os.access(candidate, os.X_OK):
        return candidate.resolve()
    raise FileNotFoundError(
        "No s'ha trobat Zensical. Executa ./setup_entorn.sh o indica el binari "
        "amb --zensical."
    )


def copy_optional_theme_dir(config, project_dir, staging_dir):
    custom_dir = config.get("project", {}).get("theme", {}).get("custom_dir")
    if not custom_dir:
        return
    relative_dir = Path(custom_dir)
    if relative_dir.is_absolute() or ".." in relative_dir.parts:
        raise ValueError(f"project.theme.custom_dir ha de ser una ruta relativa: {relative_dir}")
    source = project_dir / relative_dir
    if source.is_dir():
        shutil.copytree(source, staging_dir / relative_dir)


def prepare_staging_project(project_dir, config_path, staging_dir, docs_dir, ods_path, xslt_path):
    source_docs = project_dir / docs_dir
    if not source_docs.is_dir():
        raise FileNotFoundError(f"No s'ha trobat el directori de documentació: {source_docs}")

    staging_docs = staging_dir / docs_dir
    shutil.copytree(source_docs, staging_docs)
    shutil.copy2(config_path, staging_dir / DEFAULT_CONFIG)

    replaced_files = 0
    for markdown_file in staging_docs.rglob("*.md"):
        original = markdown_file.read_text(encoding="utf-8")
        rendered = process_markdown(original, str(ods_path), str(xslt_path))
        if rendered != original:
            markdown_file.write_text(rendered, encoding="utf-8")
            replaced_files += 1
    return replaced_files


def publish_site(staged_site, destination):
    if not staged_site.is_dir():
        raise RuntimeError(f"Zensical no ha generat el directori esperat: {staged_site}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    backup = destination.with_name(f".{destination.name}.backup")
    if backup.exists():
        shutil.rmtree(backup)
    if destination.exists():
        destination.rename(backup)

    try:
        shutil.copytree(staged_site, destination)
    except Exception:
        if destination.exists():
            shutil.rmtree(destination)
        if backup.exists():
            backup.rename(destination)
        raise
    else:
        if backup.exists():
            shutil.rmtree(backup)


def build_zensical_site(project_dir, config_name=DEFAULT_CONFIG, zensical=None, strict=False):
    project_dir = Path(project_dir).resolve()
    config_path = project_dir / config_name
    if not config_path.is_file():
        raise FileNotFoundError(f"No s'ha trobat {config_path}")

    zensical_config, docs_dir, site_dir, configured_ods, configured_xslt = (
        load_zensical_config(config_path)
    )
    ods_path = project_dir / configured_ods
    if not ods_path.is_file():
        raise FileNotFoundError(f"No s'ha trobat l'ODS configurat: {ods_path}")

    xslt_path = project_dir / configured_xslt if configured_xslt else None
    if xslt_path is not None and not xslt_path.is_file():
        raise FileNotFoundError(f"No s'ha trobat l'XSLT configurat: {xslt_path}")

    zensical_bin = resolve_zensical(zensical)
    with tempfile.TemporaryDirectory(prefix="pccf-zensical-") as temp_dir:
        staging_dir = Path(temp_dir)
        replaced_files = prepare_staging_project(
            project_dir, config_path, staging_dir, docs_dir, ods_path, xslt_path
        )
        copy_optional_theme_dir(zensical_config, project_dir, staging_dir)

        command = [str(zensical_bin), "build", "-f", DEFAULT_CONFIG]
        if strict:
            command.append("--strict")
        subprocess.run(command, cwd=staging_dir, check=True)
        publish_site(staging_dir / site_dir, project_dir / site_dir)

    print(f"Taules ODS incorporades en {replaced_files} fitxers Markdown.")
    print(f"Lloc Zensical generat: {project_dir / site_dir}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Genera un lloc Zensical incorporant prèviament les taules ODS."
    )
    parser.add_argument(
        "--project-dir",
        default=os.getcwd(),
        help="Directori amb zensical.toml. Per defecte, el directori actual.",
    )
    parser.add_argument(
        "--config-file",
        default=DEFAULT_CONFIG,
        help=f"Nom del fitxer de configuració Zensical. Per defecte: {DEFAULT_CONFIG}.",
    )
    parser.add_argument("--zensical", help="Ruta alternativa al binari de Zensical.")
    parser.add_argument("--strict", action="store_true", help="Activa la compilació estricta.")
    return parser.parse_args()


def main():
    args = parse_args()
    build_zensical_site(
        args.project_dir,
        config_name=args.config_file,
        zensical=args.zensical,
        strict=args.strict,
    )


if __name__ == "__main__":
    main()
