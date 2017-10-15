#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#主要是需要弄清模块<Module>和类<class>的区别

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

一般来说，尽量避免使用from XX import XX，而是使用import语句
这是为了避免在程序中出现名称冲突，同时也是为了使程序更易读。
