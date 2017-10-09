#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#从datetime模块中引入datetime类，两个datetime重名
from datetime import datetime
print(datetime.now())

#导入datetime这个包，没有具体说明是哪个类
import datetime
print(datetime.now())
#AttributeError: module 'datetime' has no attribute 'now'

#fix
import datetime
print(datetime.datetime.now())
#在datetime中找到datetime这个类，在使用now这个静态方法。

