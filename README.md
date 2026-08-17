# PCCF. Projectes Curriculars dels Cicles Formatius

Aquest repositori conté les versions en desenvolupament dels Projectes Curriculars dels Cicles Formatius de la família professional d'Informàtica i Comunicacions de l'IES Jaume II El Just.

Els fitxers font es troben en format Markdown, com a projectes amb MkDocs, i en un full de càlcul amb les taules. Permeten la seua exportació a PDF a través de Pandoc i WeasyPrint, fent ús d'una adaptació de la plantilla [craigbass76
pandoc-css-weasyprint-template](https://github.com/craigbass76/pandoc-css-weasyprint-template).

Els diferents apartats del document són els indicats a la [Guía pràctica per al Docent del Projecte Curricular del Cicle Formatiu](https://ceice.gva.es/documents/388109149/390831792/PCCF_Guia_Practica_Docent_VAL.pdf) de la GVA.

>
> **Contingut per al curs 2025-26**
>
> El contingut del curs 2025-26 es troba guardat a la release [Documentació curs 2025-26](https://github.com/IesElJust/PCCF/releases/tag/curs-2025-2026)
>


>
> ***Contingut adaptat al curs 2026-27***
>
> La documentació actual es correspon al curs 2026-27, i ha estat adaptat automàticament introduint les directrius establertes a la [Resolució de 16 de juliol de 2026, de la Secretaria Autonòmica d’Educació, per la qual es dicten instruccions sobre ordenació acadèmica i d’organització dels centres que impartisquen els graus D i E de Formació Professional durant el curs 2026-2027 a la Comunitat Valenciana](https://dogv.gva.es/datos/2026/07/20/pdf/2026_24495_va.pdf)
>
> Les modificacions introduides i les decisions que queden pendents a prendre per part del departament es troben al document [adaptacio_curs_2026-27.md](adaptacio_curs_2026-27.md)
>

## Continguts de cada carpeta PCCF

* **Carpeta `docs`**: Conté els diferents fitxers font en format Markdown, i la carpeta `styles` amb els estils.
* **Fitxer `mkdocs.yml`**: Fitxer de configuració de MkDocs, on definim bàsicament el tema, els plugins i l'estructura del document.
* **Fitxer `PCCF_DAM.ods`**: Conté les taules que s'han d'incorporar al PCCF: Percentatges de les competències al títol, contribució de cada mòdul a les competències professionals i a les personals, i la taula d'organització del mòdul.
* **Carpeta `my_plugins`**: Conté una còpia local del plugin personalitzat `add_tables`, amb el qual, cada vegada que servim o generem el lloc web, s'incorpora el contingut de les taules dels ODS als documents originals.
* **Fitxer `ods2html.xslt`**: Conté el fitxer XSLT per fer la transformació de l'XML amb el contingut del fitxer ODS a HTML. Es conserva per compatibilitat amb el flux anterior.
* **Script `genera_pdf.py`**: Script local en Python que genera el PDF a partir de tota la documentació, fent ús de la plantilla *pandoc-css-weasyprint-template*. Es conserva per compatibilitat, tot i que actualment també hi ha una eina centralitzada.
* **Carpeta `templates`**: Conté les plantilles, la configuració, les tipografies i els estils que necessita WeasyPrint per generar el PDF. El fitxer `templates/front-matter.md` continua sent específic de cada projecte.

## Eines centralitzades

El repositori inclou ara la carpeta `pccf_tools`, que centralitza els recursos compartits per generar PDFs:

* El plugin MkDocs `add_tables`.
* El transformador de taules ODS a HTML.
* La plantilla HTML de Pandoc.
* El CSS, imatges i tipografies compartides per WeasyPrint.
* La comanda `pccf-genera-pdf`.
* La comanda `pccf-zensical-build`, que genera llocs Zensical amb les taules dels ODS.

Això permet aplicar canvis al generador, als estils o al plugin en un únic lloc, sense haver d'actualitzar manualment totes les carpetes PCCF o Programacions. Les còpies locals dels scripts i recursos es mantenen de moment per compatibilitat.

## Requisits

Per tal de treballar amb MkDocs i generar PDFs, caldrà generar un entorn virtual Python, activar-lo i instal·lar les llibreries necessàries.

### Instal·lació recomanada

La forma recomanada és utilitzar l'script de preparació de l'entorn:

```bash
./setup_entorn.sh
```

Aquest script:

* Crea o actualitza l'entorn virtual `venv` a l'arrel del repositori.
* Instal·la les dependències definides a `requirements.txt`.
* Instal·la `pccf_tools` en mode editable.
* Comprova que MkDocs, Material for MkDocs, WeasyPrint i el plugin centralitzat funcionen.
* Avisa si no troba el binari `pandoc`.

Una vegada instal·lat, activem l'entorn amb:

```bash
source venv/bin/activate
```

Per desactivar l'entorn virtual:

```bash
deactivate
```

### Instal·lació manual

1. Creem un nou entorn virtual a l'arrel del projecte

```bash
python3 -m venv venv
```

Això ens generarà una carpeta `venv` al directori arrel, la qual no es puja al repositori, ja que és ignorada pel `.gitignore`.

2. Activem l'entorn virtual amb:

```bash
. venv/bin/activate
```

3. Dins l'entorn instal·lem les dependències:

```bash
pip install -r requirements.txt
```

4. Instal·lem les eines centralitzades:

```bash
pip install --no-build-isolation -e pccf_tools
```

5. **Instal·lació de Pandoc**. Per a la conversió a HTML/PDF fem ús de Pandoc, pel que aquest ha d'estar instal·lat al sistema:

```bash
sudo apt install pandoc
```

Amb això ja podem accedir a la carpeta de cada projecte i generar el lloc o el PDF corresponent.

## Visualització en HTML

Per tal de servir el lloc en local, ho farem amb:

```bash
mkdocs serve
```

Generalment, el tindrem disponible en l'adreça: http://127.0.0.1:8000.

Per altra banda, si volem generar el lloc per publicar-lo, farem:

```bash
mkdocs build
```

Que ens generarà la carpeta `site` amb el lloc en HTML.

### Visualització amb Zensical

Els projectes que disposen d'un fitxer `zensical.toml` es poden generar amb la
comanda centralitzada següent, executada des de l'arrel del repositori:

```bash
venv/bin/pccf-zensical-build --project-dir PCCF_DAM --strict
```

Per a la programació de PMDM:

```bash
venv/bin/pccf-zensical-build --project-dir Programacions/DAM/2n/PMDM --strict
```

La comanda utilitza la secció `[pccf.tables]` del `zensical.toml` per localitzar
l'ODS i l'XSLT, i transforma una còpia temporal dels fitxers Markdown abans
d'invocar Zensical. Per tant, no necessita el `mkdocs.yml` ni modifica els
documents font. El lloc resultant es publica en `site-zensical/`.

Si Zensical està actiu en el `PATH`, s'utilitza directament. En cas contrari,
la comanda també busca el binari en `~/.local/zensicalenv/bin/zensical`. Es pot
indicar una altra instal·lació explícitament amb `--zensical /ruta/al/binari`.

Zensical s'instal·la dins del mateix `venv` amb `./setup_entorn.sh`; no cal
activar ni mantindre un segon entorn. Per generar un `zensical.toml` inicial a
partir del `mkdocs.yml` d'un projecte:

```bash
venv/bin/pccf-zensical-config --project-dir PCCF_DAM
```

La comanda conserva el nom, la navegació, els estils, el logotip, les extensions
Markdown i la configuració de les taules. Afig una configuració Zensical pròpia
amb selector de mode clar i fosc. Si el TOML ja existeix, cal confirmar-ne la
substitució amb `--force`.


## Generació del PDF

### Opció recomanada: generador centralitzat

Amb l'entorn virtual activat, podem generar el PDF des de qualsevol projecte que continga un `mkdocs.yml`:

```bash
cd Programacions/SMX/2n/SOX
pccf-genera-pdf SOX.pdf
```

També es pot invocar des de l'arrel del repositori indicant el directori del projecte:

```bash
venv/bin/pccf-genera-pdf SOX.pdf --project-dir Programacions/SMX/2n/SOX
```

Per conservar els fitxers intermedis `generated_content.md` i `generated_content.html`:

```bash
pccf-genera-pdf SOX.pdf --keep-html
```

El generador centralitzat utilitza:

* El `mkdocs.yml` del projecte.
* El `nav` del `mkdocs.yml` per saber quins fitxers Markdown concatenar.
* L'ODS indicat en `plugins.add_tables.ods_path`.
* El `templates/front-matter.md` local del projecte, si existeix.
* Els recursos compartits de `pccf_tools` per a la plantilla, CSS, imatges i tipografies.

### Opció compatible: script local `genera_pdf.py`

Les carpetes PCCF i Programacions encara conserven el seu script local `genera_pdf.py`. Per tant, el flux anterior continua sent vàlid.

El procés per a la generació consisteix en:

* **Pas 1**. Concatena un fitxer de capçalera (`templates/front-matter.md`) i tots els fitxers font Markdown, prèviament processats per incorporar les taules del fitxer ODS.
* **Pas 2**. Converteix amb Pandoc el Markdown generat a HTML.
* **Pas 3**. Aplica WeasyPrint per convertir l'HTML a PDF.

Durant el procés es generen fitxers temporals amb el Markdown i l'HTML intermedi, que són esborrats en finalitzar la conversió.

L'ús de l'script local pot ser de diverses formes:


```bash
python3 genera_pdf.py
```

* Genera el PDF amb el contingut del projecte, amb el nom `output.pdf`.


```bash
python3 genera_pdf.py nom.pdf
```

* Genera el PDF amb el contingut del projecte, amb el nom indicat `nom.pdf`.

```bash
python3 genera_pdf.py eixida.pdf --keep-html
```

```bash
python3 genera_pdf.py --keep-html
```

Amb l'opció `--keep-html` indiquem que no volem que esborre el Markdown i l'HTML intermedi. Pot ser útil per a tasques de depuració d'errors en la generació.

## Configuració de cada PCCF

Per tal de generar cada PCCF caldrà realitzar alguns ajustos, tant al fitxer de configuració com a les plantilles.

### Modificació de l'mkdocs.yml

Al fitxer `mkdocs.yml` haurem d'ajustar la configuració del plugin personalitzat, concretament, al plugin `add_tables` l'opció `ods_path`:

```yaml
plugins:
  - search
  - add_tables:
      ods_path: 'PCCF_DAM.ods'
      xslt_path: 'ods2html.xslt'
```

Com veiem, aci es fa referència al fitxer `PCCF_DAM.ods`. Per als altres cicles caldrà tindre un fitxer `PCCF_Cicle.ods` (**Important: amb la mateixa estructura de pestanyes que aquest**), amb el contingut de cada cicle.

Per tal d'incorporar una taula al Markdown des de l'ODS, el que haurem de fer és afegir la marca `{nom_del_full}` dins el Markdown, per afegir el contingut del full. Per exemple, en `docs/3.adequacio_competencies.md`, afegim la marca:

```
{taula_percentatges_competencies}
```

Això busca el full `taula_percentatges_competencies` al full de càlcul `PCCF_DAM.ods` i l'incorpora en HTML on es troba la marca.

### Modificacions de la plantilla 

Quan generem el PDF d'un altre cicle, cal ajustar alguns paràmetres. Concretament, al fitxer `templates/front-matter.md` podrem indicar:

* El títol i subtítol del document a la portada,
* Capçalera i peus,
* ...

**Nota**: Tot i que veureu aci les imatges de fons, s'especifiquen al CSS, pel que aquests camps són ignorats.


```yaml
---
title: Projecte Curricular del Cicle Formatiu \newline Desenvolupament d'Aplicacions Multiplataforma
titlepage: true
subtitle: PCCF DAM
...
titlepage-background: "templates/img/portada.png"
page-background: "templates/img/fondo.png"
header-left: Departament d'Informàtica. Curs 2025-2026
footer-left: IES Jaume II el Just. PCCF
---
```
