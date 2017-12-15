#!/usr/bin/env python
# -*- coding:utf-8 -*-

# -----
# -- IMPORT LIBRARIES
# -----

from argparse import ArgumentParser
from tornado.ioloop import IOLoop
from tornado.web import Application

from configuration import Configuration
from request_handlers.parse_handler import ParseHandler

# -----
# -- GLOBAL VARS
# -----

config = Configuration()


# -----
# -- FUNCTIONS
# -----

def get_arguments():

    arg_parser = ArgumentParser(description="Starts the Dependency Tree Server.")

    arg_parser.add_argument(
        "-t", "--host",
        default="127.0.0.1",
        help="the host of the server")

    arg_parser.add_argument(
        "-p", "--port",
        default=30000,
        type=int,
        help="the port listened from the server")

    args = arg_parser.parse_args()

    return args


def build_application():

    return Application([
        (ParseHandler.route, ParseHandler, {"config": config})
    ])


# -----
# -- MAIN
# -----

def main():

    args = get_arguments()

    build_application().listen(address=args.host, port=args.port)

    print "Running Dependency Tree Server on '%s:%s'" % (args.host, args.port)

    IOLoop.current().start()

# ------------

if __name__ == "__main__":
    main()
