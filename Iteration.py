#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
#Iteration 迭代（遍历）
#python 中迭代是用for循环完成的。
#迭代方法：
#1.并行迭代：同时进行多个迭代； 2.按索引迭代； 3.翻转和排序迭代
d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)
	
#默认情况下，dictionary迭代的是key，
#如果要迭代value，可以使用 
for value in d.values():
	print(value)
	
#如果要同时迭代key和value -> 并行迭代
for key,value in d.items():
	print(key,value)

# 内置函数zip()就可以用来进行并行迭代
zip(*iterables) # Make an iterator that aggregates elements from each of the iterables.Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
def zip(*iterables):
    """This function returns a list of tuples, where the i-th tuple contains
    the i-th element from each of the argument sequences or iterables.

    :rtype: list[tuple]
    """
    return []
# example
>>> zip([1, 2, 3], range(10))
<zip object at 0x0000022423C85408>	 # zip class
>>> list(zip([1, 2, 3], range(10)))
[(1, 0), (2, 1), (3, 2)]

# Equivalent to 
>>> def zip(*iterables):
	# zip('ABCD', 'xy')　－－＞ Ax, By
	sentinel = object()
	iterators = [iter(it) for it in iterables]
	while iterators:
		result = []
		for it in iterators:
			elem = next(it, sentinel)
			if elem is sentinel:
				return
			result.append(elem)
		yield tuple(result)

		
>>> zip('ABC', 'xy')
<generator object zip at 0x000002A09F9815C8>
>>> list(zip('ABC', 'xy'))
[('A', 'x'), ('B', 'y')]

#通过collections模块的Iterable类型判断
form collections import Iterable
isinstance('abc',Iterable)
isinstance({},Iterable)
isinstance([],Iterable)
isinstance(123,Iterable)

#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身，-> 按索引迭代
for index , value in enumerate(['A','B','C']):
	print(index,value)

翻转和排序迭代
reversed(seq) 和 sorted(seq)方法
