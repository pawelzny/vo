#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict

__author__ = 'Paweł Zadrożny'
__copyright__ = 'Copyright (c) 2017, Pawelzny'


def dump_to_dict():
    from vo import Value

    book = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')
    dump = book.to_dict()

    assert isinstance(dump, OrderedDict)
    assert dump == OrderedDict([('author', 'Pythonista'), ('currency', 'USD'),
                                ('price', 120.44), ('title', 'DDD')])
    return


def dump_to_bytes():
    from vo import Value

    book = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')
    dump = book.to_bytes()

    assert isinstance(dump, bytes)
    assert dump == b'\'{"author": "Pythonista", "currency": "USD", ' \
                   b'"price": 120.44, "title": "DDD"}\''
    return


def dump_to_json():
    from vo import Value

    book = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')
    dump = book.to_json()

    assert isinstance(dump, str)
    assert dump == '{"author": "Pythonista", "currency": "USD", ' \
                   '"price": 120.44, "title": "DDD"}'
    return
