#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
#List Comprehensions列表生成式
list range(1,11)#打印1-10的list
[x for x in range(1,11)]#把要生成的元素放前面
#打印1*1，2*2，3*3,...,10*10
L = []
for x in range(1,11)：
	L.append(x * x)
print(L)

[x * x for x in range(1,11)]#使用列表生成式
[x * x for x in range(1,101) if x % 2 == 0]#所有偶数的乘积
[m + n for m in 'ABC' for n in 'XYZ']#使用两层循环，可以生成全排列：
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

d = {'X':'A','Y':'B','Z':'C'}
[key + '=' + value for key,value in d.items()]
#['X=A','Y'='B','Z'='C']

L = ['HELLO','WORLD','APPLE','BMW']
[s.lower() for s in L]
#['hello', 'world', 'ibm', 'apple']

L = ['Hello', 'World', 18, 'Apple', None]#由于非字符串类型没有lower()方法
[s.lower() for s in L if isinstance(s,str) == True]
#['hello', 'world', 'apple']

带步长的列表生成式，步长表示每对相邻数字之间的差别
# example
>>> L = []
>>> for n in range(0, 10, 2):	# 步长为2
	L.append(n)
>>> L
[0, 2, 4, 6, 8]
# 
>>> from math import sqrt
>>> for n in range(99, 0, -1):	# 步长设置为负值进行反向迭代
	root = sqrt(n)
	if root == int(root):
		print(n)
		break
    else:	# 循环中加入else语句
	print('Didn\'t find it!')

	
81
