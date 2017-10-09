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
 
 
 
