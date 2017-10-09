#!/usr/bin/env python3
#-*- coding:utf-8 -*-
l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

l1 = list(map(lambda x: x * x, range(1, 10)))
print(l1)

f = lambda x: x*x
print(f(5))
