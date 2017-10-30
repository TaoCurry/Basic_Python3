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

dict.clear()    #clear()方法清除字典中的所有项目，是一个原地操作，没有返回值（或者说返回None）
>>> d = dict([('name', 'Curry'), ('age', 20)])
>>> d1 = d.clear()
>>> d
...{}
>>>print(d1)
...None

# example
>>>d = {}
>>>d1 = d
>>>d['name'] = 'Curry'
>>>d['age'] = 28
>>>d1
{'name': 'Curry', 'age': 28}
>>>d = {}
>>>d1
{'name': 'Curry', 'age': 28}

#
>>>d = {}
>>>d1 = d
>>>d['name'] = 'Curry'
>>>d['age'] = 28
>>>d1
{'name': 'Curry', 'age': 28}
>>>d.clear()    #原地操作改变了原来的dict
>>>d1
{}

dict.copy() copy方法返回一个具有相同键-值对的新字典（这个方法实现的是浅复制）\
# example
>>> x = {'name': 'Curry', 'age': 28, 'team': ['golden', 'state', 'warriros']}
>>> y = x.copy()
>>> y['name'] = 'KD'
>>> y['team'].remove('state')
>>> y
{'name': 'KD', 'age': 28, 'team': ['golden', 'warriros']}	
>>> x
{'name': 'Curry', 'age': 28, 'team': ['golden', 'warriros']} 	#替换某个值的时候，不改变原字典，修改了某个值的时候，原字典修改而不是替换。

# 深复制
from copy import deepcopy
>>> d = {}
>>> d['names'] = 'Curry'
>>> d['age'] = [20, 28]
>>> c = d.copy()
>>> d1 = deepcopy(d)
>>> d['age'].remove(20)
>>> c
{'names': 'Curry', 'age': [28]}
>>> d1
{'names': 'Curry', 'age': [20, 28]}

dict.get()	#Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError. 访问字典中的键，如果键位于字典中，则返回键的值，否则返回默认值。 如果没有给出默认值，那么它默认为None，因此该方法不会引发KeyError。默认的None可以自行修改
# example
>>> d
{}
>>> print(d.get('name'))
None
>>> print(d.get('name', 'N/A'))
N/A

dict.items()  # Return a new view of the dictionary’s items ((key, value) pairs).将字典中的键-值对以列表的形式返回，返回的时候键-值对顺序不固定。
# example
>>> x = {'name': 'Curry', 'age': 28, 'team': ['golden', 'state', 'warriros']}
>>> x.items()
dict_items([('name', 'Curry'), ('age', 28), ('team', ['golden', 'state', 'warriros'])])

dict.keys()		#返回dict中keys的值

dict.values()	#返回dict中values的值

dict.pop()		# If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised. 如果键在字典中，移除这个键并且返回键所对应的值。如果键不在字典中，抛出一个KeyError错误。
# example
>>> x = {'name': 'Curry', 'age': 28, 'team': ['golden', 'state', 'warriros']}
>>> x.pop('name')
'Curry'
>>> x
{'age': 28, 'team': ['golden', 'state', 'warriros']}
>>> x = {'name': 'Curry', 'age': 28, 'team': ['golden', 'state', 'warriros']}
>>> x.pop('LOL')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x.pop('LOL')
KeyError: 'LOL'
	
dict.popitem() 		# Remove and return an arbitrary (key, value) pair from the dictionary. 从原始字符串移除并返回任意一个键值对。
# example
>>> x = {'name': 'Curry', 'age': 28, 'team': ['golden', 'state', 'warriros']}
>>> x.popitem()
('team', ['golden', 'state', 'warriros'])
>>> x
{'name': 'Curry', 'age': 28}
>>> x.popitem()
('age', 28)
>>> x
{'name': 'Curry'}
>>> x.popitem()
('name', 'Curry')
>>> x
{}

dict.setdefault()   #If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None. 如果键存在字典中，返回对应的值。如果键不存在，则插入具有默认值(None)的键.类似dict.get()方法
# example
>>> x = {}
>>> x.setdefault('name', 'N/A')
'N/A'
>>> x
{'name': 'N\\A'}	# 更新了字典

>>> x['name'] = 'Curry'
>>> x.setdefault('name')
'Curry'
>>> x
{'name': 'Curry'}	# 原始字典键存在，不改变原字典。


dict.update()    #update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). 接受另外一个字典对象或者一个可迭代的键值对，组成新的字典。
# example
>>> x = {'name': 'Curry', 'age': 28, 'team': ['golden', 'state', 'warriros']}
>>> y = {'height': '6\'6'}
>>> x.update(y)
>>> x
{'name': 'Curry', 'age': 28, 'team': ['golden', 'state', 'warriros'], 'height': "6'6"}

dict.values() # Return a new view of the dictionary’s values. 以列表的形式返回字典中的值。
# example
>>> d = {}
>>> d[1] = 1
>>> d[2] = 2
>>> d[3] = 3
>>> d.values()
dict_values([1, 2, 3])

# 字典的格式化字符串, key为string
>>>phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3528'}
>>>'Cecil\s phone number is %(Cecil)s.' % phonebook
...'Cecil\s phone number is 3528.'
