#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eric.guo'

from behave import *
from hamcrest import *
from CalculatorImpl import Calculator

import ast

def num(x):
   return ast.literal_eval(x)
   # return float(x) if '.' in x else int(x)


# 加法
@given('we have two number {number1},{number2}')
def have_number(context, number1, number2):
    context.number1 = int(number1)
    context.number2 = int(number2)


@when('we calc the plus')
def calc_plus(context):
    cal = Calculator()
    context.sum_number = cal.addition(context.number1, context.number2)


@then('we get the sum number {number}')
def get_number(context, number):
    context.expected_number = int(number)
    assert_that(context.sum_number, equal_to(context.expected_number), "Calc sum number: %d" % context.sum_number)


# 减法
@given('my have two number {number1},{number2}')
def my_number(context, number1, number2):
    context.number1 = int(number1)
    context.number2 = int(number2)


@when('my calc the minus')
def calc_minus(context):
    cal = Calculator()
    context.minus_number = cal.minus(context.number1, context.number2)


@then('my get the minus number {number}')
def got_number(context, number):
    context.expected_number = int(number)
    assert_that(context.minus_number, equal_to(context.expected_number), "Calc minus number: %d" % context.minus_number)


# 乘法
@given('you have two number {number1},{number2}')
def you_number(context, number1, number2):
    context.number1 = int(number1)
    context.number2 = int(number2)


@when('you calc the ride')
def calc_ride(context):
    cal = Calculator()
    context.ride_number = cal.ride(context.number1, context.number2)


@then('you get the ride number {number}')
def go_number(context, number):
    context.expected_number = int(number)
    assert_that(context.ride_number, equal_to(context.expected_number), "Calc ride number: %d" % context.ride_number)


# 除法
@given('he have two number {number1},{number2}')
def he_number(context, number1, number2):
    context.number1 = num(number1)
    context.number2 = num(number2)


@when('he calc the division')
def calc_division(context):
    cal = Calculator()
    context.division_number = cal.division(context.number1, context.number2)


@then('he get the division number {number}')
def gogo_number(context, number):
    context.expected_number = num(number)
    assert_that(context.division_number, equal_to(context.expected_number),"Calc division number: %d" % context.division_number)

