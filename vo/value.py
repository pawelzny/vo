#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import json
from collections import Hashable
from copy import deepcopy

__author__ = 'Paweł Zadrożny'
__copyright__ = 'Copyright (c) 2017, Pawelzny'


class ImmutableInstanceError(Exception):
    """Raised on any attempt to modify values in Value object."""

    message = 'Modification of Value instance is forbidden.'

    def __init__(self, message: str = None):
        super().__init__(message or self.message)


def str_to_bytes(string: str) -> bytes:
    return bytes(repr(string), 'utf-8')


class Value:
    """Basic implementation of DDD immutable Value Object.

    Value objects are consider same if they holds the same values.
    """

    __checksum = None
    __checksum_tpl = '_{}__checksum'

    def __init__(self, **kwargs):
        ck_sum = str_to_bytes('checksum:')
        for attr, value in sorted(kwargs.items()):
            object.__setattr__(self, attr, value)
            ck_sum += str_to_bytes(str(attr) + str(value))

        cks_tpl = self.__checksum_tpl.format(self.__class__.__name__)
        object.__setattr__(self, cks_tpl, hashlib.sha224(ck_sum).hexdigest())

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
        raise ImmutableInstanceError

    def __setitem__(self, key, value):
        raise ImmutableInstanceError

    def __delattr__(self, item):
        raise ImmutableInstanceError

    def __delitem__(self, key):
        raise ImmutableInstanceError

    def to_dict(self) -> dict:
        """Dump values to dict.

        :return: dict with values
        """
        dct = deepcopy(self.__dict__)
        del dct[self.__checksum_tpl.format(self.__class__.__name__)]
        return dct

    def to_json(self) -> str:
        """Dump values to JSON.

        :return: JSON string.
        """
        return json.dumps(self.to_dict())

    def to_bytes(self) -> bytes:
        """Convert values to bytes.

        :return: byte string
        """
        return str_to_bytes(self.to_json())
