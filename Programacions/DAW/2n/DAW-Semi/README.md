# Programació didàctica DAW

## Fitxers d'edició

- `docs/`: contingut principal de la programació.
- `DAW_DAW.ods`: font de les taules de `04`, `05` i `10`.
- `zensical.toml`: configuració del site i ordre de navegació.

## Convenció de noms

- Este projecte és la referència canònica de la família per als noms de `docs/`.
- Si es duplica a un altre mòdul, convé mantindre esta nomenclatura o actualitzar de manera coordinada `docs/`, `zensical.toml`, `tools/sync_ods_tables_site.py`, `rebuild.sh` i `README.md`.

## Scripts d'ús habitual

- `./rebuild.sh`: sincronitza les taules des de l'ODS i reconstruix el site.
- `./export_pdf.sh`: genera el PDF final.

## Marcadors ODS

- Els apartats sincronitzats des de l'ODS han de contindre els marcadors `<!-- ODS:...:start -->` i `<!-- ODS:...:end -->` esperats per `tools/sync_ods_tables_site.py`.
- En este projecte, els fitxers afectats habitualment són `2-relacio-uc.md`, `3.contribucio_ra.md`, `4.RAs_CAs_Continguts.md`, `5.esquema_general_up.md` i `10.Avaluacio.md`.
- Si falta algun marcador, `./rebuild.sh` fallarà abans de generar el site.

## Entorn virtual

1. Crear l'entorn: `python3 -m venv .venv`
2. Instal·lar dependències: `./.venv/bin/pip install -r requirements.txt`
3. Els scripts `rebuild.sh` i `export_pdf.sh` usaran `./.venv/` automàticament si existix.

## Estructura de suport

- `tools/export_site_pdf.py`: exportació de la programació a PDF.
- `tools/sync_ods_tables_site.py`: sincronització ODS -> Markdown.
- `ods-tools/`: plugin local necessari per a la transformació de taules.
- `pdf-templates/`: plantilla HTML i CSS del PDF.

## Eixides generades

- `site/`: web generada per Zensical.
- `programacio-didactica.pdf`: última exportació a PDF.

## Flux recomanat

1. Editar `docs/` i, si cal, `DAW_DAW.ods`.
2. Si hi ha canvis en apartats sincronitzats, revisar que els marcadors ODS continuen existint.
3. Executar `./rebuild.sh`.
4. Revisar `site/`.
5. Executar `./export_pdf.sh`.
