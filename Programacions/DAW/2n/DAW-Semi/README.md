# Programacio didactica DAW

## Fitxers d'edicio

- `docs/`: contingut principal de la programacio.
- `DAW_DAW.ods`: font de les taules de `04`, `05` i `10`.
- `zensical.toml`: configuracio del site i ordre de navegacio.

## Scripts d'us habitual

- `./rebuild.sh`: sincronitza les taules des de l'ODS i reconstruix el site.
- `./export_pdf.sh`: genera el PDF final.

## Entorn virtual

1. Crear l'entorn: `python3 -m venv .venv`
2. Instal lar dependències: `./.venv/bin/pip install -r requirements.txt`
3. Els scripts `rebuild.sh` i `export_pdf.sh` usaran `./.venv/` automàticament si existix.

## Estructura de suport

- `tools/export_site_pdf.py`: exportacio de la programacio a PDF.
- `tools/sync_ods_tables_site.py`: sincronitzacio ODS -> Markdown.
- `ods-tools/`: plugin local necessari per a la transformacio de taules.
- `pdf-templates/`: plantilla HTML i CSS del PDF.

## Eixides generades

- `site/`: web generada per Zensical.
- `programacio-didactica.pdf`: ultima exportacio a PDF.

## Flux recomanat

1. Editar `docs/` i, si cal, `DAW_DAW.ods`.
2. Executar `./rebuild.sh`.
3. Revisar `site/`.
4. Executar `./export_pdf.sh`.
