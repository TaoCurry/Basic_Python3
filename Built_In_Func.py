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



 
 
 
 
