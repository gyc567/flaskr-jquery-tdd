# coding=utf-8
__author__ = 'YU'
import unittest


def fun(x):
    return x + 1

class TestStringMethods(unittest.TestCase):





    def test(self):
        self.assertEqual(fun(3), 4)

    def test_upper(self):
        foo='foo'.upper()
        self.assertEqual(foo, 'FOO')

    def test_addition(self):
        self.assertEqual(1+2, 3)

    def test_number(self):
        abc='abc'.capitalize()
        self.assertEqual(abc, 'Abc')

    def test_startwith(self):
        abc = 'abc'.startswith('a')
        self.assertEqual(abc, True)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()