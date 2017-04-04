#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eric.guo'

from ut_target import SplitZero, EqualToZero, Cat
import unittest


class SzTestCase(unittest.TestCase):
    def setUp(self):
        print "test start"

    def tearDown(self):
        print "test stop"

    def testSzBig(self):
        num = 10
        sz = SplitZero()
        self.assertEqual(sz.splitzero(num),
                         "num is bigger than zero")

    def testSzSmall(self):
        num = -10
        sz = SplitZero()
        self.assertEqual(sz.splitzero(num),
                         "num is smaller than zero")

    def testSzEqual(self):
        num = 0
        sz = SplitZero()
        self.assertRaises(EqualToZero, sz.splitzero, num)

    def testCat(self):
        cat=Cat()
        self.assertEqual(cat.catchRat(),"I catch a rat")


if __name__ == "__main__":
    unittest.main()