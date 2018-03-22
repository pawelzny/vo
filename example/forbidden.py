#!/usr/bin/env python
# -*- coding: utf-8 -*-
from vo import ImmutableInstanceError

__author__ = 'Paweł Zadrożny'
__copyright__ = 'Copyright (c) 2017, Pawelzny'


def property_modification_forbidden():
    from vo import Value

    book = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')
    all_good = True

    try:
        book.title = 'BDD > DDD'  # or book['title'] = 'SPAM'
    except ImmutableInstanceError:
        all_good = False

    assert all_good is False
    assert book.title == 'DDD'
    return


def adding_new_property_forbidden():
    from vo import Value

    book = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')
    all_good = True

    try:
        book.publisher = 'SPAM'  # or book['publisher'] = 'SPAM'
    except ImmutableInstanceError:
        all_good = False

    assert all_good is False
    assert 'publisher' not in book
    return


def property_deletion_forbidden():
    from vo import Value

    book = Value(title='DDD', author='Pythonista', price=120.44, currency='USD')
    all_good = True

    try:
        del book.title  # or del book['title']
    except ImmutableInstanceError:
        all_good = False

    assert all_good is False
    assert 'title' in book
    return
