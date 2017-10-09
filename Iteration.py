#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
#Iteration 迭代（遍历）
#python 中迭代是用for循环完成的。
d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)
	
#默认情况下，dictionary迭代的是key，
#如果要迭代value，可以使用 
for value in d.values():
	print(value)
	
#如果要同时迭代key和value
for key,value in d.items():
	print(key,value)
	
#通过collections模块的Iterable类型判断
form collections import Iterable
isinstance('abc',Iterable)
isinstance({},Iterable)
isinstance([],Iterable)
isinstance(123,Iterable)

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for index , value in enumerate(['A','B','C']):
	print(index,value)