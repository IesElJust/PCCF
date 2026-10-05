# Plantilla de Programació Didàctica IABD

Esta carpeta és una plantilla reusable per a crear les programacions dels mòduls del curs d'especialització en `Intel·ligència Artificial i Big Data`.

## Objectiu

Disposar d'un patró únic de programació per a:

- `5071` `MIA`
- `5072` `SAA`
- `5073` `PIA`
- `5074` `SBD`
- `5075` `BDA`

La infraestructura és comuna, però cada mòdul haurà de tindre el seu propi `.ods` i el seu propi contingut curricular.

## Fitxers d'edició

- `docs/`: contingut principal de la programació.
- `PD_SBD.ods`: patró base de les taules sincronitzades.
- `zensical.toml`: configuració del site i ordre de navegació.

## Convenció

- Esta plantilla està pensada per ser copiada a una carpeta específica de mòdul.
- Després de copiar-la, cal revisar conjuntament `docs/`, `zensical.toml`, `tools/sync_ods_tables_site.py`, `rebuild.sh`, `export_pdf.sh` i el nom del `.ods`.
- Els textos contenen placeholders del tipus `Sistemes de Big Data`, `5074` o `SBD` que s'han de substituir en la còpia final.

## Fulls ODS esperats

Els fulls sincronitzats pel patró actual són:

- `contribucio_ra_cp`
- `ra_ca`
- `continguts`
- `sequenciacio_up_ra`
- `sequenciacio_up_continguts`
- `temporalitzacio`
- `avaluacio`

Es recomana, a més, mantindre fulls interns de treball no publicats:

- `metadades_modul`
- `mapa_ra_oficial_vs_funcional`
- `projectes_i_evidencies`

## Marcadors ODS

- Els apartats sincronitzats des de l'ODS han de contindre els marcadors `<!-- ODS:...:start -->` i `<!-- ODS:...:end -->` esperats per `tools/sync_ods_tables_site.py`.
- En esta plantilla, els fitxers afectats són `3.contribucio_ra.md`, `4.RAs_CAs_Continguts.md`, `5.esquema_general_up.md` i `10.Avaluacio.md`.
- Si s'afigen nous blocs ODS, cal ampliar `SYNC_TARGETS` de manera coherent.

## Scripts d'ús habitual

- `./rebuild.sh`: sincronitza les taules des de l'ODS i reconstruix el site.
- `./export_pdf.sh`: genera el PDF final.

## Entorn virtual

1. Crear l'entorn: `python3 -m venv .venv`
2. Instal.lar dependències: `./.venv/bin/pip install -r requirements.txt`
3. Els scripts usaran `./.venv/` automàticament si existix.

## Estructura de suport

- `tools/export_site_pdf.py`: exportació de la programació a PDF.
- `tools/sync_ods_tables_site.py`: sincronització ODS -> Markdown.
- `ods-tools/`: plugin local necessari per a la transformació de taules.
- `pdf-templates/`: plantilla HTML i CSS del PDF.

## Flux recomanat

1. Copiar esta plantilla a la carpeta del mòdul.
2. Verificar el nom de l'ODS específic del mòdul: `PD_SBD.ods`.
3. Substituir placeholders i adaptar `docs/`.
4. Omplir les taules oficials i de suport en l'ODS.
5. Executar `./rebuild.sh`.
6. Revisar `site/`.
7. Executar `./export_pdf.sh`.
