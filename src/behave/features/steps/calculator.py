#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eric.guo'

from behave import *
from hamcrest import *


class Calculator(object):
    def addition(self,a,num):
        return a+num
    def figure(self,a,num):
        return a-num
    def ride(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b




@given('we have two number {number1},{number2}')
def have_number(context, number1,number2):
    context.number1 = int(number1)
    context.number2 = int(number2)


@when('we calc the plus')
def calc_plus(context):
     cal=Calculator()
     context.sum_number = cal.addition(context.number1,context.number2)




@then('we get the sum number {number}')
def get_number(context, number):
    context.expected_number = int(number)
    assert_that(context.sum_number, equal_to(context.expected_number), "Calc sum number: %d" % context.sum_number)