#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
#Map && Reduce
#map(function, Iterable, ...) 
#接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。


#reduce(function, Iterable, initializer=None)
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数.
#reduce把结果继续和序列的下一个元素做累积计算。
reduce(f,[x1,x2,x3,x4]) = f(f((f(x1,x2),x3),x4))
#Python3 需要先调用functools模块，否则会报reduce没有定义的错误
from functools import reduce
