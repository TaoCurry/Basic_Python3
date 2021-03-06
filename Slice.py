#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
#Slice 切片/分片，利用索引提取序列。
L = list(range(100))
L[:]#复制
L[:10]#取前十个元素，索引10指向第十一个元素——这个元素并不存在。
L[::10]#L中每隔10个元素提取

T = (1,2,3,4,5,6)#Tuple也可以使用切片，返回的结果也是Tuple。
T[:]
T[:3]
T[3:]

L = [1,2,3,5,6,7]
L1 = [4]
L2 = L[:3] + L1 +L[3:]

进行切片的时候，开始和结束点需要进行指定，另外一个默认参数步长(step length)通常都是隐式设置的(step length = 1)。
  >>>numbers = list(range(11))
  >>>number1 = numbers[::1]
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  >>>number2 = numers[ : : -1]
     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # step length为负数时，从右往左进行分片操作 
  >>>number3 = numers[0:11:-2]
     [] 
    # 指定了从左往右进行切片，步长为负数时，返回空列表。
    # 当使用一个负数作为步长时，必须让开始索引大于结束索引
  >>>number4 = numbers[8:3:-2]
     [8, 6, 4]
