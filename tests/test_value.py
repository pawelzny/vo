#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import unittest
from collections import OrderedDict
from itertools import zip_longest

from vo import ImmutableInstanceError, Value
from vo.value import _str_to_bytes

__author__ = 'Paweł Zadrożny'
__copyright__ = 'Copyright (c) 2017, Pawelzny'


class BasicsTest(unittest.TestCase):
    def test_create_empty_vo(self):
        value = Value()
        self.assertIsInstance(value, Value)

    # noinspection PyUnresolvedReferences
    def test_create_vo_with_attributes(self):
        value = Value(string='test string', integer=10, floating=2.3,
                      items=[1, 2, 3], dictionary={'test': True},
                      boolean=True, empty=None)

        self.assertEqual(value.string, 'test string')
        self.assertEqual(value.integer, 10)
        self.assertEqual(value.floating, 2.3)
        self.assertListEqual(value.items, [1, 2, 3])
        self.assertDictEqual(value.dictionary, {'test': True})
        self.assertEqual(value.boolean, True)
        self.assertIsNone(value.empty)

        self.assertEqual(value['string'], 'test string')
        self.assertEqual(value['integer'], 10)
        self.assertEqual(value['floating'], 2.3)
        self.assertListEqual(value['items'], [1, 2, 3])
        self.assertDictEqual(value['dictionary'], {'test': True})
        self.assertEqual(value['boolean'], True)
        self.assertIsNone(value['empty'])

        self.assertIs(value['string'], value.string)
        self.assertIs(value['integer'], value.integer)
        self.assertIs(value['floating'], value.floating)
        self.assertIs(value['items'], value.items)
        self.assertIs(value['dictionary'], value.dictionary)
        self.assertIs(value['boolean'], value.boolean)
        self.assertIs(value['empty'], value.empty)

    def test_compare_two_values(self):
        truthy_cases = (
            (Value(title='Test case'), Value(title='Test case')),
            (Value(title='Test case', test=True), Value(title='Test case', test=True)),
            (Value(test=12), Value(test=12)),
            (Value(), Value()),
            (Value(d={'first': 1, 'two': 2}), Value(d={'first': 1, 'two': 2})),
            (Value(v=Value(test=1)), Value(v=Value(test=1))),
            (Value(number=123.1), Value(number=123.1)),
            (Value(collection={1, 2, 3}), Value(collection={1, 2, 3})),
        )

        falsy_cases = (
            (Value(v=Value(test=1)), Value(v=Value(test=2))),
            (Value(title='Test case', test=True), Value(title='Test case')),
            (Value(title='Test cases'), Value(title='Test case')),
            (Value(num=1), Value(nu=1)),
            (Value(num=1), 1),
            (Value(num=1), {'num': 1}),
            (Value(v={1, 2, 3}), {1, 2, 3}),
            (Value(text='test'), 'Value(text=\'test\')'),
        )

        for truthy, falsy in zip_longest(truthy_cases, falsy_cases):
            if truthy is not None:
                self.assertEqual(truthy[0], truthy[1])
            if falsy is not None:
                self.assertNotEqual(falsy[0], falsy[1])

    def test_if_attribute_is_in_value(self):
        truthy_cases = (
            ('title', Value(title='test val')),
            ('number', Value(number=123)),
            ('test', Value(title='test val', test=True)),
            ('lang', Value(lang='python')),
            ('_checksum', Value(lang='python')),
        )

        falsy_cases = (
            ('java', Value()),
            ('test', Value(title='foo')),
            ('empty', Value(full='om nomnom')),
            (123, Value(number=123)),
            ('checksum', Value(full='om nomnom')),
        )

        for truthy, falsy in zip_longest(truthy_cases, falsy_cases):
            if truthy is not None:
                self.assertIn(truthy[0], truthy[1])
            if falsy is not None:
                self.assertNotIn(falsy[0], falsy[1])


class DataDumpTest(unittest.TestCase):
    def test_to_dict(self):
        truthy_cases = (
            (Value(title='some value'), {'title': 'some value'}),
            (Value(title='value', aaa='A!'), OrderedDict([('aaa', 'A!'), ('title', 'value')])),
            (Value(number=123, empty=None), {'empty': None, 'number': 123}),
            (Value(number=123, empty=None), OrderedDict([('empty', None), ('number', 123)])),
            (Value(number=Value(val=130)), OrderedDict([('number', OrderedDict([('val', 130)]))])),
            (Value(number=Value(val=Value(v=150))),
             OrderedDict([
                 ('number', OrderedDict([
                     ('val', OrderedDict([('v', 150)]))
                 ]))
             ])),
            (Value(c=2, a=1, b=Value(e=3, d=Value(f=4, g=5))),
             OrderedDict([
                 ('a', 1),
                 ('b', OrderedDict([
                     ('d', OrderedDict([
                         ('f', 4),
                         ('g', 5),
                     ])),
                     ('e', 3),
                 ])),
                 ('c', 2),
             ])),
        )

        falsy_cases = (
            (Value(number=123), OrderedDict([('empty', None), ('number', 123)])),
            (Value(number=123, empty=None), OrderedDict([('number', 123), ('empty', None)])),
            (Value(number=123, empty=None), {'empty': True, 'number': 123}),
            (Value(title='some value'), {'title': 'any value'}),
            (Value(c=2, a=1, b=Value(e=3, d=Value(f=4, g=5))),
             OrderedDict([
                 ('a', 1),
                 ('c', 2),
                 ('b', OrderedDict([
                     ('d', OrderedDict([
                         ('g', 5),
                         ('f', 4),
                     ])),
                     ('e', 3),
                 ])),
             ])),
        )

        for truthy, falsy in zip_longest(truthy_cases, falsy_cases):
            if truthy is not None:
                self.assertEqual(truthy[0].to_dict(), truthy[1])
            if falsy is not None:
                self.assertNotEqual(falsy[0].to_dict(), falsy[1])

    def test_to_json(self):
        truthy_cases = (
            (Value(title='some value'), {'title': 'some value'}),
            (Value(title='value', aaa='A!'), OrderedDict([('aaa', 'A!'), ('title', 'value')])),
            (Value(number=123, empty=None), OrderedDict([('empty', None), ('number', 123)])),
            (Value(number=Value(val=Value(v=150))),
             OrderedDict([
                 ('number', OrderedDict([
                     ('val', OrderedDict([('v', 150)])),
                 ])),
             ])),
        )

        falsy_cases = (
            (Value(title='some value'), {'title': 'any value'}),
            (Value(number=123), OrderedDict([('empty', None), ('number', 123)])),
            (Value(number=123, empty=None), OrderedDict([('number', 123), ('empty', None)])),
        )

        for truthy, falsy in zip_longest(truthy_cases, falsy_cases):
            if truthy is not None:
                self.assertEqual(truthy[0].to_json(), json.dumps(truthy[1]))
            if falsy is not None:
                self.assertNotEqual(falsy[0].to_json(), json.dumps(falsy[1]))

    def test_to_bytes(self):
        truthy_cases = (
            (Value(title='some value'), b'\'{"title": "some value"}\''),
            (Value(title='some value', aaa='A!'), b'\'{"aaa": "A!", "title": "some value"}\''),
            (Value(test=True, empty=None), b'\'{"empty": null, "test": true}\''),
            (Value(number=Value(val=130)), b'\'{"number": {"val": 130}}\''),
            (Value(number=Value(val=Value(v=150))),
             b'\'{"number": {"val": {"v": 150}}}\''),
            (Value(c=2, a=1, b=Value(e=3, d=Value(f=4, g=5))),
             b'\'{"a": 1, "b": {"d": {"f": 4, "g": 5}, "e": 3}, "c": 2}\'')
        )

        falsy_cases = (
            (Value(number=123, empty=None), b'\'{"empty": true, "number": 123}\''),
            (Value(title='some value'), b'\'{"title": "any value"}\''),
        )

        for truthy, falsy in zip_longest(truthy_cases, falsy_cases):
            if truthy is not None:
                self.assertEqual(truthy[0].to_bytes(), truthy[1])
            if falsy is not None:
                self.assertNotEqual(falsy[0].to_bytes(), falsy[1])


class ModificationExceptionTest(unittest.TestCase):
    def test_raise_on_adding_new_attribute(self):
        value = Value()

        with self.assertRaises(ImmutableInstanceError):
            value.new_attr = 'ha!'

        with self.assertRaises(ImmutableInstanceError):
            setattr(value, 'old_one', 'I am so old')

        with self.assertRaises(ImmutableInstanceError):
            value['some_attr'] = 1234

    def test_raise_on_change_existing_attribute(self):
        value = Value(title='some title', test=False)

        with self.assertRaises(ImmutableInstanceError):
            value.title = 'ha!'

        with self.assertRaises(ImmutableInstanceError):
            setattr(value, 'test', 'YES!')

        with self.assertRaises(ImmutableInstanceError):
            value['_checksum'] = 1234

    # noinspection PyUnresolvedReferences
    def test_raise_on_delete_attribute(self):
        value = Value(title='some title', test=False)

        with self.assertRaises(ImmutableInstanceError):
            del value.title

        with self.assertRaises(ImmutableInstanceError):
            delattr(value, 'test')

        with self.assertRaises(ImmutableInstanceError):
            del value['_checksum']

    def test_raise_when_assign_on_init(self):
        class Book(Value):
            def __init__(self, new_attr):
                self.new_attr = new_attr
                super().__init__()

        with self.assertRaises(ImmutableInstanceError):
            Book('this is my new attribute')


class DebugFeaturesTest(unittest.TestCase):
    def test_repr(self):
        truthy_cases = (
            (Value(text='first'), "Value(text='first')"),
            (Value(is_true=True, boolean=False), "Value(boolean=False, is_true=True)"),
        )

        falsy_cases = (
            (Value(is_true=True, boolean=False), "Value(is_true=True, boolean=False)"),
            (Value(first=123), "Value(first='123')"),
        )

        for truthy, falsy in zip_longest(truthy_cases, falsy_cases):
            if truthy is not None:
                self.assertEqual(str(repr(truthy[0])), truthy[1])
            if falsy is not None:
                self.assertNotEqual(str(repr(truthy[0])), falsy[1])

    def test_str(self):
        cases = (
            Value(title='some value'),
            Value(title='some value', aaa='A!'),
            Value(number=123, empty=None),
            Value(number=123.1234, boolean=False),
            Value(collection=[2, 2, 2]),
            Value(dictionary={'val': 123, 'what?': 'foo'}),
        )

        for case in cases:
            self.assertEqual(str(case), case.to_json())


class MiscTest(unittest.TestCase):
    def test_string_to_bytes(self):
        cases = (
            ("Some string", b'\'Some string\''),
            ("With numbers 1254", b'\'With numbers 1254\''),
            ("Unicode: zażółć gęślą jaźń", b'\'Unicode: za\xc5\xbc\xc3\xb3\xc5\x82\xc4\x87 '
                                           b'g\xc4\x99\xc5\x9bl\xc4\x85 ja\xc5\xba\xc5\x84\''),
            (344.32, b'344.32'),
            (True, b'True'),
            ({'whatever': 'it takes'}, b'{\'whatever\': \'it takes\'}'),
        )

        for case in cases:
            self.assertEqual(_str_to_bytes(case[0]), case[1])
