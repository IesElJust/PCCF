#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "Creant entorn virtual en $ROOT_DIR/venv"
python3 -m venv venv

echo "Actualitzant pip"
venv/bin/python -m pip install --upgrade pip

echo "Instal·lant dependències"
venv/bin/python -m pip install -r requirements.txt

echo "Eliminant instal·lacions antigues del plugin local, si existeixen"
venv/bin/python -m pip uninstall -y mkdocs-radd-tables >/dev/null 2>&1 || true

echo "Instal·lant pccf_tools en mode editable"
venv/bin/python -m pip install --no-build-isolation -e pccf_tools

echo "Comprovant eines"
venv/bin/python -c "import mkdocs, material, odf, yaml, weasyprint, pccf_pdf; print('Imports OK')"
venv/bin/mkdocs --version
venv/bin/pccf-genera-pdf --help >/dev/null
venv/bin/pccf-zensical-build --help >/dev/null
venv/bin/pccf-zensical-config --help >/dev/null
venv/bin/zensical --version

if command -v pandoc >/dev/null 2>&1; then
  echo "Pandoc OK: $(pandoc --version | head -n 1)"
else
  echo "AVIS: No s'ha trobat pandoc. MkDocs funciona, però pccf-genera-pdf necessita el binari pandoc."
fi

if [ -f "Programacions/SMX/2n/SOX/mkdocs.yml" ]; then
  echo "Provant mkdocs build amb SOX"
  venv/bin/mkdocs build --config-file Programacions/SMX/2n/SOX/mkdocs.yml --site-dir /tmp/mkdocs-sox-site >/dev/null
fi

echo "Entorn preparat. Activa'l amb: source venv/bin/activate"
