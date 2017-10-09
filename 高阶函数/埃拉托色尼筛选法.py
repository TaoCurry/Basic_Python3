#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def _is_odd():
    n = 1
    while True:
        n = n + 2       #筛选出奇数
        yield n
def _not_divisible(n):  #筛选函数
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _is_odd()      #初始序列，3开始的奇数
    while True:
        n = next(it)    #返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)
for n in primes():
    if n < 1000:
        print(n)
    else:
        break