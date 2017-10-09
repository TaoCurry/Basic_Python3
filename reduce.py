#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
from functools import reduce
def func1(s):
	return {'1':1,'2':2,'3':3,'4':4,'5':5}[s]
def func2(x,y):
	return 10*x + y
r = reduce(func2,map(func1,'1345'))
print(r)

#优化1.0
from functools import reduce
def str2int(s):
	def str2(s):
		return {'1':1,'2':2,'3':3,'4':4,'5':5}[s]
	def 2int(x,y):
		return 10*x + y
	return reduce(2int,map(str2,'1345'))

#优化2.0
from functools import reduce
def str2(s):
	return {'1':1,'2':2,'3':3,'4':4,'5':5}[s]
def 2int(s):
	reduce(lambda x,y: 10*x + y,map(str2,'1345'))
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return str.capitalize(name)

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# -*- coding: utf-8 -*-
from functools import reduce
def prod(L):
    def prod1(x,y):
        return x*y
    return reduce(prod1,[3, 5, 7, 9])
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
