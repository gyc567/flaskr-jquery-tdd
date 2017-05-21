#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eric.guo'

import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.baidu.com')
        self.assertIn('百度', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)