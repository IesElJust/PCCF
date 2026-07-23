#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="python3"

if [ -x "./.venv/bin/python" ] && ./.venv/bin/python --version >/dev/null 2>&1; then
  PYTHON_BIN="./.venv/bin/python"
fi

has_output_pdf=false
for arg in "$@"; do
  if [ "${arg#-}" = "$arg" ]; then
    has_output_pdf=true
    break
  fi
done

if [ "$has_output_pdf" = false ]; then
  set -- programacio-didactica_PPS.pdf "$@"
fi

"$PYTHON_BIN" ./tools/export_site_pdf.py . "$@"
