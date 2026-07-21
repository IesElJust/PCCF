#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="python3"
ZENSICAL_BIN="zensical"

if [ -x "./.venv/bin/python" ]; then
  PYTHON_BIN="./.venv/bin/python"
fi

if [ -x "./.venv/bin/zensical" ]; then
  ZENSICAL_BIN="./.venv/bin/zensical"
fi

"$PYTHON_BIN" ./tools/sync_ods_tables_site.py . ./DAW_DAW.ods ./ods2html.xslt ./ods-tools
"$ZENSICAL_BIN" build
