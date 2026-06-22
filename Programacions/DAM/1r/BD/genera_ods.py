#!/usr/bin/env python3
"""Genera l'ODS de dades de la programació de Bases de dades."""
from html import escape
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZIP_STORED, ZipFile

OUT = Path(__file__).with_name("PD_BD_DAM.ods")

ra = [
("RA1", "Reconeix els elements de les bases de dades, n'analitza les funcions i valora la utilitat dels sistemes gestors.",
"a) Sistemes lògics d'emmagatzematge.\nb) Tipus de BD segons el model.\nc) Tipus segons la ubicació.\nd) Utilitat dels SGBD.\ne) Elements d'un SGBD.\nf) Classificació dels SGBD.\ng) BD distribuïdes.\nh) Fragmentació.\ni) Protecció de dades.\nj) Big Data i intel·ligència de negoci."),
("RA2", "Crea bases de dades definint-ne l'estructura i les característiques dels elements segons el model relacional.",
"a) Format d'emmagatzematge.\nb) Taules i relacions.\nc) Tipus de dades.\nd) Camps clau.\ne) Restriccions.\nf) Vistes.\ng) Usuaris i privilegis.\nh) Assistents, eines gràfiques, DDL i DCL."),
("RA3", "Consulta la informació emmagatzemada en una base de dades emprant assistents, eines gràfiques i DML.",
"a) Eines i sentències.\nb) Consultes simples.\nc) Composicions internes.\nd) Composicions externes.\ne) Consultes resum.\nf) Subconsultes.\ng) Múltiples seleccions.\nh) Optimització."),
("RA4", "Modifica la informació emmagatzemada utilitzant assistents, eines gràfiques i DML.",
"a) Eines i sentències.\nb) Inserció, supressió i actualització.\nc) Inserció des de consultes.\nd) Guions complexos.\ne) Transaccions.\nf) Reversió de canvis.\ng) Bloquejos.\nh) Integritat i consistència."),
("RA5", "Desenvolupa procediments emmagatzemats avaluant i utilitzant les sentències del llenguatge incorporat en el SGBD.",
"a) Automatització.\nb) Execució de guions.\nc) Editors de guions.\nd) Guions de tasques.\ne) Funcions del SGBD.\nf) Procediments i funcions.\ng) Control de flux.\nh) Esdeveniments i disparadors.\ni) Cursors.\nj) Excepcions."),
("RA6", "Dissenya models relacionals normalitzats interpretant diagrames entitat/relació.",
"a) Eines gràfiques.\nb) Taules.\nc) Camps.\nd) Relacions.\ne) Camps clau.\nf) Regles d'integritat.\ng) Normalització.\nh) Restriccions no representables."),
("RA7", "Gestiona informació en bases de dades no relacionals, avaluant i utilitzant les possibilitats del sistema gestor.",
"a) Caracterització.\nb) Tipus de BD no relacionals.\nc) Elements.\nd) Formes de gestió.\ne) Eines del gestor."),
]

sheets = {
"qualificacions_professionals_DAM": [
["Codi", "Qualificació professional", "Unitats de competència relacionades"],
["IFC155_3", "Programació en llenguatges estructurats d'aplicacions de gestió", "UC0223_3; UC0226_3; UC0494_3"],
["IFC080_3", "Programació amb llenguatges orientats a objectes i bases de dades relacionals", "UC0223_3; UC0226_3; UC0227_3"],
],
"qualificacions_professionals_DAM_incompletes": [
["Codi", "Qualificació professional", "Unitat de competència"],
["IFC363_3", "Administració i programació en sistemes ERP-CRM", "UC1213_3"],
["IFC303_3", "Programació de sistemes informàtics", "UC0964_3"],
],
"contribucio_cp": [
["Mòdul", "Competències del títol a què contribueix"],
["0484 Bases de dades", "b), c), e), p) i t)"],
],
"contribucio_ra_cp": [
["RA", "Aportació competencial"],
["RA1", "Analitzar sistemes d'emmagatzematge i seleccionar SGBD."],
["RA2", "Implantar l'estructura física d'una base relacional."],
["RA3", "Consultar i optimitzar la recuperació d'informació."],
["RA4", "Mantindre dades amb integritat, consistència i transaccions."],
["RA5", "Automatitzar la lògica de dades al servidor."],
["RA6", "Modelar i normalitzar esquemes relacionals."],
["RA7", "Gestionar informació en sistemes no relacionals."],
],
"ra_ca": [["Resultat d'aprenentatge", "Criteris d'avaluació"]] + [[a+" — "+b, c] for a,b,c in ra],
"continguts": [
["RA", "Continguts"],
["RA1", "Emmagatzematge; tipus de BD; SGBD; distribució i fragmentació; protecció de dades; Big Data i BI."],
["RA2", "Model relacional; tipus; claus; restriccions; índexs; NULL; vistes; usuaris; DDL i DCL."],
["RA3", "Selecció, projecció i ordenació; operadors; agregació; joins; subconsultes; unions; optimització."],
["RA4", "INSERT, UPDATE i DELETE; integritat; edició amb subconsultes; transaccions; bloqueig i concurrència."],
["RA5", "Variables; funcions; control de flux; procediments; disparadors; esdeveniments; excepcions i cursors."],
["RA6", "Model E/R i ampliat; pas a relacional; restriccions semàntiques i normalització."],
["RA7", "Tipus i elements NoSQL; gestors i eines per gestionar la informació."],
],
"sequenciacio_up_ra": [
["UP", "RA principal", "Hores", "Pes"],
["UP1. Emmagatzematge de la informació", "RA1", "25", "15%"],
["UP2. Disseny E/R i normalització", "RA6", "20", "15%"],
["UP3. Bases de dades relacionals (DDL/DCL)", "RA2", "30", "20%"],
["UP4. Consultes SQL", "RA3", "30", "20%"],
["UP5. Tractament de dades i transaccions", "RA4", "15", "10%"],
["UP6. Programació de bases de dades", "RA5", "30", "15%"],
["UP7. Bases de dades no relacionals", "RA7", "10", "5%"],
["Total", "7 RA", "160", "100%"],
],
"sequenciacio_up_continguts": [
["UP", "Contingut nuclear"],
["UP1", "Fitxers, BD, SGBD, distribució, protecció de dades i Big Data."],
["UP2", "Diagrames E/R, transformació al model relacional i normalització."],
["UP3", "Taules, claus, restriccions, vistes, usuaris, DDL i DCL."],
["UP4", "Consultes simples i multitaula, agregació, subconsultes i optimització."],
["UP5", "Modificació, integritat, transaccions, bloqueig i concurrència."],
["UP6", "Procediments, funcions, disparadors, esdeveniments, cursors i excepcions."],
["UP7", "Models NoSQL i ús d'un SGBD no relacional."],
],
"temporalització": [
["Avaluació", "Unitats", "Hores orientatives"],
["1a", "UP1 i UP2", "45"],
["2a", "UP3 i UP4", "60"],
["3a", "UP5, UP6 i UP7", "55"],
],
"avaluacio": [
["RA", "Pes", "Evidències principals"],
["RA1", "15%", "Qüestionaris, activitats i prova teoricopràctica"],
["RA2", "20%", "Pràctiques DDL/DCL i projecte"],
["RA3", "20%", "Pràctiques i prova SQL"],
["RA4", "10%", "Pràctiques DML i transaccions"],
["RA5", "15%", "Guions i prova de programació al SGBD"],
["RA6", "15%", "Modelatge, normalització i defensa"],
["RA7", "5%", "Pràctica NoSQL"],
],
}

def cell(value):
    paragraphs = "".join(f"<text:p>{escape(x)}</text:p>" for x in str(value).split("\n"))
    return f'<table:table-cell office:value-type="string">{paragraphs}</table:table-cell>'

tables = []
for name, rows in sheets.items():
    body = "".join("<table:table-row>" + "".join(cell(v) for v in row) + "</table:table-row>" for row in rows)
    tables.append(f'<table:table table:name="{escape(name)}">{body}</table:table>')

content = f'''<?xml version="1.0" encoding="UTF-8"?>
<office:document-content xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
 xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0"
 xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
 office:version="1.3"><office:body><office:spreadsheet>{''.join(tables)}</office:spreadsheet></office:body></office:document-content>'''
manifest = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" manifest:version="1.3">
<manifest:file-entry manifest:full-path="/" manifest:media-type="application/vnd.oasis.opendocument.spreadsheet"/>
<manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>
</manifest:manifest>'''
with ZipFile(OUT, "w") as z:
    z.writestr("mimetype", "application/vnd.oasis.opendocument.spreadsheet", compress_type=ZIP_STORED)
    z.writestr("content.xml", content, compress_type=ZIP_DEFLATED)
    z.writestr("META-INF/manifest.xml", manifest, compress_type=ZIP_DEFLATED)
print(OUT)
