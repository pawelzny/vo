#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import json
from collections import Hashable, OrderedDict
from copy import deepcopy
from typing import Any

__author__ = 'Paweł Zadrożny'
__copyright__ = 'Copyright (c) 2017, Pawelzny'


class ImmutableInstanceError(Exception):
    """Raised on any attempt to modify values in Value object.

    :param message: Optional message.
    :type message: str
    """

    message = 'Modification of Value instance is forbidden.'

    def __init__(self, message: str = None):
        super().__init__(message or self.message)


def _str_to_bytes(string: str) -> bytes:
    return bytes(repr(string), 'utf-8')


class Value:
    """Basic implementation of DDD immutable Value Object.

    Implementation provides:

    * Immutability of once created object
    * Comparison of two objects
    * Conversion to other data types

    :param: Any ``key=value`` pairs.
    """

    _checksum = None

    def __init__(self, **kwargs):
        ck_sum = _str_to_bytes('checksum:')
        for attr, value in sorted(kwargs.items()):
            object.__setattr__(self, attr, value)
            ck_sum += _str_to_bytes(str(attr) + str(value))
        object.__setattr__(self, '_checksum', hashlib.sha224(ck_sum).hexdigest())

    def __repr__(self):
        values = ", ".join('{}={}'.format(key, repr(val))
                           for key, val in self.to_dict().items() if key != '_checksum')
        return '{cls}({val})'.format(cls=self.__class__.__name__, val=values)

    def __str__(self) -> str:
        return self.to_json()

    def __eq__(self, other: "Value") -> bool:
        try:
            return hash(self) == hash(other)
        except TypeError:
            # catch unhashable type
            return False

    def __ne__(self, other: "Value") -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> hash:
        return hash(self._checksum)

    def __contains__(self, item: Hashable) -> bool:
        return item in self.__dict__

    def __getitem__(self, item) -> Any:
        return self.__dict__[item]

    def __setattr__(self, name, value):
        raise ImmutableInstanceError

    def __setitem__(self, key, value):
        raise ImmutableInstanceError

    def __delattr__(self, item):
        raise ImmutableInstanceError

    def __delitem__(self, key):
        raise ImmutableInstanceError

    def to_dict(self) -> OrderedDict:
        """Dump all values to OrderedDict.

        All keys are sorted in ascending direction.
        Dump does not include hash and checksum.

        :return: dict with values
        :rtype: collections.OrderedDict
        """

        def dd(dct: dict) -> dict:
            dct = deepcopy(dct)

            try:
                del dct['_checksum']
            except KeyError:
                pass

            for key, val in dct.items():
                # If any of value is instance of Value dump it recursively
                if isinstance(val, Value):
                    dct[key] = dd(val.to_dict())
            return dct

        return OrderedDict(sorted(dd(self.__dict__).items()))

    def to_json(self) -> str:
        """Dump values to JSON.

        Feed for JSON comes from ``.to_dict()`` method.

        :return: JSON string.
        :rtype: str
        """
        return json.dumps(self.to_dict())

    def to_bytes(self) -> bytes:
        """Dump values to bytes.

        Feed for byte string comes from ``.to_json()`` method.

        :return: byte string
        :rtype: bytes
        """
        return _str_to_bytes(self.to_json())
