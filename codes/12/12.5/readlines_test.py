# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
# 指定使用utf-8字符集读取文件内容
f = open("readlines_test.py", 'r', True, 'utf-8')
# 使用readlines()读取所有行，返回所有行组成的列表
for l in f.readlines():
    print(l, end='')
f.close()