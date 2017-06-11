#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eric.guo'

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

plt.xlabel(u'性别')
plt.ylabel(u'人数')


plt.title(u"性别比例分析")
plt.xticks((0,1),(u'男',u'女'))
rect = plt.bar(left = (0,1),height = (1,0.5),width = 0.35,align="center")

plt.legend((rect,),(u"图例",))

plt.show()