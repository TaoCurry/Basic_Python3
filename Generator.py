#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
#Generator 生成器
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator.
g =(x for x in range(0,10))#可以通过next()函数获得generator的下一个返回值。
for n in g:
	print(n) #也可以通过循环获得generator的所有返回值。
#定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator	
def odd():
	print('step1')
	yield 1
	print('step2')
	yield 2
	print('step3')
	yield 3
	
#迭代求斐波拉契数列	
def fibo(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a+b
		n += 1
	return 'done'

#将上述函数改为generator
def fibo(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b			#print(b)
		a, b = b, a+b
		n += 1
	return 'done'
type(fibo)

#赋值语句:a , b = b, a+b 
#相当于：
t = (b, a+b)
a = t[0]
b = t[1]
#先计算右边的b, a+b,再将b赋值给a，a+b赋值给b。
