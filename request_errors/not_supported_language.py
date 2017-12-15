# -*- coding:utf-8 -*-

# -----
# -- IMPORT LIBRARIES
# -----

from request_error import RequestError


# -----
# -- CLASS
# -----

class NotSupportedLanguage(RequestError):

    name = "NOT_SUPPORTED_LANGUAGE"

    def __init__(self, data):
        super(NotSupportedLanguage, self).__init__(data)
