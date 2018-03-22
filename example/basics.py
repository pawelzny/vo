#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Paweł Zadrożny'
__copyright__ = 'Copyright (c) 2017, Pawelzny'


# noinspection PyUnusedLocal
def create_plain_value_object():
    from vo import Value

    book_ddd = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')
    book_tdd = Value(title='TDD', author='Life', price=99.98, currency='USD')
    return book_ddd, book_tdd


# noinspection PyUnresolvedReferences
def access_value_properties():
    from vo import Value

    book = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')

    assert book.title == 'DDD'
    assert book.author == book['author']
    assert book['price'] == 120.44
    return


def compare_different_value_objects():
    from vo import Value

    book_ddd = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')
    book_tdd = Value(title='TDD', author='Life', price=99.98, currency='USD')

    assert book_ddd != book_tdd
    return


def compare_similar_value_objects():
    from vo import Value

    book_ddd = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')
    book_clone = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')

    assert book_ddd == book_clone
    assert book_ddd is not book_clone
    return


def check_property_existence():
    from vo import Value

    book = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')

    assert 'title' in book
    assert 'publisher' not in book
