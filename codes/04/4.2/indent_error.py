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
s_age = input("请输入您的年龄:")
age = int(s_age)
if age > 20 :
    print("年龄已经大于20岁了")
print("20岁以上的人应该学会承担责任...")


# 定义变量b，并为其赋值
b = 5
if b > 4:
    # 如果b>4，则执行下面的条件执行体，只有一行代码作为代码块
    print("b大于4")
else:
    # 否则，执行下面的条件执行体，只有一行代码作为代码块
    b -= 1
# 对于下面代码而言，它已经不再是条件执行体的一部分，因此总会执行
print("b不大于4")

# 定义变量c，并为其赋值
c = 5
if c > 4:
    # 如果c>4，则执行下面的条件执行体，只有c-=1一行代码为条件执行体
    c -= 1
# 下面是一行普通代码，不属于条件执行体
print("c大于4")
# 此处的else将没有if语句，因此编译出错
else:
    # 否则，执行下面的条件执行体，只有一行代码作为代码块
    print("c不大于4")
