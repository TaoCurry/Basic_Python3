#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def pis_palindrome(n):
    s = str(n)      #将正整数转化为可迭代对象的str类型。
    x = 0
    while x < n:
        if s[0] == s[len(s)-1]:
            return int(s)
        x += 1
output = filter(pis_palindrome, range(1, 1000))
print(list(output))