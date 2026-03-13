#!/usr/bin/env python3
"""
Script per generar el fitxer ODS per a la programació de PIA
Programació d'Intel·ligència Artificial
"""

import zipfile
import xml.etree.ElementTree as ET
from datetime import datetime

NS = {
    'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
    'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
}

def create_cell(value):
    """Crea una cel·la de text"""
    if value is None:
        value = ""
    cell = ET.Element('table:table-cell')
    p = ET.SubElement(cell, 'text:p')
    p.text = str(value)
    return cell

def create_row(values):
    """Crea una fila amb els valors donats"""
    row = ET.Element('table:table-row')
    for v in values:
        cell = create_cell(v)
        row.append(cell)
    return row

def create_table(name, headers, rows):
    """Crea una taula completa"""
    table = ET.Element('table:table')
    table.set('{urn:oasis:names:tc:opendocument:xmlns:table:1.0}name', name)
    
    # Header row
    header_row = ET.Element('table:table-row')
    for h in headers:
        cell = ET.Element('table:table-cell')
        p = ET.SubElement(cell, 'text:p')
        p.text = str(h)
        header_row.append(cell)
    table.append(header_row)
    
    # Data rows
    for row in rows:
        table.append(create_row(row))
    
    return table

# Dades del mòdul PIA segons el PDF
ra_ca_data = [
    ["RA1", "Caracteritza llenguatges de programació valorant la seva idoneïtat en el desenvolupament d'Intel·ligència Artificial"],
    ["RA1.a", "S'ha identificat l'estructura d'un programa informàtic."],
    ["RA1.b", "S'han valorat característiques en els llenguatges de programació adequades al tipus d'aplicacions que cal implementar."],
    ["RA1.c", "S'ha determinat el llenguatge de programació més apropiat per al desenvolupament de l'aplicació."],
    ["RA1.d", "S'han valorat característiques dels llenguatges de programació per al desenvolupament d'intel·ligència Artificial."],
    ["RA1.e", "S'ha determinat el llenguatge de programació més apropiat per al desenvolupament de l'aplicació d'Intel·ligència Artificial."],
    ["RA1.f", "S'han caracteritzat llenguatges de marcatge destacant la informació que contenen les etiquetes."],
    ["RA2", "Desenvolupa aplicacions d'intel·ligència artificial utilitzant entorns de modelatge."],
    ["RA2.a", "S'han avaluat plataformes d'intel·ligència artificial."],
    ["RA2.b", "S'han caracteritzat entorns de model d'aplicacions d'intel·ligència artificial."],
    ["RA2.c", "S'ha definit el model que es vol implementar segons el problema plantejat."],
    ["RA2.d", "S'ha implementat l'aplicació Intel·ligència Artificial."],
    ["RA2.e", "S'han avaluat els resultats obtinguts."],
    ["RA3", "Avalua les millores als negocis integrant convergència tecnològica."],
    ["RA3.a", "S'han identificat els avantatges que ofereix unificar processos, serveis, eines, mètodes i sectors."],
    ["RA3.b", "S'han identificat sistemes que faciliten la connexió tecnològica."],
    ["RA3.c", "S'han avaluat les característiques dels sistemes esmentats."],
    ["RA3.d", "S'ha avaluat com la convergència tecnològica aporta seguretat als negocis."],
    ["RA3.e", "S'ha avaluat la millora en la capacitat de presa de decisions estratègiques a un negoci connectat."],
    ["RA4", "Avalua models d'automatització industrial i de negoci relacionant-los amb els resultats esperats per les empreses."],
    ["RA4.a", "S'han identificat les noves estratègies corporatives i models de negoci a les empreses."],
    ["RA4.b", "S'ha definit la relació entre empreses i clients i el seu efecte en la manera com les empreses organitzen i gestionen els seus actius i recursos."],
    ["RA4.c", "S'han avaluat models d'automatització per als requeriments nous industrials i de negoci."],
    ["RA4.d", "S'ha avaluat la conveniència de cada model per aconseguir els resultats esperats per les empreses."],
]

continguts_data = [
    ["UD1", "Introducció a la programació", "Llenguatge de programació, Algorisme, Compilat vs Interpretat, Comparativa de llenguatges"],
    ["UD2", "Python", "Entorns de desenvolupament (Conda/Anaconda), Creació de projectes i entorns virtuals, Tipus bàsics i variables, Operadors, Estructures de control, Funcions, Llibreries, POO"],
    ["UD3", "Python aplicat al BD i IA", "Numpy, Matplotlib, Seaborn, Keras, Pandas"],
    ["UD4", "Programació d'aplicacions", "Frontend amb Flet (Calculadora/ToDo App), Docker amb MongoDB, Exportar dataset a BBDD, API-Rest, Backend amb Flask, Projecte integrador"],
    ["UD5", "Programació d'aplicacions d'IA", "Azure Cognitive Services, AWS, IBM Watson, Construcció d'aplicació amb models preentrenats"],
    ["UD6", "Convergència tecnològica", "Series temporals, Computer Vision, IA aplicat al llenguatge, App de passar llista"],
    ["UD7", "Automatització industrial", "Projectes"],
]

sequenciacio_data = [
    ["1a Avaluació", "UD1, UD2, UD3, UD4, UD5", "50%", "7h/setmana"],
    ["2a Avaluació", "UD5, UD6", "25%", "7h/setmana"],
    ["3a Avaluació", "UD7", "25%", "7h/setmana"],
]

temporalitzacio_data = [
    ["Unitat Didàctica", "Hores", "Setmanes"],
    ["UD1: Introducció a la programació", "10", "2"],
    ["UD2: Python", "35", "5"],
    ["UD3: Python aplicat al BD i IA", "30", "4"],
    ["UD4: Programació d'aplicacions", "45", "6"],
    ["UD5: Programació d'aplicacions d'IA", "35", "5"],
    ["UD6: Convergència tecnològica", "30", "4"],
    ["UD7: Automatització industrial", "25", "4"],
    ["Total", "210", "30"],
]

avaluacio_data = [
    ["Tipus", "Descripció", "Pes"],
    ["Avaluació continuada", "Seguiment del treball de l'alumne", "60%"],
    ["Proves de validació", "Examen al final de cada avaluació", "40%"],
    ["Condicionants", "Perdre dret avaluació continuada si faltes >15%", ""],
    ["Convocatòria final", "Prova 100% si no superada l'avaluació continuada", ""],
]

# Generar el fitxer ODS
output_path = 'PD_PIA.ods'

with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    # mimetype
    zf.writestr('mimetype', 'application/vnd.oasis.opendocument.spreadsheet')
    
    # content.xml
    root = ET.Element('office:document-content')
    root.set('xmlns:office', 'urn:oasis:names:tc:opendocument:xmlns:office:1.0')
    root.set('xmlns:table', 'urn:oasis:names:tc:opendocument:xmlns:table:1.0')
    root.set('xmlns:text', 'urn:oasis:names:tc:opendocument:xmlns:text:1.0')
    
    body = ET.SubElement(root, 'office:body')
    spreadsheet = ET.SubElement(body, 'office:spreadsheet')
    
    # Afegir taules
    spreadsheet.append(create_table('ra_ca', ['Codi', 'Descripció'], ra_ca_data))
    spreadsheet.append(create_table('continguts', ['UD', 'Titol', 'Continguts'], continguts_data))
    spreadsheet.append(create_table('sequenciacio_up_ra', ['Avaluació', 'UDs', 'Pes', 'Hores/setmana'], sequenciacio_data))
    spreadsheet.append(create_table('temporalització', temporalitzacio_data[0], temporalitzacio_data[1:]))
    spreadsheet.append(create_table('avaluacio', ['Tipus', 'Descripció', 'Pes'], avaluacio_data))
    
    content_xml = ET.tostring(root, encoding='unicode')
    zf.writestr('content.xml', content_xml)
    
    # styles.xml (basic)
    styles = '''<?xml version="1.0" encoding="UTF-8"?>
<office:document-styles xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0">
</office:document-styles>'''
    zf.writestr('styles.xml', styles)

print(f"Arxiu {output_path} generat correctament!")