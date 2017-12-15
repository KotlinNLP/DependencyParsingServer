# -*- coding: utf-8 -*-

# -----
# -- IMPORT BASE LIBRARIES
# -----

import os
from xml.etree import ElementTree

# -----
# -- GLOBAL CONSTANTS
# -----

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

# -----
# -- PARAMETERS
# -----

CONFIG_FILENAME = os.path.join(SCRIPT_PATH, "config", "configuration.xml")


# -----
# -- CLASS
# -----

class Configuration(dict):

    def __init__(self):

        super(Configuration, self).__init__()

        xml_tree = ElementTree.parse(CONFIG_FILENAME)
        xml_root = xml_tree.getroot()

        self._xml_root = xml_root

        self._init_nlp_server()
        self._init_max_text_len()

    # ------------

    def _init_nlp_server(self):

        self['nlp_server'] = {
            "host": self._xml_root.find("nlp_server/host").text.strip(),
            "port": int(self._xml_root.find("nlp_server/port").text.strip()),
            "path": self._xml_root.find("nlp_server/path").text.strip()
        }

    # ------------

    def _init_max_text_len(self):

        self['max_text_len'] = int(self._xml_root.find("max_text_len").text.strip())
