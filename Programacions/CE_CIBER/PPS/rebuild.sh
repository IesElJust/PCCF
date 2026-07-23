#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="python3"
ZENSICAL_BIN="zensical"

if [ -x "./.venv/bin/python" ] && ./.venv/bin/python --version >/dev/null 2>&1; then
  PYTHON_BIN="./.venv/bin/python"
fi

if [ -x "./.venv/bin/zensical" ] && ./.venv/bin/zensical --version >/dev/null 2>&1; then
  ZENSICAL_BIN="./.venv/bin/zensical"
fi

"$PYTHON_BIN" ./tools/sync_ods_tables_site.py . ./PD_PPS.ods ./ods2html.xslt ./ods-tools
"$ZENSICAL_BIN" build
