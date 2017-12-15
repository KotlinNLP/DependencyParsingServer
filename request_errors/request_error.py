# -*- coding:utf-8 -*-

# -----
# -- IMPORT LIBRARIES
# -----

import abc


# -----
# -- CLASS
# -----

class RequestError:

    __metaclass__ = abc.ABCMeta

    @classmethod
    @abc.abstractproperty
    def name(cls):
        pass

    def __init__(self, data=None):
        self.data = data

    def to_dict(self):

        return {
            "error": {
                "type": self.name,
                "data": self.data
            }
        }
