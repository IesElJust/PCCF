---
title: "Proposta curricular de cicle formatiu  \\newline FPB Informàtica d'Oficina"
subtitle: "FPB Informàtica i Comunicacions \\newline \\today"
author: "JB Talens"

# Eisvogel
titlepage: true
titlepage-rule-height: 0
titlepage-text-color: "F08A2A"
titlepage-background: "docs/img/portada-aula.png"
page-background: "docs/img/fondo.png"

geometry: "left=2cm,right=2cm,top=3cm,bottom=3cm"
toc: true
toc-depth: 3
toc-own-page: true
toc-title: "Índex"
numbersections: true
lang: ca
listings: true

# Logos i peu de pàgina
header-left: "\\includegraphics[scale=0.5]{docs/img/logos/logoJust.png} \\textcolor{morat}{| Programació d'Aula IMX}"
header-right: "\\includegraphics[scale=0.5]{docs/img/logos/GvaNext.png}"
footer-left: "\\includegraphics[scale=0.1]{docs/img/logos/FonsVal.png}"
footer-center: "\\thepage/\\pageref{LastPage}"
footer-right: "\\includegraphics[scale=0.3]{docs/img/logos/miniPla.png}"

# Bibliografia
bibliography: bibliografia.bib
csl: apa.csl
biblatexoptions: [language=spanish,backend=biber]

header-includes:
  - \input{latex-macros.tex}
---


---
title: "Proposta curricular de cicle formatiu  \\newline FPB Informàtica d'Oficina"
subtitle: "FPB Informàtica i Comunicacions \\newline \\today"
author: "JB Talens"

# Eisvogel
titlepage: true
titlepage-rule-height: 0
titlepage-text-color: "F08A2A"
titlepage-background: "docs/img/portada-aula.png"
page-background: "docs/img/fondo.png"

geometry: "left=2cm,right=2cm,top=3cm,bottom=3cm"
toc: true
toc-depth: 3
toc-own-page: true
toc-title: "Índex"
numbersections: true
lang: ca
listings: true

# Logos i peu de pàgina
header-left: "\\includegraphics[scale=0.5]{docs/img/logos/logoJust.png} \\textcolor{morat}{| Programació d'Aula IMX}"
header-right: "\\includegraphics[scale=0.5]{docs/img/logos/GvaNext.png}"
footer-left: "\\includegraphics[scale=0.1]{docs/img/logos/FonsVal.png}"
footer-center: "\\thepage/\\pageref{LastPage}"
footer-right: "\\includegraphics[scale=0.3]{docs/img/logos/miniPla.png}"

# Bibliografia
bibliography: bibliografia.bib
csl: apa.csl
biblatexoptions: [language=spanish,backend=biber]

header-includes:
  - \input{latex-macros.tex}
---


El *Decret 114/2025, de 29 de juliol del Consell, pel qual s/'establixen els currículums dels cicles formatius de grau mitjà i de grau superior de Formació Professional*, estableix que cada centre docent desenvoluparà i completarà, en el marc de la seua autonomia, els curriculums de cada cicle formatiu que impartisca mitjançant l/'elaboració de projectes curriculars (PCCF), els quals suposaran el marc de referència per a la planificació, el desenvolupament i l/'avaluació del procés d/'ensenyament i aprenentatge del cicle.

El present document, en virtut d/'aquest Decret, desenvolupa i completa el currículum per al **CFGM de Sistemes Microinformàtics i Xarxes**, i l/'adapta a l/'entorn socioeconòmic i empresarial de l/'IES Jaume II el Just, a Tavernes de la Valldigna. Les programacions didàctiques de cada mòdul professional s/'elaboraran tenint en compte aquest projecte, assegurant la coherència perdagògica i metodològica en la impartició del cicle.

# 1. Identificació del Cicle Formatiu

El primer requeriment d'un projecte curricular de cicle formatiu (PCCF) és la seua identificació clara. En aquest apartat es recullen les dades essencials que permeten reconéixer oficialment el cicle objecte de programació, així com la vinculació amb el centre educatiu i l'equip docent responsable de la seua implementació. Aquesta informació assegura la traçabilitat institucional del projecte i el seu encaix amb l'oferta educativa del centre i del sistema valencià de Formació Professional.

## Denominació oficial del títol

-   Denominació: Títol Professional Bàsic en Informàtica d'Oficina.
-   Nivell: Formació Professional Bàsica.
-   Durada: 2.000 hores (dos cursos acadèmics).
-   Família professional: Informàtica i Comunicacions.
-   Normativa estatal de referència: Reial decret 356/2014, de 16 de maig.
-   Normativa autonòmica: adaptació curricular segons normativa de la Comunitat Valenciana.
-   Referència internacional: CINE-3.5.4 (Classificació Internacional Normalitzada de l'Educació, UNESCO).
-   Marc Espanyol de Qualificacions per a l/'Educació i la Formació (MECU): Nivell 1.

## Centre educatiu

-   Nom del centre: IES Jaume II el Just.
-   Codi del centre: 46008340.
-   Localitat: Tavernes de la Valldigna (La Safor).
-   Província: València.
-   Tipus de centre: Institut públic d'Educació Secundària, Batxillerat i FP.
-   Modalitat d'ensenyament: presencial.

## Equip educatiu responsable

El projecte curricular és responsabilitat de l'equip docent del cicle, liderat pel Departament d'Informàtica i Comunicacions. Aquest equip incorpora professorat de mòduls específics i transversals, així com la figura de la tutoria i la coordinació de Formació Professional Bàsica. La direcció d'estudis de FP garanteix la integració del projecte en la programació general anual del centre.

Per al curs 2025-2026, l/'organització docent del cicle incorpora les següents assignacions específiques:

-   El Departament de Castellà assumeix la docència del mòdul transversal Comunicació i Societat, excepte els resultats d'aprenentatge vinculats a la llengua anglesa.
-   El Departament d'Anglés imparteix els resultats d'aprenentatge corresponents a la competència lingüística en llengua estrangera integrats en el mateix mòdul.
-   El Departament de Física i Química es fa càrrec de la docència del mòdul Ciències Aplicades.

Aquesta distribució respon a criteris d'especialització docent i d'adaptació curricular que garanteixen una atenció adequada a les competències bàsiques i professionals requerides


# 2. Marc normatiu per al desplegament del projecte curricular

L'elaboració d'aquest **Projecte Curricular de Cicle Formatiu (PCCF)** es fonamenta en el seu reconeixement com a instrument de **nivell curricular 2**, segons s'estableix en la guia elaborada per la Direcció General de Formació Professional. En aquest marc, el PCCF **no depén de les programacions didàctiques**, sinó que **les integra i articula** a través dels **acords pedagògics, metodològics i organitzatius** definits col·lectivament per l'equip docent. Així, esdevé el **document de referència per a la planificació i coherència global del cicle**, i orienta el desenvolupament de les **programacions d'aula dels mòduls professionals** (nivell curricular 3).

Tot i aquesta estructuració clara en dos nivells curriculars, cal destacar que, mentre que en altres etapes educatives com **Primària, ESO i Batxillerat** la normativa ha substituït el concepte de *programació didàctica* pel de *projecte curricular d'etapa o de cicle*, en l'àmbit de la Formació Professional **aquesta substitució terminològica no s'ha produït encara**. Per tant, en FP es manté l'ús del terme *programació didàctica*, tot i que el **Projecte Curricular de Cicle Formatiu (PCCF)** **assumeix i integra** tot allò corresponent al **nivell curricular 2**, segons les directrius de la Direcció General de Formació Professional.

Així, entenem que **el PCCF conté els acords i orientacions pedagògiques comunes del cicle**, que donen coherència a la pràctica docent i que **substitueixen la necessitat de programacions didàctiques individuals desvinculades**. Per tant, mentre la normativa no indique el contrari, el PCCF **integra funcionalment les programacions didàctiques**, i cada docent ha de **desenvolupar la seua pròpia programació d'aula** (nivell curricular 3) **basant-se en el marc establit pel PCCF**, coherent amb els criteris d'avaluació, els resultats d'aprenentatge i les metodologies comunes acordades per l'equip docent.

D'aquesta manera, es garanteix una coordinació acurada entre els documents, es reforça la coherència de la pràctica docent i es preserva el dret de l'alumnat a una avaluació objectiva, personalitzada i adaptada al seu progrés i circumstàncies, tal com estableix l'**Ordre 2025/13083**.

A més, aquesta normativa dona suport a la **implantació de metodologies actives**, la **flexibilitat curricular**, i l'enfocament **intermodular**, amb especial atenció a la **singularització del projecte per a cada estudiant**. Aquest plantejament reforça la funció del PCCF com a peça clau per garantir l'alineació metodològica, la contextualització i l'assoliment dels resultats d'aprenentatge (RA).

Dins aquest nou escenari, la **Resolució de 17 de juliol de 2025**, de la Secretaria Autonòmica d'Educació, dicta les **instruccions per a l'organització i funcionament dels cicles formatius de grau D i E** i estableix que el **PCCF ha d'incloure-se a la PGA** i **avaluar-se** com a part essencial de la gestió pedagògica anual. A més, aquest document ha de reflectir les directrius de centre, integrar les mesures d'atenció a la diversitat, i establir mecanismes de seguiment i millora contínua (apartat 22.1 de la resolució).

Finalment, cal tenir en compte que, malgrat la vigència de la nova **Llei orgànica 3/2022, de 31 de març**, i del desplegament del **Reial decret 659/2023**, determinats aspectes de l'ordenació de la FPB continuen regulats per normatives anteriors, com ara el **Reial decret 127/2014** o el **Reial decret 356/2014**, tal com estableixen les disposicions transitòries i el **calendari d'implantació del Reial decret 278/2023**. Aquest escenari de transició normativa implica que els centres han de gestionar una convivència ordenada entre marcs nous i vigents, cosa que reforça encara més la funció estructuradora del PCCF com a vertebrador de l'oferta formativa del cicle.

## Normativa general

-   **Llei orgànica 2/2006, de 3 de maig**, d'Educació (LOE), modificada per:
-   **Llei orgànica 8/2013, de 9 de desembre** (LOMCE)
-   **Llei orgànica 3/2020, de 29 de desembre** (LOMLOE)
-   **Llei orgànica 3/2022, de 31 de març**, d'ordenació i integració de la Formació Professional
-   **Reial decret 659/2023, de 18 de juliol**, pel qual es desplega l'ordenació del Sistema de Formació Professional
-   **Resolució de 17 de juliol de 2025**, de la Secretaria Autonòmica d'Educació, sobre instruccions per a l'FP

## Normativa específica per al títol

-   **Reial decret 356/2014, de 16 de maig**, pel qual s'estableix el títol professional bàsic en Informàtica d'Oficina
-   **Decret 185/2014, de 31 d'octubre**, pel qual s'establix el currículum del cicle a la Comunitat Valenciana

## Avaluació i qualificació

-   **Ordre 79/2010, de 27 d'agost**, sobre l'avaluació de l'alumnat dels cicles formatius a la Comunitat Valenciana
-   **Ordre 2025/13083, de 30 d'abril**, sobre el nou sistema d'avaluació en l'FP, amb efectes **retroactius** des de l'1 de setembre de 2024
-   **Reial decret 498/2024, de 21 de maig**, que actualitza els criteris d'avaluació i el sistema de qualificacions en cicles de grau bàsic

## Altres referències normatives

-   **Reial decret 217/2022**, d'ordenació de l'ESO (en allò aplicable als cicles FPB)
-   **Decret 107/2022**, d'ordenació del currículum de l'ESO a la Comunitat Valenciana
-   **Reial decret 278/2023**, sobre calendari d'implantació de la nova ordenació de l'FP
-   **Resolucions anuals d'inici de curs** de la Conselleria d'Educació
-   **Projecte educatiu del centre (PEC)** i **programació general anual (PGA)**

Aquest conjunt normatiu dona **suport i legitimitat a les decisions recollides en el PCCF**, que esdevé el document estratègic per **alinear, coordinar i millorar la pràctica docent** del cicle, afavorint l'eficàcia pedagògica i l'atenció a la diversitat dins d'un marc legal en evolució.


# 3. Adequació i adaptació de les competències professionals del títol al context socioeconòmic i cultural del centre

L'adaptació de les competències professionals del títol ha de partir d'una anàlisi del **context socioeconòmic i cultural del centre educatiu**, així com de les característiques específiques de l'alumnat. Aquesta adequació no implica modificar ni suprimir competències recollides en el perfil professional, sinó **ponderar-les i contextualitzar-les** d'acord amb les necessitats del territori i les orientacions del **Projecte d'Acció Curricular (PAC)**.

L'**IES Jaume II el Just**, situat a Tavernes de la Valldigna, es troba en una posició estratègica per donar resposta a les necessitats del **sector TIC** de les comarques de la Safor i la Ribera. El centre compta amb una àmplia trajectòria dins la **Família Professional d'Informàtica i Comunicacions**, i ofereix cicles formatius de grau bàsic, mitjà i superior, així com **cursos d'especialització en Ciberseguretat i Intel·ligència Artificial i Big Data**.

## 3.1. Anàlisi del context territorial i productiu

Segons dades de la Cambra de Comerç, el País Valencià és un dels principals pols tecnològics de l'Estat espanyol, amb més de **2.000 empreses TIC**, de les quals un 70% són **pimes**. Aquest teixit empresarial, amb escassos recursos per a formació pròpia, demanda professionals polivalents i adaptables.

Les comarques de **la Safor** i **la Ribera** han experimentat un creixement notable del sector TIC, vinculat a la digitalització de processos empresarials i a la creació d'espais d'innovació, especialment en àmbits com:

-   Digitalització del sector agroalimentari
-   Automatització i gestió empresarial
-   Suport i manteniment de sistemes i infraestructures TIC
-   Desenvolupament d'aplicacions i serveis multiplataforma

## 3.2. Marc normatiu de referència

Segons el **Reial decret 498/2024**, que actualitza els perfils professionals dels cicles de grau bàsic, les antigues /"competències professionals, personals i socials/" passen a denominar-se **competències professionals i per a l'ocupabilitat**, posant èmfasi en:

-   L'adaptació al canvi tecnològic
-   La capacitat de treball en equip
-   L'autonomia i la iniciativa professional
-   L'assoliment de tasques pròximes a l'entorn real de treball

Aquest enfocament està recollit també al **Decret 185/2014, de 31 d'octubre**, que fixa el currículum del **Títol Professional Bàsic en Informàtica d'Oficina** per a la Comunitat Valenciana, vigent fins a la plena implementació dels nous currículums previstos per la **LOFP 3/2022** i el **RD 659/2023**.

## 3.3. Adequació de les competències al perfil territorial

A partir de l'anàlisi del context i la consulta amb els agents socioeconòmics i empresarials de la zona, s'han identificat com a **competències prioritàries** per afavorir la inserció laboral i la projecció professional dels titulats les següents:

-   Manteniment de sistemes microinformàtics i xarxes locals
-   Recuperació de dades i diagnòstic de fallades
-   Instal·lació i configuració de programari bàsic i d'ofimàtica
-   Comunicació professional oral i escrita
-   Atenció al client i suport tècnic bàsic
-   Gestió de la seguretat i la protecció ambiental
-   Autonomia, responsabilitat i treball en equip

Aquestes prioritats s'han traslladat al **desenvolupament metodològic i curricular** del present PCCF, tot mantenint el marc competencial oficial però ajustant el **pes relatiu de cadascuna de les competències** segons el seu impacte formatiu i ocupacional.

## 3.4. Proposta de ponderació de competències

Per tal de garantir la coherència entre el perfil del títol i les demandes de l'entorn productiu, l'equip docent ha consensuat la següent **ponderació orientativa** de les competències professionals:

  **Codi**    **Competència professional**                                                                   **Ponderació (%)**
  ----------- ---------------------------------------------------------------------------------------------- --------------------
  a           Preparar equips i aplicacions per al tractament, impressió i arxiu de dades i textos           10 %
  b           Elaborar documents amb processadors de text i fulls de càlcul seguint protocols                10 %
  c           Acopiar materials per al muntatge i manteniment de sistemes informàtics                        5 %
  d           Realitzar operacions auxiliars de muntatge de sistemes microinformàtics                        10 %
  e           Realitzar operacions de manteniment bàsic de sistemes microinformàtics                         10 %
  f           Realitzar operacions d'emmagatzematge i transport de perifèrics i sistemes                     5 %
  g           Verificar sistemes i instal·lacions informàtiques segons procediments establerts               5 %
  h           Muntar canalitzacions i cablatge de dades amb criteris de qualitat i seguretat                 5 %
  i           Realitzar el cablejat de xarxes locals segons tècniques normalitzades                          5 %
  j           Manejar eines de l/'entorn d'usuari i dispositius d'emmagatzematge d'informació                5 %
  k           Resoldre problemes previsibles amb suport científic i tecnològic                               3 %
  l           Fomentar hàbits saludables en l'entorn personal i social                                       2 %
  m           Aplicar accions de conservació del medi ambient                                                2 %
  n           Utilitzar tecnologies per a l'autonomia i aprenentatge permanent                               3 %
  o           Comunicar-se amb claredat en diversos entorns i mitjans                                        3 %
  p           Comunicar-se en llengua estrangera en situacions habituals                                     2 %
  q           Explicar fets o fenòmens socials amb precisió lingüística                                      2 %
  r           Adaptar-se a canvis tecnològics i organitzatius en l'activitat professional                    3 %
  s           Complir tasques pròpies amb responsabilitat i eficiència                                       4 %
  t           Comunicar-se i treballar en equip respectant l'autonomia i competència dels altres             3 %
  u           Aplicar mesures de prevenció de riscos laborals i seguretat                                    3 %
  v           Complir normes de qualitat, accessibilitat i disseny universal                                 2 %
  w           Actuar amb iniciativa i responsabilitat en la tria de procediments professionals               2 %
  x           Exercir els drets i obligacions professionals amb participació en la vida social i econòmica   1 %
  **Total**                                                                                                  **100 %**

Aquesta ponderació serà tinguda en compte en la programació d'aula, en les situacions d'aprenentatge i en el disseny de projectes intermodulars, amb l'objectiu de formar titulats i titulades preparats per a **l'ocupabilitat real i el desenvolupament professional sostenible** dins del sector TIC del territori.


# 4. Contribució de cada mòdul a les competències professionals del cicle

Per a la coordinació del treball educatiu, és necessari **estudiar com cada mòdul contribueix al desenvolupament de les competències professionals** del títol. Aquesta visió integrada permet una planificació coherent i compartida entre els docents implicats, i ajuda a garantir que totes les competències requerides siguen abordades de manera progressiva i equilibrada al llarg del cicle formatiu.

Aquest enfocament també permet, en un nivell més avançat de programació, **identificar resultats d'aprenentatge (RA) clau** que, pel seu caràcter transversal o pel seu impacte professional, requerisquen una atenció especial dins de cada mòdul. Així, el procés de programació pot ajustar-se per garantir que cap competència quede desatesa i que es desenvolupen de manera efectiva aquelles que són més rellevants per a la inserció laboral i el desenvolupament personal de l'alumnat.

Per tal d'arribar a aquest nivell de concreció, es proposa estructurar una **taula de contribució competencial**, en què es relacione cada mòdul amb les competències professionals del perfil. Aquesta associació s'establix a partir de les orientacions del Reial decret que regula el títol (RD 356/2014), i pot ser revisada o ajustada per l'equip educatiu si ho considera oportú, d'acord amb les característiques del context i del grup classe.

La **competència general** del títol és la següent:

> */"Realitzar operacions auxiliars de muntatge i manteniment de sistemes microinformàtics, perifèrics i xarxes de comunicació de dades, i de tractament, reproducció i arxiu de documents, operant amb la qualitat indicada i actuant en condicions de seguretat i de protecció ambiental amb responsabilitat i iniciativa personal, i comunicant-se de forma oral i escrita en llengua castellana, i si escau, en la llengua cooficial pròpia, així com en alguna llengua estrangera./"*

## 4.1. Taula de correspondència entre mòduls i competències professionals

A continuació es presenta la relació entre els **mòduls professionals** del cicle i les **competències professionals, personals i socials** que contribueixen a desenvolupar:

  **Mòdul Professional**                                                   **Competències Professionals, Personals i Socials Desenvolupades**
  ------------------------------------------------------------------------ --------------------------------------------------------------------
  3029/. Muntatge i manteniment de sistemes i components informàtics       c), d), e), f), g), h), i), j)
  3030/. Operacions auxiliars per a la configuració i explotació           a), j)
  3016/. Instal·lació i manteniment de xarxes per a transmissió de dades   h), i)
  3031/. Ofimàtica i arxiu de documents                                    a), b), j)
  3011/. Comunicació i societat I                                          m), n), ñ), o), p)
  3012/. Comunicació i societat II                                         q), r), s), t), u), v), w)
  3009/. Ciències aplicades I                                              j), k), l), m)
  3010/. Ciències aplicades II                                             q), r), s), t), u), v), w), x)
  3033/. Formació en centres de treball (FCT)                              Totes les competències transversals i tècniques en context real

> Aquesta taula és un instrument fonamental per a la **coordinació entre docents**, la programació compartida de situacions d'aprenentatge i la detecció de possibles buits competencials en el desenvolupament del currículum.

## 4.2. Utilització didàctica

El claustre i l'equip docent poden utilitzar aquesta informació per:

-   Dissenyar activitats i projectes integrats amb una visió competencial
-   Assignar responsabilitats específiques de seguiment i avaluació per competència
-   Coordinar l'acció tutorial i les activitats d'orientació professional
-   Planificar de manera col·laborativa els **projectes intermodulars** i les **situacions d'aprenentatge**

Amb tot això, el **PCCF esdevé una eina viva**, en constant revisió, que assegura la cohesió del treball educatiu i l'alineació de les actuacions docents amb els objectius del sistema de Formació Professional i les necessitats de l'entorn.

### 4.3. Estructura modular i transició del currículum

Actualment, el cicle **Tècnic Bàsic en Informàtica d'Oficina** presenta la següent estructura modular i horària, vigent **fins al curs 2024-2025**. A partir del curs 2025-2026, s'implantarà una nova estructura que reflecteix els canvis introduïts pel nou marc normatiu.

#### **Estructura vigent fins al curs 2024-2025**

  **Curs**   **Mòdul Professional**                                                   **Hores setmanals**   **Hores totals**
  ---------- ------------------------------------------------------------------------ --------------------- ------------------
  **1r**     3031/. Ofimàtica i arxiu de documents                                    9                     300
             3029/. Muntatge i manteniment de sistemes i components informàtics       9                     290
             3009/. Ciències aplicades I                                              5                     158
             3011/. Comunicació i societat I                                          5                     158
             Tutoria                                                                  1                     34
             CV0005. Formació i Orientació Laboral I                                  1                     30
             **Total 1r curs**                                                        **30**                **970**
  **2n**     3016/. Instal·lació i manteniment de xarxes per a transmissió de dades   10                    255
             3030/. Operacions auxiliars per a la configuració i l'explotació         6                     155
             3019/. Ciències aplicades II                                             6                     158
             3012/. Comunicació i societat II                                         6                     158
             Tutoria                                                                  1                     34
             CV0006. Formació i Orientació Laboral II                                 1                     30
             3033/. Formació en centres de treball                                    /-                    240
             **Total 2n curs**                                                        **30**                **1.030**
             **Total cicle**                                                          **60**                **2.000**

------------------------------------------------------------------------

#### **Nova estructura a partir del curs 2025-2026**

  **Curs**   **Codi**   **Mòdul Professional**                                        **Hores setmanals**   **Hores totals**
  ---------- ---------- ------------------------------------------------------------- --------------------- ------------------
  **1r**     3029       Muntatge i manteniment de sistemes i components informàtics   9                     299
             3031       Ofimàtica i arxiu de documents                                9                     299
             3161       Comunicació i Ciències Socials I                              4                     133
             3163       Ciències aplicades I                                          4                     133
             TU01CF     Tutoria Primer                                                2                     69
             3159p      Itinerari personal per a l'ocupabilitat 1r                    2                     67
                        **Total 1r curs**                                             **30**                **1.000**
  **2n**     3016       Instal·lació i manteniment de xarxes de comunicació           10                    332
             3030       Configuració i explotació de sistemes informàtics             6                     200
             3159       Itinerari personal per a l'ocupabilitat                       1                     34
             3162       Comunicació i Ciències Socials II                             5                     166
             3164       Ciències aplicades II                                         5                     166
             TU02CF     Tutoria Segon                                                 1                     35
             3160972    Projecte intermodular d'aprenentatge col·laboratiu            2                     67
                        **Total 2n curs**                                             **30**                **1.000**
                        **Total cicle**                                               **60**                **2.000**

------------------------------------------------------------------------

Aquesta nova estructura reforça el **component competencial, transversal i integrat del currículum**, amb una clara aposta per la coordinació entre mòduls, la personalització de l'itinerari formatiu i el treball per projectes. L'equip docent haurà d'adaptar les seues programacions i estratègies metodològiques per tal de garantir l'aplicació efectiva d'aquest nou model.

## 4.4. Comparativa entre l'estructura vigent i la nova proposta curricular

La següent taula resumeix de manera comparativa les diferències entre l'estructura **vigent fins al curs 2024-2025** i la **nova proposta curricular a partir del curs 2025-2026** per al cicle de **Tècnic Bàsic en Informàtica d'Oficina**:

  **Aspecte**                               **Estructura vigent (fins 2024-2025)**          **Nova estructura (a partir de 2025-2026)**
  ----------------------------------------- ----------------------------------------------- ------------------------------------------------------------------
  Nombre total de mòduls                    12 mòduls                                       12 mòduls (amb codis i denominacions revisades)
  Projecte intermodular                     Apareix només a 2n curs com a mòdul específic   Es manté i es reforça com a element vertebrador
  Itinerari personal per a l'ocupabilitat   Present als dos cursos                          Es manté, però amb integració més activa en el PCCF
  Tutoria                                   Dos mòduls (1r i 2n)                            Es manté igual
  Comunicació i Ciències Socials            Dues fases (I i II)                             Es manté, amb ajustos metodològics
  Ciències aplicades                        Dues fases (I i II)                             Es manté, amb orientació cap a contextos professionals
  Denominació de mòduls tècnics             Formulació genèrica                             Denominació més precisa i funcional: configuració, xarxes/...
  Distribució horària                       30 h setmanals / 2.000 h totals                 Sense canvis (mateix volum global)
  Orientació competencial                   Implícita i a través d'objectius                Explícita, integrada i centrada en resultats d'aprenentatge (RA)
  Enfocament metodològic                    Tradicional amb algunes iniciatives actives     Actiu, per projectes, personalitzat i transversal

## 4.5. Consideracions per a la implementació

La nova proposta curricular comporta un **canvi de paradigma** en la manera com es planifica, s'imparteix i s'avalua el currículum de la Formació Professional Bàsica. Les principals implicacions per al desenvolupament del **PCCF** són:

-   Necessitat d'una **coordinació didàctica més estreta** entre docents dels diferents mòduls.
-   Incorporació de **metodologies actives** i de situacions d'aprenentatge contextualitzades.
-   Major **centralitat del projecte intermodular**, que esdevé eix transversal del procés formatiu.
-   Integració efectiva de les **competències per a l'ocupabilitat**, amb accions concretes des de cada mòdul.
-   Adaptació progressiva de les programacions a un model **orientat a l'assoliment de RA** i no només de continguts.

Aquest context reforça la funció estratègica del **PCCF com a instrument de planificació col·lectiva**, alineat amb els objectius del centre, el PEC i les exigències de la nova legislació educativa.


# 5. Contribució de cada mòdul a les competències per a l/'ocupabilitat

Igual que en l'apartat anterior, és important identificar **quines competències per a l'ocupabilitat es treballaran en cada mòdul professional**, per tal d'integrar-les de manera coherent i efectiva a l/'hora de programar.

Aquestes competències, que inclouen aspectes com la responsabilitat, l'autonomia, el treball en equip o l'adaptabilitat, **no tenen una relació directa amb les habilitats tècniques pròpies de la professió**, i per això no resulta convenient aplicar una ponderació percentual com es fa amb les competències professionals.

Al contrari, es recomana que **l'equip docent, en funció de la seua experiència i del disseny de les activitats d'aprenentatge, decidisca en quins mòduls és més adient treballar cada competència per a l'ocupabilitat**. Aquesta decisió s'hauria de prendre col·lectivament, tenint en compte el context, l'alumnat i els escenaris d'aplicació professional simulats o reals.

Aquestes competències són fonamentals per a l'**acollida, la permanència i el progrés en l'àmbit laboral**, i han d'estar **reflectides de manera clara i visible en les rúbriques, llistes de control, activitats d'autoavaluació i qualsevol altre instrument emprat per a l'avaluació** dels mòduls que les treballen. Aquesta inclusió permet garantir que el procés d'avaluació valore **tant el desenvolupament tècnic com les actituds i capacitats personals i socials** que configuren un perfil professional complet.

## 5.1. Relació orientativa entre mòduls i competències per a l'ocupabilitat

La següent taula ofereix una proposta inicial de **distribució de les competències per a l'ocupabilitat** entre els diferents mòduls del cicle:

  **Mòdul Professional**                                                   **Competències per a l'ocupabilitat desenvolupades**
  ------------------------------------------------------------------------ ---------------------------------------------------------------
  3029/. Muntatge i manteniment de sistemes i components informàtics       t), u), v), w), x), y), z)
  3031/. Ofimàtica i arxiu de documents                                    t), u), v), w), x), y), z)
  3016/. Instal·lació i manteniment de xarxes per a transmissió de dades   t), u), v), w), x), y), z)
  3030/. Operacions auxiliars per a la configuració i l'explotació         t), u), v), w), x), y), z)
  3161 / 3162. Comunicació i Ciències Socials I i II                       s), t), u), v), w), z)
  3163 / 3164. Ciències aplicades I i II                                   t), u), v), w), x), y), z)
  3159/. Itinerari personal per a l'ocupabilitat                           s), t), u), v), w), x), y), z)
  3160972/. Projecte intermodular d'aprenentatge col·laboratiu             t), u), v), w), y), z)
  Tutoria (TU01CF / TU02CF)                                                Seguiment actitudinal i suport al desenvolupament transversal

> Aquesta distribució hauria de ser revisada per l'equip docent en cada curs acadèmic, d'acord amb les programacions, els perfils d'alumnat i els objectius del projecte intermodular. Les competències per a l'ocupabilitat s'han d'integrar de forma natural en la dinàmica d'aula i han de ser **avaluables mitjançant indicadors clars i observables**.

Perquè això siga possible, cal:

-   Planificar situacions d'aprenentatge on aquestes competències apareguen de manera contextualitzada i significativa.
-   Incorporar-les explícitament en els **instruments d'avaluació** del mòdul (rúbriques, escales de valoració, llistes de control, autoavaluacions, etc.).
-   Fer ús de **metodologies actives i cooperatives** que faciliten el seu desplegament (projectes, tasques compartides, simulacions, etc.).
-   Establir espais de coordinació entre docents per **acordar evidències comunes**, seqüenciar-ne el treball i **garantir la coherència avaluadora**.

## 5.2. Rúbrica d'exemple: Competència "Treball en equip" (competència t)

La següent rúbrica mostra un exemple pràctic per a avaluar la competència **t) Comunicar-se i treballar en equip respectant l'autonomia i competència dels altres** dins d'una situació d'aprenentatge col·laborativa:

  **Indicador**                                             **Nivell 1** (Iniciació)          **Nivell 2** (En procés)         **Nivell 3** (Assolit)                   **Nivell 4** (Excel·lent)
  --------------------------------------------------------- --------------------------------- -------------------------------- ---------------------------------------- ----------------------------------------------------
  Participa activament en les tasques col·lectives          Només quan se li demana           Participa de manera irregular    Participa de manera regular              Participa amb iniciativa i constància
  Respecta les opinions i funcions del grup                 Té dificultats per acceptar-les   Les accepta amb ajuda            Les respecta i coopera activament        Ajuda a integrar les aportacions dels altres
  Es comunica de forma clara i efectiva amb el grup         Amb dificultats i poc claredat    Amb certa claredat i correcció   Amb claredat i adequació                 Amb fluïdesa, assertivitat i empatia
  Assumeix responsabilitats i compleix els acords de grup   Evita responsabilitats            Assumeix algunes tasques         Assumeix tasques de manera responsable   Assumeix lideratges i facilita la cohesió del grup

> Aquesta rúbrica pot adaptar-se a altres mòduls i a altres competències (com la responsabilitat, la iniciativa o l'autonomia), mantenint sempre la claredat dels indicadors i la relació amb les situacions d'aprenentatge concretes.

La inclusió d'aquests instruments en les programacions d'aula, així com el seu ús sistemàtic per part del professorat, permetrà consolidar una **avaluació integral i equitativa**, que tinga en compte **tant el desenvolupament tècnic com el creixement personal i social** de l'alumnat.

A més, cal tindre en compte que **l'equip docent es reuneix de manera setmanal**, fet que facilita el **seguiment compartit del desenvolupament de les competències per a l'ocupabilitat**. Aquestes reunions permeten:

-   Analitzar l'evolució de l'alumnat en relació amb aquestes competències transversals.
-   Compartir evidències d'aprenentatge observades en els diferents mòduls.
-   Ajustar o redefinir indicadors i estratègies d'intervenció educativa segons les necessitats reals del grup.
-   Coordinar accions específiques per al desenvolupament d'algunes competències en situacions comunes (com el projecte intermodular o activitats col·laboratives).

Aquest **seguiment sistemàtic, reflexiu i compartit** garanteix una visió integral de l'alumnat, i assegura que la **avaluació de les competències per a l'ocupabilitat** siga **coherent, contínua i orientada a la millora**.

A més, les conclusions de les reunions setmanals es recolliran de manera estructurada en actes i informes de seguiment pedagògic, que permetran fer un **retorn regular a l'alumnat**, així com ajustar, si cal, les intervencions educatives i les estratègies metodològiques.


# 6. Enfocaments didàctics i metodològics

El cicle de Formació Professional Bàsica en Informàtica d'Oficina a l'IES Jaume II el Just es fonamenta en un **enfocament actiu, contextualitzat i professionalitzador**, alineat amb els principis recollits a l'article 13 del **Reial decret 659/2023**, que promou la incorporació de **metodologies actives** en la docència dels cicles formatius.

Aquest enfocament no es limita a una declaració d'intencions, sinó que es **materialitza en un conjunt de principis metodològics consensuats** per l'equip docent, amb caràcter vinculant per a totes les programacions del cicle. El consens metodològic ha estat treballat en les reunions setmanals del claustre del cicle i suposa un compromís explícit amb un model pedagògic transformador.

## 6.1. Principis metodològics acordats

L'equip docent acorda aplicar de forma transversal les següents estratègies metodològiques:

-   **Aprenentatge basat en projectes (ABP)**: l'alumnat desenvolupa **projectes interdisciplinars** reals o simulats, com ara:
    -   *Projecte de reciclatge de plàstics i impressió 3D* (Ciències Aplicades II, IMX i Comunicació i Societat II)
    -   *Projecte "Aprenem de la Pluja"*, vinculat a la DANA de 2024, orientat a la restauració d'equipament TIC i dades.
    -   *Participació en la Fira Experimenta*, amb projectes de caràcter científic-tecnològic de divulgació.
-   **Aprenentatge-Servei (ApS)**: com a eix transversal, alguns projectes integren una dimensió social i de servei comunitari, com el **manteniment i instal·lació de xarxes** al propi centre per part de l'alumnat, amb finalitats reals i aplicació immediata.
-   **Aprenentatge col·laboratiu**: foment del treball en equip mitjançant activitats grupals estructurades, ús d'eines de gestió col·laborativa i **responsabilitat compartida** en tasques i rols.
-   **Contextualització professional i realisme pedagògic**: les situacions d'aprenentatge s'inspiren en l'àmbit laboral real i aprofiten el context del centre i l'entorn socioeconòmic.
-   **Personalització de l'aprenentatge i enfocament inclusiu**, adaptant les activitats als ritmes, necessitats i potencialitats de l'alumnat.
-   **Ús pedagògic de les TIC**: integració d'eines digitals tant per a la producció com per a la comunicació i l'organització del treball.
-   **Avaluació contínua i formativa**, basada en evidències d'aprenentatge, rúbriques competencials, observació directa, autoavaluacions i portafolis.

## 6.2. Coherència, seguiment i compromís docent

Aquest marc metodològic consensuat és de **compliment obligat per a tot el professorat del cicle**, i s'aplicarà tant a nivell de mòdul com en el desenvolupament del **Projecte Intermodular d'Aprenentatge Col·laboratiu**.

Les **reunions setmanals de l'equip docent** tindran com a funció, entre altres, fer **seguiment del desplegament metodològic**, ajustar estratègies si cal i garantir que es manté la coherència entre els mòduls i els objectius del PCCF.

Aquest enfocament metodològic pretén oferir una resposta eficaç als desafiaments del món laboral i educatiu actual, **convertint l'alumnat en protagonista actiu del seu aprenentatge** i facilitant la seua integració futura en entorns professionals reals.


# 7. Organització i distribució dels mòduls professionals

D'acord amb l'article 11 del **Reial decret 659/2023**, els centres de Formació Professional poden organitzar els mòduls de manera flexible, sempre que es respecten els resultats d'aprenentatge de cada un i el currículum oficial.

Amb aquesta finalitat, l'equip docent del cicle de **Formació Professional Bàsica en Informàtica d'Oficina** ha acordat una organització interna que **afavoreix el treball interdisciplinari dins de cada curs**, mitjançant agrupacions pedagògiques que permeten desenvolupar **projectes comuns, integració competencial i metodologies actives** com l'ABP i l'ApS.

## 7.1. Organització dels mòduls en **1r curs**

  --------------------------------------------------------------------------------------------------------------------------------------------------------
  **Àmbit de treball integrador**               **Mòduls implicats**                            **Projectes o actuacions vinculades**
  --------------------------------------------- ----------------------------------------------- ----------------------------------------------------------
  **Tecnologia i manteniment bàsic**            /- Muntatge i manteniment de sistemes/          Projecte: Simulació d'un taller TIC escolar
                                                - Ciències Aplicades I                          

  **Ofimàtica i documentació digital**          /- Ofimàtica i arxiu de documents/              Projecte: Creació de materials digitals i fitxes manuals
                                                - Comunicació i Ciències Socials I              

  **Ocupabilitat i desenvolupament personal**   /- Itinerari personal per a l'ocupabilitat I/   Dossier de perfil professional inicial
                                                - Tutoria I                                     
  --------------------------------------------------------------------------------------------------------------------------------------------------------

## 7.2. Organització dels mòduls en **2n curs**

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Àmbit de treball integrador**                **Mòduls implicats**                             **Projectes o actuacions vinculades**
  ---------------------------------------------- ------------------------------------------------ ----------------------------------------------------------------------
  **Xarxes i comunicacions TIC**                 /- Instal·lació i manteniment de xarxes/         Projecte APS: Manteniment real de la xarxa del centre
                                                 - Operacions auxiliars per a la configuració     

  **Tecnologia i sostenibilitat**                /- Ciències Aplicades II/                        Projecte: Reciclatge de plàstic i impressió 3D
                                                 - Projecte intermodular                          

  **Comunicació i gestió documental avançada**   /- Comunicació i Ciències Socials II/            Projecte: Memòries tècniques i comunicació digital
                                                 - Ofimàtica aplicada (recuperació i anàlisi)     

  **Ocupabilitat i orientació professional**     /- Itinerari personal per a l'ocupabilitat II/   Projecte: Dossier professional + CV + simulació d'entrevista laboral
                                                 - Tutoria II                                     
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

> El mòdul **Projecte intermodular d'aprenentatge col·laboratiu** s'integra de manera transversal als projectes del segon curs, actuant com a eix vertebrador de la metodologia ABP i facilitant la coordinació docent.

## 7.3. Objectius d'aquesta reorganització

Aquesta estructura respon a la voluntat de:

-   Potenciar la **coherència metodològica i competencial** dins de cada curs.
-   Desenvolupar **projectes amb sentit real i integrats** dins de l'horari lectiu.
-   Facilitar la **coordinació entre docents** de cada nivell per planificar i avaluar conjuntament.
-   Fomentar una **transició progressiva** cap a l'entorn professional i la inserció laboral.
-   Optimitzar l'ús del **Projecte Intermodular** com a espai de síntesi i treball col·laboratiu.

Aquesta reorganització **no altera la càrrega horària oficial** del cicle, sinó que reconfigura **lògiques de treball didàctic** per a afavorir l/'aprenentatge significatiu, transversal i amb sentit per a l'alumnat.

### 7.4. Organització específica del mòdul "Comunicació i Societat"

El mòdul de **Comunicació i Societat** presenta una estructura **singular** dins la Formació Professional Bàsica, ja que **integra de manera transversal continguts de diverses matèries de caràcter general**:

-   **Llengua Castellana**
-   **Llengua Valenciana**
-   **Ciències Socials**
-   **Llengua Estrangera (Anglés)**

A diferència d'altres mòduls de caràcter professional, aquest mòdul exigeix una **planificació didàctica coordinada entre diversos docents**, els quals han de garantir conjuntament el desenvolupament de tots els resultats d'aprenentatge vinculats als àmbits implicats.

Amb aquesta finalitat, el centre ha establit una **organització interna específica** del mòdul, basada en els següents criteris pedagògics:

-   **Coordinació metodològica transversal** mitjançant programacions compartides i reunions de seguiment entre els docents dels àmbits lingüístic, social i estranger.
-   **Distribució equilibrada dels continguts entre primer i segon curs**, assegurant una progressió didàctica coherent.
-   **Integració funcional de l'anglés** en tasques contextualitzades: simulació d'entrevistes, elaboració de documents, presentacions orals, etc.
-   **Orientació competencial i transversal**, vinculada a les competències comunicatives, socials, cíviques i per a l'ocupabilitat.
-   **Participació activa en projectes intermodulars**, on la dimensió comunicativa té un paper fonamental: redacció de memòries, sensibilització, exposicions orals, etc.

Aquest enfocament garanteix el desenvolupament d'habilitats de comunicació bàsica, de reflexió crítica sobre la realitat social i de participació responsable a la comunitat educativa.

Els docents implicats assumeixen el compromís de treballar amb **criteris d'avaluació consensuats**, i d'aplicar **instruments compartits d'avaluació formativa i competencial**, en coordinació amb el conjunt del professorat del cicle i dins del marc del **Projecte d'Acció Curricular (PAC)**.

------------------------------------------------------------------------

### 7.4.1 Organització del mòdul Comunicació i Societat I (Codi 3011)

Aquest mòdul, situat en **primer curs**, integra continguts inicials de llengua castellana, llengua anglesa i ciències socials. Els seus resultats d'aprenentatge (RA) tenen com a eixos:

-   L'anàlisi de les societats prehistòriques i de l'Edat Antiga, i les seues relacions amb l'entorn natural i artístic.
-   La construcció de l'espai europeu fins a les primeres transformacions industrials.
-   L'adquisició de competències bàsiques d'expressió i comprensió oral i escrita en castellà.
-   La iniciació a la literatura en llengua castellana.
-   La comunicació oral i escrita funcional en anglès en situacions quotidianes i escolars.

------------------------------------------------------------------------

### 7.4.2 Organització del mòdul Comunicació i Societat II (Codi 3012)

En **segon curs**, el mòdul aprofundeix en els mateixos àmbits però des d'un enfocament més complex i contextualitzat. Els RA s'orienten a:

-   Comprendre l'evolució de les societats contemporànies i el sistema democràtic.
-   Comunicar-se amb claredat i correcció en llengua castellana en contextos socials i laborals.
-   Interpretar i produir textos literaris des del segle XIX fins a l'actualitat.
-   Utilitzar l'anglés en interaccions senzilles de caràcter professional i personal, amb vocabulari específic i estructures bàsiques.

------------------------------------------------------------------------

### 7.4.3 Comparativa de Resultats d'Aprenentatge: Comunicació i Societat I vs II

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Àmbit**                          **Comunicació i Societat I (3011)**                     **Comunicació i Societat II (3012)**
  ---------------------------------- ------------------------------------------------------- -----------------------------------------------------------------------------
  **Ciències Socials**               RA1: Societats prehistòriques i antigues/               RA1: Societats contemporànies i evolució històrica/
                                     RA2: Edat Mitjana, moderna i construcció europea        RA2: Democràcia, Drets Humans i participació ciutadana

  **Llengua Castellana (oral)**      RA3: Comunicació oral bàsica i escolta activa           RA3: Comunicació oral estructurada i expressió adequada a contextos formals

  **Llengua Castellana (escrita)**   RA4: Producció de textos breus i lectura comprensiva/   RA4: Producció escrita de textos més complexos/
                                     RA5: Iniciació a la literatura clàssica                 RA5: Literatura contemporània i anàlisi crítica

  **Llengua Anglesa**                RA6: Expressió oral bàsica i estructurada/              RA6: Presentacions orals concretes/
                                     RA7: Diàlegs i converses senzilles/                     RA7: Interacció en contextos personals i laborals/
                                     RA8: Textos escrits breus                               RA8: Textos escrits amb detall
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

### 7.4.4 Distribució orientativa de responsabilitats docents

  **Àmbit**              **Responsable principal**                **Funcions específiques**
  ---------------------- ---------------------------------------- ---------------------------------------------------------------------------------------------
  Llengua Castellana/*   Professor/a de Llengua Castellana        Expressió oral i escrita, anàlisi de textos, lectura literària, gramàtica, ortografia
  Ciències Socials/*     Professor/a de Geografia i Història      Evolució històrica, ciutadania, democràcia, anàlisi de fonts i contextos socials
  Llengua Anglesa        Professor/a d'Anglés                     Producció i comprensió oral i escrita, vocabulari funcional, interacció en contextos reals
  Coordinació general    Equip docent del cicle + cap d'estudis   Planificació conjunta, seguiment d'alumnat, disseny de situacions d'aprenentatge integrades

> /* *Per motius d'organització interna i racionalització de recursos docents, els àmbits de Llengua Castellana i Ciències Socials poden estar integrats i ser atesos pel mateix professorat, habitualment el de Llengua Castellana.*


# 8. Criteris generals sobre l/'organització, la comunicació i desenvolupament del procés d/'avaluació de l/'aprenentatge

El procés d'avaluació de l'alumnat en el cicle de Formació Professional Bàsica en Informàtica d'Oficina es regirà per:

-   L'**Ordre 2025/13083** (DOGV 30.04.2025), que regula l'avaluació, acreditació, certificació i titulació en l'FP a la Comunitat Valenciana.
-   La **Llei orgànica 3/2022**, d'ordenació i integració de la FP.
-   El **Reial decret 659/2023**, pel qual s'estableix l'ordenació del sistema de Formació Professional.

Els principis generals que emanen d'aquesta normativa són:

1.  L'avaluació ha de ser **contínua, formativa i integradora**, adaptada als ritmes i característiques de l'alumnat.
2.  L'avaluació es basa en l'assoliment dels **Resultats d'Aprenentatge (RA)** definits per a cada mòdul.
3.  El procés ha de facilitar l'**orientació, la millora dels aprenentatges** i la **inserció laboral** de l'alumnat.

## 8.1 Organització del procés d'avaluació

-   Es realitzarà una **sessió inicial de diagnòstic** dins del primer mes de curs.
-   L'equip docent celebrarà **sessions d'avaluació trimestrals** i farà un seguiment setmanal de l'evolució de l'alumnat.
-   La **superació de cada mòdul** requerirà l'assoliment de tots els RA amb una qualificació mínima de 5 sobre 10.
-   L'alumnat amb una assistència inferior al 85% podrà perdre el dret a l'avaluació contínua.
-   Es preveuen **convocatòries ordinària i extraordinària** per a la recuperació dels RA no assolits.
-   El Projecte Intermodular serà també objecte d'avaluació coordinada entre els docents implicats.

## 8.2 Instruments d'avaluació

Els instruments d'avaluació es seleccionaran en funció del tipus de tasca i metodologia utilitzada:

-   **Proves pràctiques i escrites**
-   **Observació sistemàtica**
-   **Portafolis**
-   **Rúbriques i llistes de control**
-   **Autoavaluació i coavaluació**
-   **Seguiment de projectes i activitats col·laboratives**
-   **Presentacions orals i informes tècnics**

Els criteris d'avaluació s'ajustaran als RA i seran compartits amb l'alumnat des de l'inici del curs.

## 8.3 Comunicació amb l'alumnat i les famílies

-   Els criteris i instruments d'avaluació es publicaran a través de la plataforma *Aules* i seran explicats a l'alumnat a l'inici de cada mòdul.
-   L'equip docent mantindrà una **comunicació constant** mitjançant reunions de tutoria, notificacions digitals i entrevistes.
-   Els **butlletins oficials** de qualificacions es tramitaran a través de la plataforma *ITACA*.
-   Es fomentarà la **transparència i la participació activa** de les famílies en el seguiment del procés educatiu.

## 8.4 Desenvolupament del procés d'avaluació

-   L'avaluació es realitzarà sobre **cada RA de forma diferenciada**.
-   Cada RA haurà d'estar **superat de forma individual** per considerar-se el mòdul aprovat.
-   El professorat farà **ajustaments metodològics i de planificació** segons l'evolució del grup.
-   L'avaluació continuarà en la **Formació en Entorns Laborals (FEE)**.

## 8.5 Avaluació en la Formació en Entorns Laborals (FEE)

La FEE és una part fonamental del cicle formatiu. Es realitzarà:

-   Mitjançant un **seguiment conjunt entre el centre educatiu i l'empresa**.
-   L'avaluació es fonamentarà en **l'assoliment dels RA relacionats amb el mòdul**, contextualitzats a l'entorn laboral.
-   L'empresa col·laboradora emetrà un **informe de valoració** i el tutor o tutora acadèmica completarà la qualificació.

> *L'avaluació de la FEE es regirà pels mateixos criteris de rigor, objectivitat i coherència que la resta de mòduls del cicle.*

## 8.6 Avaluació del procés docent i del professorat

-   El professorat realitzarà una **autoavaluació contínua** de la seua pràctica docent.
-   L'equip docent revisarà **trimestralment** la coherència i eficàcia de les seues programacions.
-   A final de curs, es farà una **avaluació col·lectiva** sobre:
-   La selecció i seqüenciació de continguts.
-   Els criteris i instruments d'avaluació utilitzats.
-   L'adequació de les metodologies.
-   Els resultats de l'alumnat i el seu progrés.


# 9. Base de dades d/'empreses o organismes equiparats que col·laboren amb el PCCF i criteris d/'assignació de l/'alumnat

La plataforma **SAO** per a la gestió de la FEE (Formació en Entorns Laborals), així com de l'antiga FCT i la FP Dual, disposa d'una **base de dades** amb el registre de les empreses que col·laboren anualment amb el centre.

Tanmateix, l'equip educatiu ha acordat mantindre un **registre digital complementari**, específic del departament, que reculla l'historial de col·laboració amb les empreses i organismes equiparats. Aquest registre podrà mantindre's en format **full de càlcul** o integrat en la **plataforma web de la borsa de treball del centre**.

Els responsables de l'actualització d'aquest registre seran el **tutor o tutora del grup** i el/la **coordinador/a de formació en empresa**, i es realitzarà **just després de la finalització del període lectiu**. El registre inclourà, si és possible, els **Resultats d'Aprenentatge (RA)** treballats per l'alumnat en cada empresa, per tal d'ajustar els futurs **programes formatius individuals**.

A més, es fomentarà la **col·laboració activa de les empreses** en:

-   L'elaboració i revisió dels programes formatius.
-   El disseny i participació en projectes col·laboratius.
-   El desenvolupament d'una **xarxa de mentors** que done suport a l'alumnat en iniciatives d'emprenedoria.

## Criteris d'assignació de l'alumnat a les empreses

Per garantir una distribució equitativa i ajustada, es tindran en compte els següents criteris:

-   Adequació al perfil professional del cicle.
-   Competències, interessos i característiques personals de l'alumnat.
-   Ubicació geogràfica i possibilitat de desplaçament.
-   Capacitat de tutorització de l'empresa.
-   Garantia d'igualtat d'oportunitats.
-   Valoració de l'historial de col·laboració amb l'empresa.
-   Temporalització i disponibilitat per acollir alumnat.

És important destacar que el **teixit empresarial local** es compon principalment de **petites i mitjanes empreses (pimes)**, i que les empreses de major dimensió estan focalitzades en sectors específics dins l'àmbit TIC.

Aquest context dificulta, sovint, trobar empreses que puguen acollir alumnat en condicions òptimes per desenvolupar **tots els Resultats d'Aprenentatge del cicle**. Per aquest motiu, i per garantir la cobertura competencial, es preveu que els RA siguen **treballats de manera complementària entre l'empresa i el centre educatiu**, Aquest context dificulta, sovint, trobar empreses que puguen acollir alumnat en condicions òptimes per desenvolupar **tots els Resultats d'Aprenentatge del cicle**. Per aquest motiu, i per garantir la cobertura competencial, es preveu que els RA siguen **treballats de manera complementària entre l'empresa i el centre educatiu**.

La seua avaluació es basarà en **percentatges d'assoliment**, en lloc de considerar els RA com a blocs tancats. Aquesta distribució parcial i compartida haurà de quedar **clarament reflectida en les programacions d'aula dels mòduls implicats**, indicant quines parts s'abordaran a l'empresa i quines es desenvoluparan al centre, així com els criteris i instruments d'avaluació associats.

### Exemple de taula de distribució dels RA entre centre i empresa

  **Mòdul professional**                 **Codi**   **RA**   **Descripció del RA**                                    /% al Centre   /% a l/'Empresa   Observacions
  -------------------------------------- ---------- -------- -------------------------------------------------------- -------------- ----------------- ---------------------------------------
  Aplicacions Ofimàtiques                3013       RA1      Utilitza aplicacions de processador de textos            70%            30%               Activitats de redacció a l'empresa
  Instal·lació i manteniment de xarxes   3014       RA2      Realitza connexions bàsiques i diagnòstics de xarxa      50%            50%               Pràctiques directes amb client
  Comunicació i Societat II              3012       RA6      Comunica informació oral en anglès en context laboral    40%            60%               Simulacions reals i atenció en anglès
  Tractament de la informació digital    3015       RA3      Arxiva i gestiona informació amb criteris de seguretat   60%            40%               Adaptat a protocols de l'empresa

*Aquesta taula pot ser adaptada per a cada mòdul, i complementada amb instruments d'avaluació específics (rúbriques, fulls d'observació, informes de tutoria/...).*


# 10. Criteris per a realitzar els plans formatius individuals

Cada alumne o alumna que participe en un itinerari de **Formació en Entorns Laborals (FEE)** haurà de disposar d'un **Pla Formatiu Individualitzat (PFI)** que definisca de manera clara i flexible les activitats formatives a desenvolupar tant al **centre educatiu** com a l'**empresa o organisme col·laborador**.

Aquest Pla Formatiu serà el resultat d'un procés de **codisseny entre el centre i l'empresa**, i haurà d'assegurar la **cobertura de tots els Resultats d'Aprenentatge (RA)** establits en el currículum, distribuint-los entre ambdós espais formatius segons la seua naturalesa, les capacitats de l'empresa i les necessitats de l'alumnat.

## Criteris generals per a la seua elaboració

-   El Pla Formatiu haurà de ser **coherent amb la programació d'aula del mòdul professional** i el **PAC del cicle**.
-   Es concretarà la **relació de RA assignats a l'empresa, al centre i compartits**, indicant els **percentatges d'assoliment estimats** en cada àmbit.
-   Caldrà indicar els **objectius específics**, **tasques formatives**, **condicions de seguiment**, així com els **instruments i criteris d'avaluació**.
-   S'inclouran les **competències per a l'ocupabilitat** a desenvolupar preferentment en context real.
-   Es preveuran **mecanismes de revisió i ajust del pla**, especialment quan es produïsquen canvis rellevants en el context formatiu o empresarial.

## Documentació i protocol

Per garantir l'homogeneïtat i el seguiment de qualitat, el centre establirà un **model de document de PFI**, que inclourà com a mínim:

-   Dades de l'alumne/a i de l'empresa col·laboradora.
-   Responsable de tutoria acadèmica i de supervisió a l'empresa.
-   RA assignats i percentatges corresponents.
-   Activitats formatives previstes.
-   Indicadors d'avaluació i instruments associats.
-   Dates clau i horari previst.
-   Signatura de les parts implicades.

Aquest document serà **signat pel centre, l'empresa i l'alumne/a**, i constituirà el marc de referència per al seguiment i l'avaluació de l'estada formativa.

Els Plans Formatius Individuals s'arxivaran en format digital i estaran **disponibles per a la inspecció educativa, la coordinació de FEE i l'equip docent**.

> 🗂 *A més, la informació continguda en el PFI podrà ser incorporada com a evidència dins del portafoli d'avaluació de l'alumnat.*


# 11. Criteris per a adaptar els mòduls de Digitalització i Sostenibilitat a les característiques específiques del perfil professional del cicle formatiu

Els mòduls **transversals** de **Digitalització Aplicada als Sectors Productius** i **Sostenibilitat Aplicada al Sistema Productiu** formen part del currículum comú de la nova Formació Professional i tenen un **caràcter integrador i contextual**. Per això, és necessari **adaptar-ne els continguts, activitats i enfocaments** a les **característiques del cicle formatiu de FPB en Informàtica d'Oficina**, així com al **perfil professional de l'alumnat** i a la realitat del teixit productiu de l/'entorn.

## Adaptació del mòdul de Digitalització

El mòdul de **Digitalització** s'orientarà a dotar l'alumnat de competències bàsiques per a comprendre i aplicar processos de digitalització en contextos administratius i d'oficina. En concret, es treballaran:

-   **Ús d'eines digitals col·laboratives** (drive, calendari, suite ofimàtica en núvol, etc.)
-   **Digitalització de documents i arxius**, amb formats estandarditzats i criteris d'organització segura.
-   **Coneixements bàsics de ciberseguretat i protecció de dades**, aplicats a la gestió documental.
-   Introducció al concepte d'**automatització de tasques administratives** amb programari d'oficina.
-   Participació en **projectes de digitalització del centre o de la comunitat**, com per exemple, la gestió de fitxers o l'organització de dades per a esdeveniments escolars.

## Adaptació del mòdul de Sostenibilitat

Pel que fa al mòdul de **Sostenibilitat**, es proposarà una aproximació pràctica i contextualitzada, que ajude a l'alumnat a comprendre l'impacte ambiental i social de les activitats administratives i digitals. Es prioritzaran:

-   Pràctiques d'**estalvi de recursos** en l'ús de tecnologies (paper, tinta, energia/...).
-   **Gestió responsable de residus electrònics** (tòners, aparells informàtics obsolets).
-   Foment del **consum responsable**, especialment en compres i equipaments per a l'oficina.
-   Introducció al càlcul de la **petjada ecològica** i a l'impacte dels hàbits digitals (ús de núvol, enviament massiu de correus, etc.).
-   Participació en **projectes transversals** com el projecte de **reciclatge de plàstic i impressió 3D**, en col·laboració amb altres mòduls.

## Enfocament transversal i coordinat

Ambdós mòduls es desplegaran en coordinació amb la resta de mòduls del cicle, i **preferentment dins de situacions d'aprenentatge o projectes intermodulars**. Això garantirà:

-   **Contextualització real dels continguts**, afavorint la transferència d'aprenentatges.
-   **Avaluació integrada** a través de projectes i activitats col·laboratives.
-   **Enfocament competencial i vivencial**, orientat a la inserció laboral i la ciutadania responsable.

L'equip docent establirà anualment, dins de la **PGA**, quines activitats o projectes oferiran millor encaix per integrar **digitalització i sostenibilitat** dins del cicle, i quins criteris s'utilitzaran per a la seua avaluació.


# 12. El pla de tutoria i orientació professional

Per al cicle formatiu de **Formació Professional Bàsica en Informàtica d'Oficina**, i d'acord amb l'article 91 de la LOMLOE, el Decret 72/2021 i l'Orde 10/2023, l'equip docent estableix les següents **línies estratègiques de tutoria i orientació professional**. Aquestes s'han de concretar en els **plans d'acció tutorial (PAT)** anuals de cada grup.

## 1. Organització de la tutoria

-   El/la tutor/a serà un/a docent del grup amb hores assignades a tutoria segons la PGA.
-   Encara que no hi haja hora setmanal específica, es podran fer **sessions de tutoria dins de les hores lectives** del mòdul assignat al/la tutor/a.
-   Les **sessions grupals** es dedicaran a aspectes personals, acadèmics i professionals.
-   Les **entrevistes individuals** serviran per fer seguiment i donar suport a l'alumnat amb NESE o situacions personals complexes.
-   Es garantirà la coordinació amb el **departament d'orientació** per:
-   Detectar necessitats específiques.
-   Establir estratègies individualitzades.
-   Fer acompanyament emocional i acadèmic.

## 2. Orientació acadèmica

-   S'organitzaran activitats per a informar sobre opcions formatives posteriors:
-   Cicles de Grau Mitjà de la mateixa família professional.
-   Cursos d'especialització i certificacions professionals.
-   Altres vies formatives (ocupacional, PICE, formació a distància, etc.).
-   Es realitzaran:
-   **Xarrades amb professorat** de cicles superiors.
-   **Trobades amb exalumnes** titulats.
-   **Sessions informatives** sobre les comissions col·legiades d'orientació.

## 3. Orientació professional, inserció laboral i emprenedoria

-   L'alumnat participarà en activitats com:
-   **Taller de recerca d'ocupació** (CV, entrevistes, portals).
-   **Fires d'ocupació i visites a empreses**.
-   **Xarrades amb professionals del sector**.
-   Difusió del **caràcter dual de la FP** i possibilitats d'inserció directa.
-   **Hackatons, concursos i activitats de captació de talent**.
-   Mentories amb professionals i exalumnes per fomentar l'emprenedoria.
-   Orientació cap a **reptes reals** que puguen convertir-se en projectes d'empresa.

## 4. Seguiment i avaluació del pla

-   El Pla de Tutoria i Orientació es **avaluarà anualment**, durant el tercer trimestre, amb:
-   **Enquestes de valoració de l'alumnat**.
-   **Reunions de l'equip docent i amb el departament d'orientació**.
-   **Informe final de valoració del PAT**, amb propostes de millora.
-   Els resultats d'aquesta avaluació es tindran en compte per ajustar les accions del curs següent.

------------------------------------------------------------------------

## /[clip/] Annexos del pla de tutoria i orientació

### [Annex 1. Model d'entrevista individual](../annexos/Annex1-Entrevista/)

### [Annex 2. Qüestionari d'interessos professionals](../annexos/Annex2-Interessos/)

### [Annex 3. Fitxa de seguiment del PAT](../annexos/Annex3-SeguimentPAT/)

### [Annex 4. Enquesta de valoració del pla (alumnat)](../annexos/Annex4-EnquestaAlumnat/)


# 13. Concreció dels plans i els programes del centre vinculats al currículum

Aquest apartat concreta com es despleguen, dins del cicle de **Formació Professional Bàsica en Informàtica d'Oficina**, els **plans, projectes i programes impulsats pel centre**, assegurant la seua **coherència amb els objectius del currículum** i la formació integral de l'alumnat. Es descriuen accions específiques, mòduls implicats, responsables i temporalització aproximada.

## 1. Programa Emprén -- Aula Emprenedora

El centre participa activament en el **Programa Emprén**, de foment de la cultura emprenedora. L'Aula Emprenedora promou:

-   L'**emprenedoria social, sostenible i col·laborativa**.
-   El desenvolupament d'**habilitats personals i professionals**.
-   La sensibilització cap a models de negoci responsables i innovadors.

## 2. Projecte /"JustHub Garage -- Espai d'Innovació i Creativitat/"

Llançat el curs 2024, aquest projecte transforma l'aula en un **entorn de coworking i laboratori de prototipatge**, inspirat en les empreses nascudes en garatges. Està alineat amb l'estratègia d'**Aules Transformadores**, i s'hi desenvolupen:

-   Projectes interdisciplinars basats en reptes reals del sector TIC.
-   Metodologies com **Design Thinking**, **Scrum** o **ABP**.
-   Espais que simulen una **aula-empresa col·laborativa**.

### Accions concretes:

  Acció                                                     Mòduls implicats                       Temporalització    Responsables
  --------------------------------------------------------- -------------------------------------- ------------------ ----------------------------------------
  Desenvolupament de projectes col·laboratius (coworking)   IMX, CAII, Comunicació i Societat II   Octubre - Maig     Equip docent i mentors externs
  Introducció a metodologies àgils                          IMX, Sostenibilitat                    Octubre - Gener    Coordinador/a JustHub
  Projectes de sostenibilitat i digitalització              Tots els mòduls                        Tot el curs        Coordinació docent
  Tallers i xarrades d'emprenedoria                         Tutoria, Comunicació                   Novembre - Abril   Aula Emprén + empreses col·laboradores
  Mostra final de projectes (demo day)                      Tots els mòduls                        Final de curs      Equip docent i col·laboradors externs

## 3. Altres plans i programes

-   **Orientació Professional (Decret 72/2021)**: Integrada en les tutories i activitats del mòdul de Comunicació, coordinada amb el Departament d'Orientació.
-   **Formació i inserció laboral (FCT i borsa d'ocupació)**: Coordinació amb empreses locals i serveis municipals d'ocupació.
-   **Participació en convocatòries INNOVATEC o projectes de millora**: Quan siga aplicable, els projectes d'innovació es connectaran amb continguts del mòdul de digitalització o sostenibilitat.

## 4. Objectius didàctics i alineació curricular

Tots aquests programes reforcen:

-   El treball de les **competències professionals, personals i socials**.
-   La connexió amb els **ODS** (Agenda 2030), especialment en l'àmbit tecnològic i ambiental.
-   L'adquisició d'**experiència pràctica i projectes significatius** per a l'alumnat.

Amb aquesta visió transversal, es fomenta una formació contextualitzada, flexible i orientada a la ciutadania activa i emprenedora.


# 14. Orientacions per a l/'ús d/'espais, mitjans i equipaments disponibles

L'organització dels espais i dels recursos materials en el cicle de **Formació Professional Bàsica en Informàtica d'Oficina** té com a objectiu **facilitar un aprenentatge actiu, segur i contextualitzat**, d'acord amb els requisits establerts pel *Reial decret 405/2023* i alineat amb els principis d'innovació metodològica i pedagògica.

## 1. Condicions dels espais docents

Segons la normativa:

-   Cal disposar d'un **espai formatiu de mínim 60 m²** per grup.
-   El grau d'utilització ha de ser **igual o superior al 50%** del temps disponible.
-   Es garantiran les següents **condicions ambientals i de seguretat**:
-   **Humitat**: controlada per evitar condensació i electricitat estàtica.
-   **Il·luminació**: lateral i difusa, per evitar reflexos en pantalles.
-   **Cablejat**: centralitzat, segur i fora de zones de pas.
-   **Mobiliari ergonòmic**: per protegir la salut postural de l'alumnat.

## 2. Transformació metodològica i Aula-Empresa

El cicle es desplega seguint un model d'**aula-empresa**, on l'aula simula un **entorn productiu col·laboratiu**. Aquesta transformació implica:

-   Organització de l'espai en **illes de treball col·laboratiu**.
-   Creació d'una **zona de reunions** per a planificació i feedback.
-   Utilització de **mobiliari flexible** (pissarres mòbils, pantalles compartides).
-   Espais diferenciats per a **presentació de projectes** o defensa d'evidències.

Aquest entorn afavoreix metodologies com l'**Aprenentatge Basat en Projectes (ABP)**, **reptes**, o **simulacions d'entorns laborals**, fonamentals per a l'adquisició de les competències del cicle.

## 3. Ús de l'Aula Emprén

El centre disposa d'una **Aula Emprén**, vinculada al Programa Emprén. Aquesta aula permet desenvolupar:

-   **Tallers de creativitat i ideació de projectes**
-   **Hackatons i concursos** interdisciplinars
-   **Xarrades amb empreses i mentors**
-   **Simulació de presentacions professionals** i esdeveniments

S'utilitzarà especialment per a l'impuls del projecte **JustHub Garage** i per activitats dels mòduls de *Tutoria*, *Comunicació i Societat* i *Sostenibilitat*.

## 4. Coordinació i ús compartit dels espais

Per optimitzar els espais del centre i garantir-ne un ús eficient:

-   Es coordinarà la utilització de les aules especialitzades (*tècniques, informàtiques, Emprén*) entre els diferents mòduls i grups.
-   Es podran establir **protocols d'ús i reserva**.
-   Es prioritzaran aquelles activitats relacionades amb **projectes intermodulars, digitalització i sostenibilitat**.

------------------------------------------------------------------------

**Conclusió**:/
L/'ús intencionat dels espais i equipaments disponibles permetrà **contextualitzar l'aprenentatge**, millorar la **motivació de l'alumnat**, i connectar-lo amb els **entorns reals de treball**, facilitant així l'assoliment dels resultats d'aprenentatge establerts.


# 15. Criteris i procediments per a l/'avaluació i la revisió de la pràctica docent

L'avaluació i revisió de la **pràctica docent** en la Formació Professional Bàsica és una eina clau per garantir la qualitat educativa i millorar de manera contínua el procés d'ensenyament-aprenentatge. En aquesta etapa, on l'alumnat sovint presenta trajectòries escolars complexes, cal una revisió docent **especialment sensible a la motivació, inclusió i orientació professional**.

Aquest procés d'avaluació es fonamenta en els **principis de la LOMLOE** (article 1, LO 3/2020) i inclou la reflexió sobre la **planificació, execució i resultats**, tant individuals com col·lectius, de la tasca docent.

## Criteris per a la revisió de la pràctica docent

1.  **Adequació al currículum de FPB**:

    -   Ajust de les programacions als resultats d'aprenentatge i sabers bàsics del currículum.
    -   Adaptació dels continguts al nivell competencial i ritme de l'alumnat.
    -   Coherència entre sabers, criteris d'avaluació i instruments aplicats.

2.  **Adaptació a les característiques de l'alumnat**:

    -   Aplicació de mesures universals, addicionals o personalitzades per garantir l'èxit educatiu.
    -   Consideració del pla personal d'aprenentatge (PPA) quan siga aplicable.

3.  **Metodologies actives i personalitzades**:

    -   Ús d'ABP, APS, reptes, tallers i simulacions com a estratègies habituals.
    -   Participació de l'alumnat com a protagonista del seu procés d'aprenentatge.

4.  **Inclusió i gestió d'aula**:

    -   Promoció d'un clima positiu, respectuós i segur.
    -   Ús d'estratègies de gestió emocional, resolució de conflictes i mediació educativa.

5.  **Avaluació formativa i competencial**:

    -   Aplicació de rúbriques, escales descriptives i portafolis.
    -   Observació del progrés i ajust del procés d'ensenyament en temps real.

6.  **Orientació i acompanyament**:

    -   Integració del pla de tutoria i orientació dins de les activitats del mòdul.
    -   Coordinació amb el departament d'orientació i serveis socials si cal.

## Procediments d'avaluació de la pràctica docent

-   **Autoavaluació docent**: cada professor realitzarà una reflexió individual (almenys un cop per curs) sobre les seues fortaleses, àrees de millora i necessitats de suport.

-   **Anàlisi col·lectiva**: l'equip docent realitzarà una reunió de revisió trimestral per compartir bones pràctiques, revisar dificultats i proposar millores.

-   **Enquestes de valoració de l'alumnat**: es passarà una enquesta breu a final de cada trimestre o quadrimestre per recollir la seua percepció sobre el clima d'aula, les activitats i el seu propi aprenentatge.

-   **Valoració conjunta amb l'equip orientador**: especialment en casos amb PPA, es farà una valoració específica de les adaptacions aplicades i de l'impacte en la motivació i l'assistència de l'alumnat.

## Revisió del Projecte Curricular del Cicle Formatiu (PCCF)

El **PCCF s'analitzarà anualment** al final del curs escolar en una sessió d'avaluació global. En aquest espai, es valorarà:

-   La implementació real dels criteris i metodologies acordades.
-   L'adequació dels recursos, espais i materials.
-   L'impacte dels projectes transversals en l'assoliment de competències.
-   La coordinació entre mòduls i amb serveis externs.

El resultat d'aquesta revisió podrà comportar **modificacions concretes** per al següent curs, que quedaran recollides com a *actualitzacions* del PCCF, sempre d'acord amb el principi de millora contínua i col·laborativa.

------------------------------------------------------------------------

## /[clip/] Annexos de suport

Per facilitar el procés de revisió i reflexió docent, es proposen els següents annexos:

-   [/[nota/] Model d'autoavaluació docent](../annexos/Annex-Autoavaluacio-Docent/)
-   [/[llista/] Enquesta de valoració del mòdul (alumnat)](../annexos/Annex-Enquesta-Alumnat/)

Aquests materials es poden adaptar a cada mòdul o departament, i poden formar part de la documentació habitual de final de trimestre o de curs.


# 16. Atenció a la diversitat. Mesures de resposta educativa a la inclusió

L/'atenció a les diferències individuals és un **precepte constitucional** (Constitució Espanyola, Art. 27.1) i un pilar de l/'educació inclusiva. En l/'àmbit de la Formació Professional Bàsica (FPB), aquest compromís es concreta mitjançant les **Mesures de Resposta Educativa per a la Inclusió (MREI)**, tal com estableixen la **LO 3/2022** i el **RD 659/2023**.

Aquestes mesures tenen com a finalitat **eliminar les barreres** d/'accés, participació i aprenentatge, i assegurar que tot l'alumnat tinga oportunitats reals per assolir les competències del cicle.

## Principis normatius

D'acord amb el RD 659/2023, article 15, les mesures s'han d'ajustar a:

-   **Normalització i inclusió educativa**
-   **Accessibilitat universal i disseny per a tots**
-   **Adaptació de condicions d'aprenentatge i avaluació**

## Tipologia de mesures (MREI)

### 1. Adaptacions metodològiques

-   Ús de **metodologies actives i flexibles** (ABP, reptes, tallers col·laboratius).
-   Disseny d'**activitats graduades** que permeten diferents nivells d/'assoliment.
-   Atenció a la diversitat d'estils d'aprenentatge (visual, kinestèsic, etc.).

### 2. Suport personalitzat i tutorització

-   **Tutories individualitzades** per establir plans de seguiment o PPA.
-   Dinàmiques de suport emocional, regulació i motivació.
-   Observació sistemàtica per identificar necessitats emergents.

### 3. Adaptacions d'organització i d'espais

-   Agrupaments flexibles i suport dins l'aula ordinària.
-   Ajustos en la distribució de temps, activitats i materials.
-   Coordinació amb el departament d'orientació i serveis externs.

### 4. Accessibilitat i recursos adaptats

-   Materials accessibles (ampliació de tipografia, contrast, lectura fàcil/...).
-   Ús de **tecnologies assistives** (lector de pantalla, subtítols, teclats especials/...).
-   Eliminació de barreres físiques, sensorials i digitals.

## Avaluació inclusiva

-   Avaluació **personalitzada i formativa**, orientada al progrés.
-   Ús d'**instruments diversos i adaptats** (rúbriques, observació, exposicions, autoavaluació).
-   Flexibilitat en les condicions (temps extra, format de proves, presentacions orals/...).

## Revisió i seguiment

-   Les MREI seran acordades i revisades **col·lectivament** per l'equip docent en coordinació amb el departament d'orientació.
-   Les mesures aplicades es revisaran **trimestralment**, i s'ajustaran segons l'evolució de l'alumnat i les necessitats detectades.

## Referències normatives i recursos

-   LO 3/2022, d/'ordenació i integració de la Formació Professional
-   RD 659/2023, d'ordenació dels cicles de grau bàsic
-   GVA: [Mesures d'inclusió educativa](https://ceice.gva.es/va/web/inclusioeducativa)
-   GVA: [Identificació de barreres](https://ceice.gva.es/es/web/inclusioeducativa/identificacio-de-barreres)

## Comentari final

En el marc del Projecte Curricular de Cicle Formatiu, les MREI s'integren com a part fonamental del model pedagògic del centre. La seua aplicació en FPB esdevé imprescindible per garantir l'**equitat real** i la **justícia educativa**, superant una visió només compensatòria.

> /[idea/] Les MREI no són excepcions, sinó respostes sistemàtiques i estructurades que reconeixen i abracen la diversitat.


# 17. Criteris per a la planificació d/'activitats complementàries i extraescolars

Les **activitats complementàries i extraescolars** són eines pedagògiques que **enriqueixen i consoliden** el procés d'ensenyament-aprenentatge. Permeten a l'alumnat aplicar els coneixements adquirits en entorns reals, millorar la motivació i desenvolupar competències transversals.

Aquestes activitats es programaran seguint els criteris acordats per l'equip docent i alineats amb els **objectius del currículum del cicle FPB d'Informàtica d'Oficina**.

## Criteris generals per a la planificació

1.  **Pertinència curricular**: han de reforçar els continguts i sabers treballats als mòduls.
2.  **Caràcter inclusiu**: totes les activitats han de ser accessibles i promoure la participació de tot l'alumnat.
3.  **Coherència amb la programació d/'aula**: han d'estar relacionades amb els objectius i competències específiques dels mòduls.
4.  **Viabilitat organitzativa**: es valorarà la logística, horaris, pressupost i recursos disponibles.
5.  **Informació prèvia a l'alumnat i famílies**: es facilitarà una comunicació clara sobre objectius, continguts, dates i requisits de participació.

## Tipus d/'activitats

### Activitats complementàries

Realitzades dins de l'horari lectiu, amb caràcter pedagògic i estretament vinculades al currículum.

-   **Tallers tecnològics** (automatització, IA, impressió 3D...)
-   **Jornada de contacte amb empreses del sector**
-   **Seminaris d'especialització** amb professionals TIC
-   **Visita a la Fossa 112 de Paterna** (memòria històrica i tecnologia aplicada)
-   **Eixides de curta durada a l'entorn de la ciutat i muntanya** (orientació, treball en equip, medi ambient)
-   **Hackatons i jams tecnològiques** dins del centre

### Activitats extraescolars

Fora de l'horari lectiu, obertes a la participació voluntària i orientades a l'enriquiment acadèmic i personal.

-   **Visita al Museu del videojoc d'Ibi**
-   **Visites a universitats o centres tecnològics**
-   **Competició Programame**
-   **Skills Comunitat Valenciana**
-   Participació en fires i concursos com:
-   **Experimenta** (UV)
-   **La Navaja Negra** (ciberseguretat)
-   **Buca IMSEF** (projectes internacionals)
-   **ISIF** (fira internacional d'innovació educativa)

## Coordinació i seguiment

L'equip docent farà una planificació anual d'activitats, tenint en compte:

-   Els **projectes interdisciplinars** en curs.
-   Les **necessitats formatives i motivacionals** de l'alumnat.
-   La valoració d'impacte de cursos anteriors.

Així mateix, es garantirà l'avaluació de cada activitat per mitjà de **rúbriques, qüestionaris de satisfacció o evidències documentals**, integrant-les com a part del desenvolupament competencial del cicle.

------------------------------------------------------------------------

## /[clip/] Annexos de suport

Els següents documents faciliten la planificació i valoració de les activitats complementàries i extraescolars:

-   [/[calendari/] Fitxa de planificació d'activitat](../annexos/Annex-Planificacio-Activitat/)
-   [/[gràfic/] Fitxa de valoració d'activitat](../annexos/Annex-Valoracio-Activitat/)

Es recomana utilitzar aquestes plantilles per a totes les activitats organitzades dins del cicle FPB.


# 18. Criteris per a l/'organització del mòdul professional de projecte

Aquest apartat **no és aplicable al cicle de Formació Professional Bàsica d/'Informàtica d/'Oficina**, ja que aquest **no inclou el mòdul professional de projecte** dins del seu currículum, segons el Reial decret 127/2014 i el Reial decret 356/2014.

No obstant això, els **projectes interdisciplinaris** i activitats col·laboratives realitzades al llarg del cicle compleixen la funció d/'aplicació pràctica dels coneixements, d/'acord amb els principis metodològics de l/'FPB.


# 19. Altres aspectes que ha de contindre el PCCF

Aquest apartat recull **acords interns, decisions pedagògiques i aspectes rellevants** consensuats per l'equip docent del cicle de **Formació Professional Bàsica d'Informàtica d'Oficina**.

Tot i que no formen part d'un bloc normatiu específic, aquests aspectes complementen el projecte curricular i **contribueixen a la cohesió metodològica, pedagògica i organitzativa** del cicle.

## 1. Acords metodològics

-   Ús generalitzat de metodologies actives: ABP, reptes, simulacions, tallers/...
-   Aposta per l'**aprenentatge vivencial i contextualitzat**, relacionat amb entorns reals.
-   Preferència per activitats intermodulars coordinades dins d'un mateix projecte o situació d'aprenentatge.

## 2. Acords d/'avaluació

-   Ús compartit d'escales qualitatives, rúbriques i portafolis per a una avaluació formativa.
-   Disseny conjunt d'instruments d'avaluació per projectes transversals.
-   Establiment de mínims consensuats per a l'avaluació contínua.

## 3. Acords d'inclusió i convivència

-   Protocol intern per a la detecció primerenca de dificultats d'aprenentatge.
-   Coordinació mensual amb orientació per al seguiment de casos amb MREI o PPA.
-   Espais de trobada amb alumnat per tractar qüestions de convivència, benestar i clima d'aula.

## 4. Altres acords específics

-   Compromís de participació del cicle en activitats del centre (jornades culturals, fires, etc.)
-   Creació d'una comissió de projectes per coordinar accions com JustHub Garage o FP Skills.

> 🗒️ *Aquest apartat pot actualitzar-se cada curs escolar amb els nous acords establerts pel claustre docent o la comissió pedagògica del cicle.*

## 5. Informe del Departament d'Informàtica i Comunicacions sobre la programació didàctica en FPB

En compliment de les **Instruccions d'inici de curs 2025-2026 de la GVA**, aquest Departament elaborarà la **programació didàctica única de cada mòdul professional** del cicle, amb caràcter de document marc per a tot el curs i per a tot l'alumnat, independentment del torn, la modalitat o el règim en què s'impartisca.

No obstant això, i amb la finalitat de deixar constància en el **Projecte Curricular de Cicle Formatiu (PCCF)**, l'Equip del Departament d'Informàtica i Comunicacions **manifesta informe desfavorable** davant aquesta aplicació normativa, atés que:

-   **No s'alinea amb el canvi de paradigma educatiu** establit per la **LOMLOE** i la **Llei Orgànica de Formació Professional**, que impulsen un model competencial i d'**avaluació formativa i contínua**.
-   **Genera incoherència interetapes**, ja que en Primària, ESO i Batxillerat, mitjançant les Instruccions d'inici de curs, aquest canvi s'ha traduït en l'ús de les **Situacions d'Aprenentatge (SA)** com a instrument didàctic, mentre que en FP es manté un esquema basat en **Unitats de Programació (UP)**.
-   **Redueix la capacitat de connexió entre Resultats d'Aprenentatge, Criteris d'Avaluació i Sabers**, en no contemplar clarament la seua planificació i concreció en activitats contextualitzades.
-   **Allunya la FP de la seua finalitat última**, que és preparar l'alumnat per a entorns reals i professionals mitjançant aprenentatges aplicats, flexibles i basats en la resolució de reptes.

Per tant, **acatem les Instruccions vigents**, però el Departament d'Informàtica i Comunicacions considera que la decisió **no respon plenament a l'esperit de la legislació bàsica ni a l'orientació pedagògica de la resta d'etapes educatives**, i recomana que en futures adaptacions normatives es recupere la coherència global, incorporant instruments didàctics que permeten el desenvolupament real del model competencial (com les **Situacions d'Aprenentatge**).

------------------------------------------------------------------------

## Annex: Diferències entre Unitats Didàctiques / Unitats de Programació (UD/UP) i Situacions d'Aprenentatge (SA)

Les **Unitats Didàctiques (UD)** foren introduïdes amb la LOGSE i mantingudes amb la LOMCE com a model bàsic de planificació./
Actualment, les **Instruccions d'inici de curs de la GVA** exigeixen l'ús de **Unitats de Programació (UP)** com a instrument de la programació didàctica en FP.

En canvi, la **LOMLOE** i la **Llei de FP** estableixen un nou paradigma educatiu basat en el desenvolupament competencial i l'avaluació formativa./
Aquest canvi, en altres etapes educatives (Primària, ESO i Batxillerat), s'ha concretat a través de les **Situacions d'Aprenentatge (SA)**, que actuen com a instrument didàctic central.

  Aspecte                   Unitats Didàctiques / Unitats de Programació (UD/UP)                                                                   Situacions d'Aprenentatge (SA)
  ------------------------- ---------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  **Marc normatiu**         Introduïdes amb LOGSE i mantingudes amb LOMCE. En FP, les Instruccions d'inici de curs 25-26 de la GVA exigeixen UP.   La LOMLOE i la Llei de FP impulsen un model competencial i d'avaluació formativa que en altres etapes s'ha traduït en SA.
  **Estructura**            Seqüència tancada de continguts i activitats, orientada a objectius preestablerts.                                     Organització flexible i contextualitzada al voltant d'un repte o problema real.
  **Focus principal**       Objectius didàctics i criteris d'avaluació concrets, amb enfocament transmissiu.                                       Desenvolupament de competències específiques i clau a través de tasques significatives.
  **Metodologia**           Lineal, centrada en la transmissió i la repetició de continguts.                                                       Activa, col·laborativa i basada en la resolució de problemes i la interdisciplinarietat.
  **Avaluació**             Generalment sumativa, centrada en proves i resultats individuals.                                                      Formativa i contínua, vinculada al procés i a l'aplicació pràctica en contextos reals.
  **Finalitat educativa**   Adquisició ordenada de coneixements i habilitats concretes.                                                            Preparació integral per a la vida personal, social i professional mitjançant contextos aplicats.


# 20. Les programacions didàctiques dels mòduls i/o els projectes

Les programacions didàctiques concreten com s'imparteixen els mòduls professionals i, si escau, els projectes del cicle. S'elaboren d'acord amb el PCCF i amb les directrius de la comissió de coordinació pedagògica del centre, i serveixen de base per a les programacions d'aula.

::: {.admonition .note}
Marc normatiu

Tal com estableix l'article 9.2 del Decret 114/2025, de 29 de juliol, del Consell,/
les programacions didàctiques han d'incloure, com a mínim, els elements següents.
:::

## 1. Concepte i finalitat

La programació del mòdul ha de ser un document clar, concís i útil per a planificar l'activitat docent. Ha d'ajustar-se al que preveu el PCCF i donar resposta a: - La seqüència i organització dels resultats d'aprenentatge (RA) i dels criteris d'avaluació. - L'organització i temporització dels continguts, metodologies i recursos. - Les condicions d'impartició (presencial o semipresencial) i l'atenció a la diversitat.

La programació és única per a cada mòdul del cicle; la seua concreció operativa es reflectirà en les programacions d'aula de cada grup.

## 2. Contingut mínim de la programació didàctica del mòdul

-   Dades identificatives, marc normatiu i contextualització del mòdul.
-   Relació entre els estàndards de competència i els mòduls del cicle formatiu.
-   Contribució dels RA a les competències generals del títol.
-   Esquema general i seqüenciació de les unitats de programació.
-   Metodologia del procés d'ensenyança-aprenentatge, incloent enfocaments actius i treball per projectes.
-   Recursos (humans, materials i digitals).
-   Ús d'espais i equipaments.
-   Mesures d'atenció a la diversitat i suports personals.
-   Avaluació de l'aprenentatge: instruments, moments, pesos i recuperació.
-   Activitats complementàries i extraescolars vinculades al mòdul.
-   Criteris i procediments per a l'avaluació del desenvolupament de la programació i de la pràctica docent, així com els criteris de qualificació.
-   Qualsevol altre apartat que l'equip educatiu considere rellevant dins del PCCF.

::: {.admonition .tip}
Recomanacions de qualitat

-   Defineix indicadors mesurables per avaluar l'avenç dels RA.
-   Assegura coherència entre activitats, instruments d'avaluació i pesos.
-   Preveu adaptacions metodològiques i d'avaluació per a necessitats específiques.
-   Actualitza anualment la programació amb evidències
:::


