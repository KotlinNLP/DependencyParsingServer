# -*- coding:utf-8 -*-

# -----
# -- IMPORT LIBRARIES
# -----

import abc
import ujson

from tornado.web import RequestHandler

from request_decorators import handle_request_exception

# -----
# -- PARAMETERS
# -----

MAX_REQUEST_BODY = 2000


# -----
# -- CLASS
# -----

class ExtendedRequestHandler(RequestHandler):

    route = "/"

    def __init__(self, application, request):

        super(ExtendedRequestHandler, self).__init__(application, request)

    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        """Set default headers: handle CORS requests."""
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET")

    @handle_request_exception
    def get(self):
        self.write(self.process_request() + "\n")

    @handle_request_exception
    def post(self):
        self.write(self.process_request() + "\n")

    @abc.abstractmethod
    def process_request(self):
        pass

    def get_arg(self, name, default=None):

        if self.request.method == "GET":
            return self.get_argument(name=name, default=default)

        elif self.request.method == "POST":

            if len(self.request.body) > MAX_REQUEST_BODY:
                raise RuntimeError("Request body too long (%d)" % len(self.request.body))

            return self.get_argument(name=name, default=default)

        else:
            raise RuntimeError("Invalid request method: %s" % self.request.method)

    def jsonify(self, obj):

        pretty_print = self.get_argument(name="pretty", default=None) is not None

        return ujson.dumps(obj, indent=2) if pretty_print else ujson.dumps(obj)
