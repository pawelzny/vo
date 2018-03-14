#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from collections import Hashable
from copy import deepcopy

__author__ = 'Paweł Zadrożny'
__copyright__ = 'Copyright (c) 2017, Pawelzny'


class ValueModificationForbidden(Exception):
    def __init__(self, message: str = None):
        message = message or "Modification of existing Value is forbidden."
        super().__init__(message)


class Value:
    """
    Basic implementation of DDD invariant Value Object.
    Value objects are consider same if they holds the same values.
    """

    __checksum = None
    __checksum_tpl = '_{}__checksum'

    @staticmethod
    def to_bytes(string: str) -> bytes:
        return bytes(repr(string), 'utf-8')

    # noinspection PyPep8Naming
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        ck_sum = self.to_bytes('checksum:')
        for key, value in sorted(self.__dict__.items()):
            ck_sum += self.to_bytes(str(key) + str(value))

        cks_tpl = self.__checksum_tpl.format(self.__class__.__name__)
        self.__dict__[cks_tpl] = hashlib.sha224(ck_sum).hexdigest()

    def __eq__(self, other: "Value") -> bool:
        return self.__checksum == other.__checksum

    def __ne__(self, other: "Value") -> bool:
        return self.__checksum != other.__checksum

    def __hash__(self) -> hash:
        return hash(self.__checksum)

    def __contains__(self, item: Hashable):
        return item in self.__dict__

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setattr__(self, name, value):
        raise ValueModificationForbidden()

    def __setitem__(self, key, value):
        raise ValueModificationForbidden()

    def is_empty(self) -> bool:
        return len(self.__dict__) == 1

    def to_dict(self) -> dict:
        dct = deepcopy(self.__dict__)
        del dct[self.__checksum_tpl.format(self.__class__.__name__)]
        return dct
