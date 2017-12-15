# -*- coding:utf-8 -*-

# -----
# -- IMPORT LIBRARIES
# -----

import traceback

from tornado.web import HTTPError


# -----
# -- FUNCTIONS
# -----

def handle_request_exception(func):
    def func_wrapper(*args, **kwargs):

        self = args[0]

        try:
            return func(*args, **kwargs)

        except HTTPError as err:
            raise err

        except Exception:
            print "[Runtime Exception]"
            print traceback.format_exc()
            self.send_error(500)

    return func_wrapper


def check_arguments(*decorator_args):
    def function_decorator(func):
        def func_wrapper(*args, **kwargs):
            required_args = list(decorator_args)

            for arg in required_args:
                _check_argument(self=args[0], required_arg_name=arg)

            return func(*args, **kwargs)

        return func_wrapper

    return function_decorator


# -----
# -- PRIVATE FUNCTIONS
# -----

def _check_argument(self, required_arg_name):

    if self.get_arg(required_arg_name) is None:
        raise HTTPError(log_message="Missing '%s' parameter" % required_arg_name, status_code=400)
