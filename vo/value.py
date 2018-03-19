#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import json
from collections import Hashable, OrderedDict
from copy import deepcopy

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


def str_to_bytes(string: str) -> bytes:
    return bytes(repr(string), 'utf-8')


class Value:
    """Basic implementation of DDD immutable Value Object.

    **Features:**

        * Two objects with exact values are considered the same
        * Objects are immutable (raise ImmutableInstanceError)

    :Example:

    .. code-block:: python

        >>> val = Value(name='Primary', price=10.35, currency='USD')
        >>> val.price
        10.35

        >>> val['currency']
        'USD'

    :param **kwargs: Any key=value pairs.
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

    def __repr__(self):
        cks_tpl = self.__checksum_tpl.format(self.__class__.__name__)
        values = ", ".join('{}={}'.format(key, repr(val))
                           for key, val in self.to_dict().items() if key != cks_tpl)
        return '{cls}({val})'.format(cls=self.__class__.__name__, val=values)

    def __str__(self):
        return '{} Value'.format(self.__class__.__name__)

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
        :rtype: dict
        """
        dct = OrderedDict(sorted(deepcopy(self.__dict__).items()))
        del dct[self.__checksum_tpl.format(self.__class__.__name__)]
        return dct

    def to_json(self) -> str:
        """Dump values to JSON.

        :return: JSON string.
        :rtype: str
        """
        return json.dumps(self.to_dict())

    def to_bytes(self) -> bytes:
        """Convert values to bytes.

        :return: byte string
        :rtype: bytes
        """
        return str_to_bytes(self.to_json())
