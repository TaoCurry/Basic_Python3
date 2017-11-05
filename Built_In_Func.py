#!/usr/bin/env python 3
# -*- coding：utf-8 -*-

1. abs(x)#x:integer|float|complex.x为复数时，返回其大小。

2. all(iterable)#如果迭代器里面的任何元素都非零,返回True;否则返回False.
	def all (iterable):
		for element in iterable:
			if no element:
				return False
		return True		
	
3. any(iterable)#如果迭代器里面的任意元素都非零,返回True;否则返回False.
	def any (iterable):
		for element in iterable:
			if not element:
				return False
		return True
 
 
 4. bin(x)#将整数转换为二进制字符串。
 
 5. bool(x)#返回一个布尔值，即True或False。None '' 0 ｛｝ [] ()都会fasle
 
 6. hex(x)#将整数转换为以“0x”为前缀的小写十六进制字符串.
 
 7. oct(x)#将整数转换为以“0o”为前缀的小写八进制字符串.
 
 8. chr(x)#参数是0-0x10ffff(1,114,111),参数可以是二进制、八进制、十进制和十六进制。返回是当前整数对应的Unicode编码。

 9. ord(x)#给定一个表示一个Unicode字符的字符串，返回一个表示该字符的Unicode代码点的整数。
 
10. pow(x,y[，z])#x的y次方，如果z存在，再进行取模操作，即pow(x, y) % z
 
11. round(number[, ndigits]) #根据给定的精度对数字进行四舍五入
    >>>round(42.3)
	42
    >>>round(15.7)
        16
    >>>round(15.668, 2)
        15.67
   #round()返回结果和python版本有关
    >>>python2 round(0.5)
    1
   >>>python3 round(0.5) 
    0
   >>>python3 round(-0.5)
    0
   PythonDoc: if two multiples are equally close, rounding is done toward the even choice 如果距离两边一样远,朝向偶数一端.
# especially:	
 	>>>round(2.675, 2)
    	   2.67
	round(2.675, 2) gives 2.67 instead of the expected 2.68. 
	This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float.
	[结果不是 2.68 主要是和浮点型的计算精度有关，计算机已经对计算结果进行了截断处理，所以机器处理的值会比 2.675这个实际值小一点。]	

12. repr(object) # 将对象转化为供解释器读取的形式,计算机内部读取的字符串格式
	>>>repr('hello')
	   "'hello'"
    repr实际上是一个函数，str/int是一种type class

13. str(object) #返回一个字符串版本的对象。如果没有提供对象，则返回空字符串。返回给用户显示的字符串对象
 	>>>str('123')
	   '123'

14. int(x[,base=])#把一个数、字符串转化成整形。如果为空，返回0；如果是数，返回x.__int__()；如果是浮点数，取整数部分.
  >>>type(int())
	class type
  >>>int(10)
  >>>int(12.99)
  >>>int(0.99)
 # especially
  int(x,base = 2/8/10/16/)#base为2|8|10|16进制.
  >>>int('0xff',base = 16)
	255
  >>>int('0o377',base = 8)
	255
  >>>int('0b11111111',base = 2)
 	255
	
15. float(x)#把字符串或者一个数转化成浮点数.
  >>>float('+123')
	123.0
  >>>float('   123445\n')
	12345.0
  >>>float('1e-003')
	0.001
  >>>float('+1E6')
	1000000.0
  >>>float('-Infinity') 
	-inf #负无限大
  >>>float('NaN')
	nan # not a number
	
16. ascii(object) # As repr(), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes. This generates a string similar to that returned by repr() in Python 2.和Python2中的repr()内置函数一样。

17. any(iterable)	# Return True if any element of the iterable is true. If the iterable is empty, return False.如果iterable中的任何元素都为true，则返回True。 如果iterable为空，则返回False。 主要是用来判断迭代对象是否都为空元素
# equal
>>> def any(iterable):
	for elements in iterable:
		if elements:
			return True
	return False

>>> any(())
False
>>> any([1, 2, 0])
True

18. all(iterable)	# Return True if all elements of the iterable are true (or if the iterable is empty). 如果iterable中的所有元素都为true（或者iterable为空），则返回True。
>>> def all(iterable):
	for elements in iterable:
		if not elements:
			return False
	return True

>>> all(())
True
>>> all([1])
True
>>> all([None])
False
>>> all([None, '', 0])
False

19. zip(*iterable) 	# 将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
# example
>>> def zip(*iterables):
	sentinel = object()
	iterators = [iter(it) for it in iterables]
	while iterators:
		result = []
		for it in iterators:
			elem = next(it, sentinel)
			if elem is sentinel:
				return
			result.append([elem])
		yield tuple(result)

		
>>> zip([1, 2, 3],['age', 'name', 'height'])
<generator object zip at 0x000002730800FBA0>
>>> list(zip([1, 2, 3],['age', 'name', 'height']))
[([1], ['age']), ([2], ['name']), ([3], ['height'])]
# example
>>> name = ['Curry', 'KD', 'Lebron']
>>> number = [30, 35, 23]
>>> zip(name, number)
<zip object at 0x000001D50EF054C8>
>>> list(zip(name, number))
[('Curry', 30), ('KD', 35), ('Lebron', 23)]

zip（）与*操作符结合可用于解压缩列表
# example
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
<zip object at 0x000001D7B3265608>
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zip(x, y))
>>> list(x2)
[1, 2, 3]
>>> list(y2)
[4, 5, 6]
>>> x == list(x2) and y == list(y2)
True
>>> 

20. eval((expression, globals=None, locals=None)   # The arguments are a string and optional globals and locals. If provided, globals must be a dictionary. If provided, locals can be any mapping object.执行一个字符串表达式，并返回表达式的值。参数是一个字符串和可选的全局作用域和局部作用域。 如果提供，globals全局作用域必须是一个字典。 如果提供，locals局部作用域可以是任何映射对象。
	 
# example
>>> x = 1
>>> eval('x + 1')   # 将字符串作为表达式计算，并且返回值
2

21. divmod(a, b)	#Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as (a // b, a % b). For floating point numbers the result is (q, a % b). 以两个（非复数）数字作为参数，并在使用整数除法时返回由它们的商和余数组成的一对数字。 混合操作数类型适用于二元算术运算符的规则。 对于整数，结果与（a // b，a % b）相同。对于浮点数参数，结果与(q, a % b)相同.

# example
>>> divmod(10, 3)
(3, 1)
>>> divmod(10.0, 3.0)
(3.0, 1.0)

22. enumerate(iterable, start=0)	# Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the values obtained from iterating over iterable. 返回一个枚举对象，iterable必须是一个序列，一个迭代器或者其他支持迭代的对象。由enumerate（）返回的迭代器的__next __（）方法返回一个元组，该元组包含一个计数（从start开始，默认为0）以及迭代获得的值。

# example
>>> l  = list(range(10))
>>> enumerate(l)
<enumerate object at 0x000002A09F98C798>	# enumerate obeject
>>> list(enumerate(l))
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]
>>> tuple(enumerate(l))
((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9))
>>> dict(enumerate(l))
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
		 
>>> list(enumerate(range(11), 1))
[(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10)]  
		 
# Equivalent to:
def enumerate(iterable, start=0):
		 n = start
		 for elem in iterable:
		 	yield n, elem
		 n += 1
		 
		 
>>> enumerate(range(10))
<generator object enumerate at 0x000002A09F981518>
>>> g = enumerate(range(10))
>>> next(g)		# 调用next()方法
(0, 0)
>>> next(g)
(1, 1)
>>> next(g)
(2, 2)
>>> next(g)
(3, 3)
>>> next(g)
(4, 4)
>>> next(g)
(5, 5)
>>> next(g)
(6, 6)
>>> next(g)
(7, 7)
>>> next(g)
(8, 8)
>>> next(g)
(9, 9)
>>> next(g)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    next(g)
StopIteration
		 
23. frozenset([iterable]) #Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class. 返回一个新的冻结对象，可选的元素来自iterable。 frozenset是一个内置的类。

# example
>>> frozenset([1, 2, 3])
frozenset({1, 2, 3})	# frozenset object
>>> frozenset('asdsd')
frozenset({'d', 'a', 's'})	#		 

24. id(object)	 # Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value. 以整数形式返回对象的内存地址.在整个对象的生命周期中保证这个对象是独一无二的。两个具有非重叠生命周期的对象可能具有相同的id（）值。

 # example
>>> id(frozenset('asdsd'))
2888895493288
>>> id(g)
2888895567040

25. filter(function, iterable)	#Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. 接受一个函数和一个可迭代对象,将可迭代对象中的每个元素传入函数中执行,如果函数返回值为True，就保留这个元素。
filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) 		 

# example
>>> def is_odd(n):
	return n % 2 ==1

>>> filter(is_odd, list(range(11)))
<filter object at 0x000002A09F984780>	
# filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item))
>>> list(filter(is_odd, list(range(11))))
[1, 3, 5, 7, 9]
		 

		 
