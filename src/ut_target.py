#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
__author__ = 'eric.guo'




class Teacher(object):
    def teach(self):
         return "Teach"




class Calculator(object):
    def addition(self,a,num):
        return a+num
    def figure(self,a,num):
        return a-num
    def ride(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b

# class Subtraction(object):
#     def figure(self,a,num):
#         return a-num
#
# class Multiplication(object):
#     def ride(self,a,b):
#         return a*b
#
# class Division(object):
#     def division(self,a,b):
#         return a/b

class Cat(object):
    def catchRat(self):
        return "I catch a rat"

