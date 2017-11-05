#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
def fibo(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a+b
		n += 1
	return 'done'
for n in fibo(10):
	print(n)

# Update 更简单的方法计算斐波拉契数列：
>>> fibs = [0, 1]
>>> for i in range(8):	 # 
	fibs.append(fibs[-2] + fibs[-1])

	
>>> fibs
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Update
>>> num = int(input('Please input Fibo\'s you want: '))
Please input Fibo's you want: 10
>>> for i in range(num - 2):
	fibs.append(fibs[-2] + fibs[-1])

	
>>> fibs
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
