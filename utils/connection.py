# -*- coding: utf-8 -*-

# -----
# -- IMPORT LIBRARIES
# -----

import ujson
import httplib
import urllib
import ssl


# -----
# -- EXCEPTIONS
# -----

class CurlError(RuntimeError):

    def __init__(self, response):

        self.status = response.status
        self.data = response.read()

        message = (
            "\nCall status " + str(self.status) +
            "\nReason: " + str(response.reason) +
            "\nData: " + str(self.data)
        )

        super(CurlError, self).__init__(message)


class InvalidProtocol(RuntimeError):
    pass


class InvalidMethod(RuntimeError):
    pass


class InvalidResponseType(RuntimeError):
    pass


# -----
# -- FUNCTIONS
# -----

def curl_call(url, body=None, method="GET", path="", protocol="HTTP", response_type="json", validate_cert=True):

    if response_type not in ("text", "json", "file"):
        raise InvalidResponseType(response_type)

    else:
        if response_type == "file":
            full_url = protocol.lower() + "://" + url + path
            return urllib.urlretrieve(full_url)

        else:
            if body is None:
                body = {}

            connection = _get_connection(url, protocol.lower(), validate_cert)

            _exec_request(connection, body, path, method.lower())

            return _get_response(connection, response_type)


def _get_connection(url, protocol, validate_cert):

    if protocol == "http":
        return httplib.HTTPConnection(url)

    elif protocol == "https":
        return httplib.HTTPSConnection(url, context=None if validate_cert else ssl.SSLContext(ssl.PROTOCOL_TLSv1))

    else:
        raise InvalidProtocol(protocol)


def _exec_request(connection, body, path, method):

    if method == "get":
        connection.request("GET", path + "?" + _encode_get_parameters(body))

    elif method == "post":
        connection.request("POST", path, ujson.dumps(body))

    else:
        raise InvalidMethod(method)


def _encode_get_parameters(params):
    return "&".join([name + "=" + urllib.quote(str(value)) for name, value in params.iteritems()])


def _get_response(connection, response_type):

    response = connection.getresponse()

    if response.status != 200:
        raise CurlError(response)

    elif response_type == "text":
        return response.read()

    elif response_type == "json":
        return ujson.decode(response.read())
