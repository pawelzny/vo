#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from vo import Value, ValueModificationForbidden

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

    def test_is_empty(self):
        v1 = Value(text='first text', other_attr=1243, new_attr=True)
        v2 = Value()

        self.assertFalse(v1.is_empty())
        self.assertTrue(v2.is_empty())

    def test_modification_forbidden(self):
        v = Value(text='first text', other_attr=1243, new_attr=True)
        with self.assertRaises(ValueModificationForbidden):
            v.something_new = 'forbidden'

        with self.assertRaises(ValueModificationForbidden):
            v['something_other'] = 'also forbidden'

    def test_value_contains_key(self):
        v = Value(text='first text', other_attr=1243, new_attr=True)
        self.assertIn('text', v)
        self.assertIn('other_attr', v)
        self.assertIn('new_attr', v)
        self.assertNotIn('forbidden', v)
