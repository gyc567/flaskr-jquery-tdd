#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eric.guo'

from ut_target import SplitZero, EqualToZero,Teacher,Calculator
import unittest



class SzTestCase(unittest.TestCase):
    def setUp(self):
        pass
        # print "test start"

    def tearDown(self):
        pass
        # print "test stop"

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

    def testFigure(self):
        a=1
        b=2
        ac=Calculator()
        self.assertEqual(ac.addition(a,b),3)

    def testMeasurement(self):
        a=1
        b=2
        ac=Calculator()
        self.assertEqual(ac.figure(a,b),-1)

    def testRide(self):
        a=1
        b=2
        ac=Calculator()
        self.assertEqual(ac.ride(a,b),2)

    def testDivision(self):
        a=1.0
        b=2.0
        ac=Calculator()
        self.assertEqual(ac.division(a,b),0.5)
        self.assertEqual(ac.division(5, 2), 2.5)
        self.assertEqual(ac.division(4, 3), 1.3333333333333333)

    def testTeacher(self):
        teacher=Teacher()
        self.assertEqual(teacher.teach(),'Teach')

    def testSzEqual(self):
        num = 0
        sz = SplitZero()
        self.assertRaises(EqualToZero, sz.splitzero, num)


if __name__ == "__main__":
    unittest.main()