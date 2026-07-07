import os

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

from .transformer import process_markdown


class AddTablesPlugin(BasePlugin):
    config_scheme = [
        ("ods_path", config_options.Type(str)),
        ("xslt_path", config_options.Type(str, default="ods2html.xslt")),
    ]

    def on_config(self, config):
        project_dir = os.path.dirname(config.config_file_path)
        self.ods_path = os.path.join(project_dir, self.config["ods_path"])
        self.xslt_path = os.path.join(project_dir, self.config["xslt_path"])

        print(f"INFO    -  [add_tables] ods_path: {self.ods_path}")
        print(f"INFO    -  [add_tables] xslt_path: {self.xslt_path}")
        return config

    def on_page_markdown(self, markdown, **kwargs):
        return process_markdown(markdown, self.ods_path, self.xslt_path)
