#!/usr/bin/env bash

# Punt d'entrada conservat per compatibilitat.
# La generació moderna crea els llocs Zensical, els PDF i la carpeta ordenada.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "$ROOT_DIR/genera_carpeta_pdfs.sh" "$@"
