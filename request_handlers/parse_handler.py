# -*- coding:utf-8 -*-

# -----
# -- IMPORT LIBRARIES
# -----

import re
from utils.nlp_server_interface import NLPServerInterface
from utils.request_decorators import check_arguments
from utils.request_handler import ExtendedRequestHandler
from utils.connection import CurlError
from request_errors.not_supported_language import NotSupportedLanguage


# -----
# -- CLASS
# -----

class ParseHandler(ExtendedRequestHandler):

    route = "/parse"

    _not_supported_lang_prefix = "Language not supported"

    def __init__(self, application, request, config):

        super(ParseHandler, self).__init__(application, request)

        self.config = config
        self.nlp_server_interface = NLPServerInterface(config['nlp_server'])

    @check_arguments("text")
    def process_request(self):

        text = self.get_arg("text")

        if len(text) > self.config['max_text_len']:
            raise RuntimeError("Text too long (%d)" % len(text))

        try:
            response = self.nlp_server_interface.parse(text)
            return self.jsonify(self._convert_response(response))

        except CurlError as err:

            if err.status == 400 and err.data.startswith(self._not_supported_lang_prefix):
                return self.jsonify(NotSupportedLanguage(data={"lang": err.data.strip()[-2:]}).to_dict())
            else:
                raise err

    # -----
    # -- Private Methods
    # -----

    @classmethod
    def _convert_response(cls, nlp_server_response):

        return {
            "lang": nlp_server_response['lang'],
            "sentences": [
               {
                    "id": sentence_id,
                    "atoms": [cls._convert_token(token) for token in sentence['tokens']]
               }
               for sentence_id, sentence in enumerate(nlp_server_response['sentences'])
            ]
        }

    @classmethod
    def _convert_token(cls, token):

        head = token['dependency']['head']
        corefs = token['coReferences']

        return {
            "id": token['id'] + 1,
            "form": token['surface']['form'],
            "pos": " + ".join(map(lambda m: m['pos'], token['morphology'][0]['list'])) if token['morphology'] else None,
            "head": head + 1 if head is not None else 0,
            "deprel": " + ".join(map(lambda d: re.sub(r".*~", "", d), token['dependency']['relation'].upper().split("+"))),
            "corefs": [{"atomId": c['tokenId'] + 1, "sentenceId": c['sentenceId']} for c in corefs] if corefs else None,
            "sem": None
        }
