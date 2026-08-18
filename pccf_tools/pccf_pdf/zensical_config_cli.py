import argparse
import json
import os
from pathlib import Path

import yaml


class MkDocsSafeLoader(yaml.SafeLoader):
    pass


def python_name_reference(loader, suffix, node):
    loader.construct_scalar(node)
    return suffix


MkDocsSafeLoader.add_multi_constructor(
    "tag:yaml.org,2002:python/name:", python_name_reference
)


def load_mkdocs_yaml(path):
    return yaml.load(path.read_text(encoding="utf-8"), Loader=MkDocsSafeLoader) or {}


def toml_string(value):
    return json.dumps(str(value), ensure_ascii=False)


def toml_value(value):
    if isinstance(value, str):
        return toml_string(value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(toml_value(item) for item in value) + "]"
    if isinstance(value, dict):
        entries = (f"{toml_string(key)} = {toml_value(item)}" for key, item in value.items())
        return "{ " + ", ".join(entries) + " }"
    raise TypeError(f"Valor no compatible amb TOML: {value!r}")


def find_tables_config(plugins):
    for plugin in plugins or []:
        if isinstance(plugin, dict) and "add_tables" in plugin:
            config = plugin["add_tables"] or {}
            if not config.get("ods_path"):
                break
            return config["ods_path"], config.get("xslt_path")
    raise ValueError("No s'ha trobat plugins.add_tables.ods_path en el mkdocs.yml.")


def markdown_extension_sections(extensions):
    sections = {}
    for extension in extensions or []:
        if isinstance(extension, str):
            sections.setdefault(extension, {})
        elif isinstance(extension, dict):
            for name, config in extension.items():
                config = config or {}
                if (
                    name in sections
                    and isinstance(sections[name], dict)
                    and isinstance(config, dict)
                ):
                    sections[name].update(config)
                else:
                    sections[name] = config
        else:
            raise TypeError(f"Extensió Markdown no compatible: {extension!r}")
    return sections.items()


def primary_color(theme):
    palette = theme.get("palette") or {}
    if isinstance(palette, dict):
        return palette.get("primary", "deep purple")
    if isinstance(palette, list):
        for option in palette:
            if isinstance(option, dict) and option.get("primary"):
                return option["primary"]
    return "deep purple"


def render_zensical_config(mkdocs_config):
    site_name = mkdocs_config.get("site_name")
    if not site_name:
        raise ValueError("Falta site_name en el mkdocs.yml.")
    ods_path, xslt_path = find_tables_config(mkdocs_config.get("plugins"))
    theme = mkdocs_config.get("theme") or {}

    lines = [
        "# Generat amb pccf-zensical-config a partir de mkdocs.yml.",
        "[project]",
        f"site_name = {toml_string(site_name)}",
        'site_dir = "site-zensical"',
    ]
    if mkdocs_config.get("docs_dir"):
        lines.append(f"docs_dir = {toml_string(mkdocs_config['docs_dir'])}")
    if mkdocs_config.get("extra_css"):
        lines.append(f"extra_css = {toml_value(mkdocs_config['extra_css'])}")
    if mkdocs_config.get("nav"):
        lines.append(f"nav = {toml_value(mkdocs_config['nav'])}")

    lines.extend(["", "[project.theme]", 'variant = "classic"', 'language = "ca"'])
    if theme.get("logo"):
        lines.append(f"logo = {toml_string(theme['logo'])}")
    lines.append('features = ["navigation.top", "toc.follow"]')

    primary = primary_color(theme)
    lines.extend(
        [
            "",
            "[[project.theme.palette]]",
            'scheme = "default"',
            f"primary = {toml_string(primary)}",
            'toggle.icon = "lucide/sun"',
            'toggle.name = "Canvia al mode fosc"',
            "",
            "[[project.theme.palette]]",
            'scheme = "slate"',
            f"primary = {toml_string(primary)}",
            'toggle.icon = "lucide/moon"',
            'toggle.name = "Canvia al mode clar"',
        ]
    )

    for name, config in markdown_extension_sections(mkdocs_config.get("markdown_extensions")):
        lines.extend(["", f"[project.markdown_extensions.{name}]"])
        if not isinstance(config, dict):
            raise TypeError(f"La configuració de {name} ha de ser un mapa.")
        lines.extend(f"{key} = {toml_value(value)}" for key, value in config.items())

    lines.extend(["", "[pccf.tables]", f"ods_path = {toml_string(ods_path)}"])
    if xslt_path:
        lines.append(f"xslt_path = {toml_string(xslt_path)}")
    return "\n".join(lines) + "\n"


def generate_config(project_dir, input_name="mkdocs.yml", output_name="zensical.toml", force=False):
    project_dir = Path(project_dir).resolve()
    input_path = project_dir / input_name
    output_path = project_dir / output_name
    if not input_path.is_file():
        raise FileNotFoundError(f"No s'ha trobat {input_path}")
    if output_path.exists() and not force:
        raise FileExistsError(f"{output_path} ja existeix. Utilitza --force per reemplaçar-lo.")

    config = load_mkdocs_yaml(input_path)
    rendered = render_zensical_config(config)
    output_path.write_text(rendered, encoding="utf-8")
    print(f"Configuració Zensical generada: {output_path}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Genera un zensical.toml a partir de la configuració MkDocs existent."
    )
    parser.add_argument("--project-dir", default=os.getcwd(), help="Directori del projecte.")
    parser.add_argument("--input", default="mkdocs.yml", help="Fitxer YAML d'entrada.")
    parser.add_argument("--output", default="zensical.toml", help="Fitxer TOML d'eixida.")
    parser.add_argument("--force", action="store_true", help="Reemplaça el TOML si ja existeix.")
    return parser.parse_args()


def main():
    args = parse_args()
    generate_config(args.project_dir, args.input, args.output, args.force)


if __name__ == "__main__":
    main()
