#!/usr/bin/env python 3
# -*- coding：utf-8 -*-

abs(x)#x:integer|float|complex.x为复数时，返回其大小。

all(iterable)#如果迭代器里面的任何元素都非零,返回True;否则返回False.
def all (iterable):
	for element in iterable:
		if no element:
			return False
	return True		
	
any(iterable)#如果迭代器里面的任意元素都非零,返回True;否则返回False.
def any (iterable):
	for element in iterable:
		if not element:
			return False
	return True
 
 
 bin(x)#将整数转换为二进制字符串。
 
 bool(x)#返回一个布尔值，即True或False。
 
 hex(x)#将整数转换为以“0x”为前缀的小写十六进制字符串.
 
 oct(x)#将整数转换为以“0o”为前缀的小写八进制字符串.
 
 chr(x)#参数是0-0x10ffff(1,114,111),参数可以是二进制、八进制、十进制和十六进制。返回是当前整数对应的Unicode。
 
 ord(x)#给定一个表示一个Unicode字符的字符串，返回一个表示该字符的Unicode代码点的整数。
 
 pow(x,y[，z])#x的y次方，如果z存在，再进行取模操作，即pow(x, y) % z
 
 round(x[,y]) #返回浮点数x的四舍五入值, x:数值表达式; y:数值表达式，保留小数点后几位，如果没有y，默认保留整数。
   #round()返回结果和python版本有关
    >>>python2 round(0.5)
    1
   >>>python3 round(0.5) 
    0
   >>>python3 round(-0.5)
    0
   PythonDoc: if two multiples are equally close, rounding is done toward the even choice 如果距离两边一样远,朝向偶数一端.
>>>round(2.675, 2)
    2.67
round(2.675, 2) gives 2.67 instead of the expected 2.68. 
This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float.
[结果不是 2.68 主要是和浮点型的计算精度有关，计算机已经对计算结果进行了截断处理，所以机器处理的值会比 2.675这个实际值小一点。]	

	
 int(x)#把一个数、字符串转化成整形。如果为空，返回0；如果是数，返回x.__int__()；如果是浮点数，取整数部分.
 int()
 int(10)
 int(12.99)
 int(0.99)
 int(x,base = 2/8/10/16/)#base为2|8|10|16进制.
 int('0xff',base = 16)
 int('0o377',base = 8)
 int('0b11111111',base = 2)
 
 float(x)#把字符串或者一个数转化成浮点数.
 float('+123')
 float('   123445\n')
 float('1e-003')
 float('+1E6')
 float('-Infinity')
 float('NaN')
 
 str()#返回一个字符串版本的对象。如果没有提供对象，则返回空字符串。
 
 
 
