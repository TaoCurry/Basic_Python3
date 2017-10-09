#!/usr/bin/env python 3
# -*- coding:utf-8 -*-
#dict.+Tab 即可显示所有dict的一些内建方法。 dict()是一个工厂函数，是一个类型。
#class dict(object) --> dict()只能添加一个对象
dict() #创建一个空字典。
dict((('a',65),('b',66),('c',67))) #伪装为一个object。
dict(**kwargs)	#输入一个关键字参数。

dict.clear()  
dict.copy()
dict.get()
dict.items()#
dict.keys()#返回dict中keys的值
dict.values()#返回dict中values的值
dict.pop()
dict.setdefault() #If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
dict.update()#update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). 

