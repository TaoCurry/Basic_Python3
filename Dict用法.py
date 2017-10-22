#!/usr/bin/env python 3
# -*- coding:utf-8 -*-
#dict.+Tab 即可显示所有dict的一些内建方法。 dict()是一个工厂函数，是一个类型。
# dict()函数根本不是一个函数，它是个类型，类似list/tuple/str一样。
#class dict(object) --> dict()只能添加一个对象
dict() #创建一个空字典。
dict((('a',　65),　('b',　66),　('c',　67))) #伪装为一个object。
dict(**kwargs)	#输入一个关键字参数
>>>d = dict(name='Curry', age=20)
>>>d
...d = {'name': 'Curry', 'age': 20}

dict.clear()    #clear()方法清除字典中的所有项目，是一个原地操作，没有返回值（返回None）
>>> d = dict([('name', 'Curry'), ('age', 20)])
>>> d1 = d.clear()
>>> d
...{}
>>>print(d1)
...None

dict.copy()
dict.get()
dict.items()  #
dict.keys()#返回dict中keys的值
dict.values()#返回dict中values的值
dict.pop()
dict.setdefault()   #If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
dict.update()    #update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). 

# 字典的格式化字符串, key为string
>>>phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3528'}
>>>'Cecil\s phone number is %(Cecil)s.' % phonebook
...'Cecil\s phone number is 3528.'
