from lxml import etree
import re
import zipfile


def extract_content_xml(ods_path, out_path="/tmp/content.xml"):
    """Extreu content.xml del fitxer ODS"""
    with zipfile.ZipFile(ods_path, "r") as z:
        with z.open("content.xml") as content:
            with open(out_path, "wb") as f:
                f.write(content.read())
    return out_path


def transform_sheet_to_html(xslt_path, content_xml_path, sheet_name):
    try:
        with open(xslt_path, "rb") as f:
            xslt_root = etree.XML(f.read())
        transform = etree.XSLT(xslt_root)

        # Alguns ODS contenen un `content.xml` que LibreOffice tolera però
        # que requerix mode de recuperació per a ser processat amb lxml.
        parser = etree.XMLParser(recover=True, huge_tree=True)
        xml_doc = etree.parse(content_xml_path, parser)
        html_tree = transform(xml_doc, sheet_name=etree.XSLT.strparam(sheet_name))

        return str(html_tree)

    except Exception as e:
        print(f"[XSLT ERROR - lxml] Full '{sheet_name}': {e}")
        return None


def process_markdown(markdown, ods_path, xslt_path):
    pattern = re.compile(r'\{([^}]+)\}(?:\s*"([^"]+)")?')
    content_xml_path = extract_content_xml(ods_path)

    def replace_match(match):
        sheet_name = match.group(1)
        title = match.group(2)
        html = transform_sheet_to_html(xslt_path, content_xml_path, sheet_name)
        if not html:
            return match.group(0)
        if title:
            return f"<h3>{title}</h3>\n{html}"
        return html

    return pattern.sub(replace_match, markdown)
