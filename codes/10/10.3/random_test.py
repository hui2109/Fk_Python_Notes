# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2020, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
import random

# 生成范围在0.0 <= x < 1.0之间的伪随机浮点数
print(random.random())
# 生成范围在2.5 <= x < 10.0之间的伪随机浮点数
print(random.uniform(2.5, 10.0))
# 生成呈指数分布的伪随机浮点数
print(random.expovariate(1 / 5))
# 生成从0到9的伪随机整数
print(random.randrange(10))
# 生成从0到100的随机偶数
print(random.randrange(0, 101, 2))
# 随机抽取一个元素
print(random.choice(['Python', 'Swift', 'Kotlin']))
book_list = ['Python', 'Swift', 'Kotlin']
# 对列表元素进行随机排列
random.shuffle(book_list)
print(book_list)
# 随机抽取4个独立的元素
print(random.sample([10, 20, 30, 40, 50], k=4))
