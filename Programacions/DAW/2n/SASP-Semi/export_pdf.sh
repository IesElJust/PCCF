#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="python3"

if [ -x "./.venv/bin/python" ]; then
  PYTHON_BIN="./.venv/bin/python"
fi

"$PYTHON_BIN" ./tools/export_site_pdf.py . "$@"
