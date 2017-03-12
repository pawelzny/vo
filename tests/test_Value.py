import unittest

from vo.Value import Value


class ValueTest(unittest.TestCase):
    def test_assign_kwargs(self):
        value = Value(test=True, text="Some text")

        self.assertTrue(value.test)
        self.assertEqual('Some text', value.text)

    def test_equal(self):
        v1 = Value(text="first text", other_attr=1243)
        v2 = Value(other_attr=1243, text="first text")

        self.assertEqual(v1, v2)
        self.assertEqual(hash(v1), hash(v2))

        v1.new_attr = True
        v2.new_attr = False

        self.assertNotEqual(v1, v2)
        self.assertNotEqual(hash(v1), hash(v2))

    def test_setter(self):
        v1 = Value()
        v1.set(some_attr="I am some attribute")
        self.assertEqual('I am some attribute', v1.get('some_attr'))

        v1.set(some_attr="Now i am different")
        self.assertEqual("Now i am different", v1.some_attr)

    def test_getter(self):
        v1 = Value()
        self.assertEqual("Example string", v1.get('undefined_attr', "Example string"))
