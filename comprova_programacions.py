#!/usr/bin/env python3
"""Comprova que les programacions de moduls existeixen i son MkDocs."""

from __future__ import annotations

import argparse
import sys
import unicodedata
from pathlib import Path
from typing import Any


ALIASES = {
    "DAW": ["Desplegament"],
    "DIG": ["Digitalitzacio", "DIGITALITZACIO", "DIGITALITZACIÓ"],
    "GBD": ["SBD"],
    "LMSGI": ["LMI"],
    "PRG": ["PRO"],
    "SOST": ["Sostenibilitat", "SOSTENIBILITAT"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Llig moduls.yaml i comprova que cada modul tinga una carpeta "
            "amb mkdocs.yml o mkdocs.yaml dins de Programacions."
        )
    )
    parser.add_argument(
        "--yaml",
        default="moduls.yaml",
        help="Fitxer YAML amb els moduls (per defecte: moduls.yaml).",
    )
    parser.add_argument(
        "--programacions",
        default="Programacions",
        help="Carpeta arrel de les programacions (per defecte: Programacions).",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Mostra nomes errors i avisos.",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except ImportError:
        return load_simple_moduls_yaml(path)

    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    if not isinstance(data, dict):
        raise ValueError(f"{path} no conte un diccionari YAML a l'arrel")
    return data


def load_simple_moduls_yaml(path: Path) -> dict[str, Any]:
    """Parser minim per a l'estructura actual de moduls.yaml.

    Accepta:
      CICLE:
          - 1r:
              - MODUL
          - 2n:
              - MODUL
          - PIM
    """
    data: dict[str, list[Any]] = {}
    current_cycle: str | None = None
    current_course: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        stripped = raw_line.strip()
        indent = len(raw_line) - len(raw_line.lstrip(" "))

        if indent == 0 and stripped.endswith(":"):
            current_cycle = stripped[:-1].strip()
            current_course = None
            data[current_cycle] = []
            continue

        if current_cycle is None or not stripped.startswith("- "):
            continue

        item = stripped[2:].strip()
        if item.endswith(":"):
            current_course = item[:-1].strip()
            course_entry: dict[str, list[str]] = {current_course: []}
            data[current_cycle].append(course_entry)
            continue

        if current_course and indent > 4:
            last_entry = data[current_cycle][-1]
            if isinstance(last_entry, dict):
                last_entry[current_course].append(item)
            continue

        current_course = None
        data[current_cycle].append(item)

    return data


def iter_expected_modules(data: dict[str, Any]) -> list[tuple[str, str | None, str]]:
    expected: list[tuple[str, str | None, str]] = []

    for cycle, entries in data.items():
        if not isinstance(entries, list):
            continue

        for entry in entries:
            if isinstance(entry, dict):
                for course, modules in entry.items():
                    if not isinstance(modules, list):
                        continue
                    for module in modules:
                        expected.append((str(cycle), str(course), str(module)))
            else:
                expected.append((str(cycle), None, str(entry)))

    return expected


def mkdocs_config(path: Path) -> Path | None:
    for filename in ("mkdocs.yml", "mkdocs.yaml"):
        candidate = path / filename
        if candidate.is_file():
            return candidate
    return None


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return "".join(ch for ch in value.casefold() if ch.isalnum())


def possible_matches(parent: Path, module: str) -> list[Path]:
    if not parent.is_dir():
        return []

    wanted_names = [module, *ALIASES.get(module.upper(), [])]
    wanted_norms = {normalize_name(name) for name in wanted_names}
    matches: list[Path] = []
    for child in sorted(parent.iterdir()):
        if not child.is_dir():
            continue
        child_norm = normalize_name(child.name)
        if any(wanted == child_norm or wanted in child_norm for wanted in wanted_norms):
            matches.append(child)
    return matches


def expected_path(programacions: Path, cycle: str, course: str | None, module: str) -> Path:
    if course is None:
        return programacions / cycle / module
    return programacions / cycle / course / module


def group_parent(programacions: Path, cycle: str, course: str | None) -> Path:
    if course is None:
        return programacions / cycle
    return programacions / cycle / course


def group_label(course: str | None) -> str:
    if course is None:
        return "Sense curs"
    return course


def print_module_list(title: str, values: list[str]) -> None:
    if values:
        print(f"    {title}: {', '.join(values)}")
    else:
        print(f"    {title}: -")


def main() -> int:
    args = parse_args()
    yaml_path = Path(args.yaml)
    programacions = Path(args.programacions)

    if not yaml_path.is_file():
        print(f"ERROR: no existeix el fitxer {yaml_path}", file=sys.stderr)
        return 2

    if not programacions.is_dir():
        print(f"ERROR: no existeix la carpeta {programacions}", file=sys.stderr)
        return 2

    try:
        data = load_yaml(yaml_path)
    except Exception as exc:
        print(f"ERROR: no s'ha pogut llegir {yaml_path}: {exc}", file=sys.stderr)
        return 2

    expected = iter_expected_modules(data)
    expected_by_group: dict[tuple[str, str | None], set[str]] = {}
    courses_by_cycle: dict[str, set[str]] = {}
    report: dict[tuple[str, str | None], dict[str, list[str]]] = {}
    missing: list[Path] = []
    not_mkdocs: list[Path] = []
    ok = 0

    for cycle, course, module in expected:
        path = expected_path(programacions, cycle, course, module)
        key = (cycle, course)
        expected_by_group.setdefault(key, set()).add(module)
        if course is not None:
            courses_by_cycle.setdefault(cycle, set()).add(course)
        group = report.setdefault(
            key,
            {"ok": [], "missing": [], "not_mkdocs": [], "suggestions": []},
        )

        if not path.exists():
            missing.append(path)
            group["missing"].append(module)
            parent = path.parent
            suggestions = possible_matches(parent, module)
            if suggestions:
                joined = ", ".join(str(item) for item in suggestions)
                group["suggestions"].append(f"{module}: {joined}")
            continue

        if not path.is_dir():
            not_mkdocs.append(path)
            group["not_mkdocs"].append(f"{module} (no es carpeta: {path})")
            continue

        config = mkdocs_config(path)
        if config is None:
            not_mkdocs.append(path)
            group["not_mkdocs"].append(f"{module} ({path})")
            continue

        ok += 1
        group["ok"].append(f"{module} -> {config}" if not args.quiet else module)

    extras_by_group: dict[tuple[str, str | None], list[str]] = {}
    for key, expected_modules in expected_by_group.items():
        cycle, course = key
        parent = group_parent(programacions, cycle, course)
        if not parent.is_dir():
            extras_by_group[key] = []
            continue
        extras_by_group[key] = [
            child.name
            for child in sorted(parent.iterdir())
            if child.is_dir() and child.name not in expected_modules
            and not (course is None and child.name in courses_by_cycle.get(cycle, set()))
        ]

    print("Detall per cicle i curs")
    for cycle, entries in data.items():
        if not isinstance(entries, list):
            continue

        printed_groups: set[tuple[str, str | None]] = set()
        print()
        print(cycle)
        for entry in entries:
            courses = entry.keys() if isinstance(entry, dict) else [None]
            for course in courses:
                key = (str(cycle), str(course) if course is not None else None)
                if key in printed_groups:
                    continue
                printed_groups.add(key)
                group = report.get(
                    key,
                    {"ok": [], "missing": [], "not_mkdocs": [], "suggestions": []},
                )
                print(f"  {group_label(key[1])}")
                print_module_list("Trobades", group["ok"])
                print_module_list("Falten", group["missing"])
                print_module_list("Sense MkDocs", group["not_mkdocs"])
                print_module_list("Possibles coincidencies", group["suggestions"])
                print_module_list("No definides al YAML", extras_by_group.get(key, []))

    print()
    print("Resum")
    print(f"  Programacions esperades: {len(expected)}")
    print(f"  Correctes: {ok}")
    print(f"  Carpetes inexistents: {len(missing)}")
    print(f"  Carpetes sense projecte MkDocs: {len(not_mkdocs)}")

    return 1 if missing or not_mkdocs else 0


if __name__ == "__main__":
    raise SystemExit(main())
