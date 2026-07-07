import re
import os
import zipfile
import xml.etree.ElementTree as ET
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import subprocess
from .transformer import process_markdown

class AddTablesPlugin(BasePlugin):
    config_scheme = [
        ('ods_path', config_options.Type(str)),
        ('xslt_path', config_options.Type(str, default="ods2html.xslt")),
    ]

    def on_config(self, config):
        self.ods_path = os.path.join(os.path.dirname(config.config_file_path), self.config['ods_path'])
        self.xslt_path = os.path.join(os.path.dirname(config.config_file_path), self.config['xslt_path'])

        print(f"INFO    -  [add_tables] ods_path: {self.ods_path}")
        print(f"INFO    -  [add_tables] xslt_path: {self.xslt_path}")
        return config


    def on_page_markdown(self, markdown, **kwargs):
        return process_markdown(markdown, self.ods_path, self.xslt_path)

    def on_post_page(self, output_content, **kwargs):
        return output_content

    
        try:
            with zipfile.ZipFile(ods_path, "r") as z:
                with z.open("content.xml") as content:
                    tmp_content_path = "/tmp/content.xml"
                    with open(tmp_content_path, "wb") as f:
                        f.write(content.read())

            result = subprocess.run(
                ["xsltproc", "--stringparam", "sheet_name", sheet_name, xslt_path, tmp_content_path],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                print("ERROR    -  XSLT processing failed:")
                print(result.stderr)
                return None

            return result.stdout

        except Exception as e:
            print(f"ERROR    -  transform_sheet_to_html: {e}")
            return None