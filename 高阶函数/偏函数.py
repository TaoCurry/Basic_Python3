#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#导入functools模块,functools.partial()
#functools.partial(func, *args, **keywords)
import functools
int2 = functools.partial(int, base=8)       #八进制转十进制输出
int3 = functools.partial(int, base=16)      #十六进制转十进制输出
int4 = functools.partial(int, base=2)        #二进制转十进制输出
i = int2('12345')
j = int3('12345')
k = int4('1001011')
print('八进制转十进制的结果是：%5d' % i)
print('十六进制转十进制的结果是：%5d' % j)
print('二进制转十进制的结果是：%d' % k)