#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="python3"
if [ -x "./.venv/bin/python" ] && ./.venv/bin/python --version >/dev/null 2>&1; then
  PYTHON_BIN="./.venv/bin/python"
fi

"$PYTHON_BIN" ./tools/sync_ods_tables_site.py . ./SASP_DAW.ods ./ods2html.xslt ./ods-tools
"$PYTHON_BIN" -m zensical build
