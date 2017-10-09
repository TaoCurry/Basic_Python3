#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def calc_sum(*args):
    n = 0
    for i in args:
        n = i + n
    return n
sum = calc_sum(1, 2, 3, 4, 5)
print(sum)

def calc_sum1(*args):
    def sum_():
        n = 0
        for i in args:
            n = i + n
        return n
    return sum_
sum1 = calc_sum1(1, 2, 3, 4, 5)  #调用cal_sum1时，返回的是一个函数。
print(sum1)    #<function calc_sum1.<locals>.sum at 0x0000025E64ACCEA0>
print(sum1())  #15--调用sum1()时，才真正返回结果。