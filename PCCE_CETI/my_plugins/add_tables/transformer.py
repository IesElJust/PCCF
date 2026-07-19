from lxml import etree
import logging
import os
import re
import tempfile
import zipfile

logger = logging.getLogger("mkdocs.plugins.add_tables")

def extract_content_xml(ods_path):
    """Extreu content.xml del fitxer ODS"""
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xml")
    temp_file.close()
    with zipfile.ZipFile(ods_path, "r") as z:
        with z.open("content.xml") as content:
            with open(temp_file.name, "wb") as f:
                f.write(content.read())
    return temp_file.name


def transform_sheet_to_html(xslt_path, content_xml_path, sheet_name):
    try:
        # Carreguem XSLT
        with open(xslt_path, "rb") as f:
            xslt_root = etree.XML(f.read())
        transform = etree.XSLT(xslt_root)

        # Carreguem content.xml
        xml_doc = etree.parse(content_xml_path)

        # Apliquem la transformació amb paràmetre
        html_tree = transform(xml_doc, sheet_name=etree.XSLT.strparam(sheet_name))

        return str(html_tree)

    except Exception as e:
        logger.error("XSLT error en la fulla '%s': %s", sheet_name, e)
        return None

def process_markdown(markdown, ods_path, xslt_path):
    """
    Substitueix les marques {nom_full} en el markdown pel resultat de l'XSLT.
    """

    pattern = re.compile(r'\{([^}]+)\}(?:\s*"([^"]+)")?')
    content_xml_path = extract_content_xml(ods_path)

    def replace_match(match):
        sheet_name = match.group(1)
        title = match.group(2)
        html = transform_sheet_to_html(xslt_path, content_xml_path, sheet_name)
        if not html:
            return match.group(0)  # Deixem la marca original si hi ha error
        if title:
            return f"<h3>{title}</h3>\n{html}"
        return html

    try:
        return pattern.sub(replace_match, markdown)
    finally:
        os.unlink(content_xml_path)
