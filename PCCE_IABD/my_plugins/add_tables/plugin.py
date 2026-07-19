import logging
import os

from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

from .transformer import process_markdown

logger = logging.getLogger("mkdocs.plugins.add_tables")

class AddTablesPlugin(BasePlugin):
    config_scheme = [
        ('ods_path', config_options.Type(str)),
        ('xslt_path', config_options.Type(str, default="ods2html.xslt")),
    ]

    def on_config(self, config):
        self.ods_path = os.path.join(os.path.dirname(config.config_file_path), self.config['ods_path'])
        self.xslt_path = os.path.join(os.path.dirname(config.config_file_path), self.config['xslt_path'])

        logger.info("ods_path: %s", self.ods_path)
        logger.info("xslt_path: %s", self.xslt_path)
        return config


    def on_page_markdown(self, markdown, **kwargs):
        return process_markdown(markdown, self.ods_path, self.xslt_path)

    def on_post_page(self, output_content, **kwargs):
        return output_content
