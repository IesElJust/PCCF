#!/usr/bin/env bash

# Genera tots els llocs i PDF Zensical i prepara una còpia ordenada dels PDF.
#
# Eixides:
#   zensical_full_doc/           lloc complet per a GitHub Pages
#   PDFs/generats/PCCF/          PDF dels projectes curriculars
#   PDFs/generats/Programacions/ PDF de les programacions didàctiques
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILDER="$ROOT_DIR/venv/bin/pccf-zensical-full-build"
FULL_OUTPUT="$ROOT_DIR/zensical_full_doc"
PDF_OUTPUT="$ROOT_DIR/PDFs/generats"

if [[ ! -x "$BUILDER" ]]; then
    echo "No s'ha trobat $BUILDER." >&2
    echo "Executa primer ./setup_entorn.sh." >&2
    exit 1
fi

echo "Generant tots els llocs Zensical i els PDF..."
"$BUILDER" --root-dir "$ROOT_DIR" --output-dir "$FULL_OUTPUT" --strict "$@"

STAGING_DIR="$(mktemp -d "$ROOT_DIR/PDFs/.generats.tmp.XXXXXX")"
BACKUP_DIR="$ROOT_DIR/PDFs/.generats.backup"
trap 'rm -rf "$STAGING_DIR"' EXIT

mkdir -p "$STAGING_DIR/PCCF" "$STAGING_DIR/Programacions"

while IFS= read -r -d '' pdf; do
    relative="${pdf#"$FULL_OUTPUT/PCCF/"}"
    destination="$STAGING_DIR/PCCF/$relative"
    mkdir -p "$(dirname "$destination")"
    cp "$pdf" "$destination"
done < <(find "$FULL_OUTPUT/PCCF" -type f -name '*.pdf' -print0 | sort -z)

while IFS= read -r -d '' pdf; do
    relative="${pdf#"$FULL_OUTPUT/Moduls/"}"
    destination="$STAGING_DIR/Programacions/$relative"
    mkdir -p "$(dirname "$destination")"
    cp "$pdf" "$destination"
done < <(find "$FULL_OUTPUT/Moduls" -type f -name '*.pdf' -print0 | sort -z)

if [[ -e "$BACKUP_DIR" ]]; then
    rm -rf "$BACKUP_DIR"
fi
if [[ -e "$PDF_OUTPUT" ]]; then
    mv "$PDF_OUTPUT" "$BACKUP_DIR"
fi
if mv "$STAGING_DIR" "$PDF_OUTPUT"; then
    rm -rf "$BACKUP_DIR"
else
    [[ ! -e "$PDF_OUTPUT" && -e "$BACKUP_DIR" ]] && mv "$BACKUP_DIR" "$PDF_OUTPUT"
    exit 1
fi
trap - EXIT

PCCF_COUNT="$(find "$PDF_OUTPUT/PCCF" -type f -name '*.pdf' | wc -l)"
PROGRAM_COUNT="$(find "$PDF_OUTPUT/Programacions" -type f -name '*.pdf' | wc -l)"

echo "PDF ordenats en $PDF_OUTPUT"
echo "Projectes curriculars: $PCCF_COUNT"
echo "Programacions didàctiques: $PROGRAM_COUNT"
