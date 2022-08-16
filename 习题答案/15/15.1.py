# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com 公众号: fkbooks                  #
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
import ssl
from urllib.request import *

# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

with urlopen('https://fkjava.org/') as f:
    # 按字节读取数据
    data = f.read()
    # 将字节数据恢复成字符串
    print(data.decode('utf-8'))
