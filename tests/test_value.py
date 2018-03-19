#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import unittest

from vo import Value, ImmutableInstanceError

__author__ = 'Paweł Zadrożny'
__copyright__ = 'Copyright (c) 2017, Pawelzny'


class ValueTest(unittest.TestCase):
    def test_assign_kwargs(self):
        value = Value(test=True, text='Some text')

        self.assertTrue(value.test)
        self.assertEqual(value.text, 'Some text')
        self.assertEqual(value['text'], 'Some text')

    def test_equal(self):
        v1 = Value(text='first text', other_attr=1243)
        v2 = Value(other_attr=1243, text='first text')

        self.assertEqual(v1, v2)
        self.assertEqual(hash(v1), hash(v2))

    def test_not_equal(self):
        v1 = Value(text='first text', other_attr=1243, new_attr=True)
        v2 = Value(other_attr=1243, text='first text', new_attr=False)

        self.assertNotEqual(v1, v2)
        self.assertNotEqual(hash(v1), hash(v2))

    def test_to_dict(self):
        v = Value(text='first text', other_attr=1243)
        dump = v.to_dict()
        self.assertDictEqual(dump, {'text': 'first text', 'other_attr': 1243})

    def test_to_json(self):
        v = Value(text='first text', other_attr=1243)
        dump = v.to_json()
        self.assertIsInstance(dump, str)

        load = json.loads(dump)
        self.assertDictEqual(load, {'text': 'first text', 'other_attr': 1243})

    def test_to_bytes(self):
        v = Value(text='first text', other_attr=1243)
        dump = v.to_bytes()

        self.assertIsInstance(dump, bytes)
        self.assertEqual(dump, b'\'{"other_attr": 1243, "text": "first text"}\'')

    def test_modification_forbidden(self):
        v = Value(text='first text', other_attr=1243, new_attr=True)
        with self.assertRaises(ImmutableInstanceError):
            v.text = 'forbidden'

        with self.assertRaises(ImmutableInstanceError):
            v.something_new = 'forbidden'

        with self.assertRaises(ImmutableInstanceError):
            v['something_other'] = 'also forbidden'

    def test_delete_forbidden(self):
        v = Value(text='first text', other_attr=1243, new_attr=True)
        with self.assertRaises(ImmutableInstanceError):
            del v.text

        with self.assertRaises(ImmutableInstanceError):
            del v['other_attr']

    def test_value_contains_key(self):
        v = Value(text='first text', other_attr=1243, new_attr=True)
        self.assertIn('text', v)
        self.assertIn('other_attr', v)
        self.assertIn('new_attr', v)
        self.assertNotIn('forbidden', v)

    def test_repr(self):
        v = Value(first='first', second=2, is_true=True)
        self.assertEqual(repr(v), "Value(first='first', is_true=True, second=2)")
