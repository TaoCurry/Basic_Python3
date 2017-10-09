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
