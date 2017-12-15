#!/usr/bin/env python
# -*- coding:utf-8 -*-

# -----
# -- IMPORT LIBRARIES
# -----

from utils.connection import curl_call


# -----
# -- CLASS
# -----

class NLPServerInterface:

    # -----
    # -- Constructor
    # -----

    def __init__(self, config):

        self._config = config

    # -----
    # -- Public Methods
    # -----

    def parse(self, text):
        return curl_call(
            url="%s:%d" % (self._config['host'], self._config['port']),
            path=self._config['path'],
            body={"text": text.encode("utf-8")},
            method="GET",
            response_type="json")
