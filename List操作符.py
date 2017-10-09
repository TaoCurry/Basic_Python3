#！/usr/bin/env python 3
# -*- coding: utf-8 -*-
#List操作符
list1 = [123]
list2 = [456]
list1 > list2 #比较操作符
list3 = [123,456]
list4 = [456,123]
list3 > list4 #先比较第一个元素，如果判断完成，接下来没有比较的需要了。
list5 = list1 + list2 #+为连接符，连接两个list。
list1 * 5#list1元素重复出现三次。
123 not in list1
456 in list2
#list中常见的BIF
#1、count:计算list中某个元素重复出现的次数
list1.count(123)
#2、index:list中某个元素对应的索引位置，可以指定范围。
list1.index(123)
list1.index(123,3,7)
#3、reverse：反转list中的元素。
list6 = [23,30,45,99,35,3,6]
list6.reverse()
list6
#4、sort：将list中的元素从小到大排序
list6.sort()#list6.sort(reverse = False)
list6
#1、从大到小排序：先调用sort（）再调用reverse
#sort(func,key，reverse),sort自带三个参数，前两个为默认参数。1、func:指定排序的算法；2、key：和算法搭配的关键字；3、reverse = False
