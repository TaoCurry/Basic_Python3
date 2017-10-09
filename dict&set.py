#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#key-value hash值
#dict是一种映射。一一对应。
d = {'Micheal':95,'Curry':30,'MacGrady':1,'Kobe':24,'KD':35}#dict
d['Micheal']
d['Curry']
d['KLAY'] = 11		#通过使用key 往dict加入元素
d['KLAY']
#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Jack'] = 90
d['Jack']
d['Jack'] = 88
d['Jack']
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
'MacGrady' in d		#第一种方法
d.get('MacGrady')	#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
d.get('Haris',-1)
#注意：返回None的时候Python的交互式命令行不显示结果。
d.pop('KD')			#删除一个key

#Set集合	
s = set([1,2,3])		#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的
s = set([1,1,2,2,3,3])	#重复元素在set中自动被过滤
s.add(4)				#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果.
						#add() 方法接受单个可以是任何数据类型的参数，并将该值添加到集合之中。
s.update({})/s.update({},{})/s.update([])	#接受一个或多个集合作为参数，也接受list作为参数。
s.remove(4)				#通过remove(key)方法可以删除元素，只能单个删除。如果该值不在集合中，remove() 方法引发一个 KeyError 例外。
s.discard()				#单个删除。如果针对一个集合中不存在的值调用 discard() 方法，它不进行任何操作。不产生错误；只是一条空指令。
s.pop()					#从集合中删除某个值，并返回该值。然而，由于集合是无序的，并没有“最后一个”值的概念，因此无法控制删除的是哪一个值。它基本上是随机的。
						#当set中没有元素时，再次使用pop()将会提示KeyError
s1 = set([1,2,3])
s2 = set([2,3,4])
s1 & s2
s1 | s2					#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作.
#常见集合操作
union()					#union() 方法返回一个新集合，其中装着 在两个 集合中出现的元素。
intersection()			#intersection() 方法返回一个新集合，其中装着 同时 在两个集合中出现的所有元素。
difference()			
symmetric_difference()	#symmetric_difference() 方法返回一个新集合，其中装着所有只在其中一个集合中出现的元素。

b_set = {1,2,3,7,8,9,12,30}
c_set = {2,3,4,5,6,7,9,11,10}
b_set.union(c_set) == c_set.union(b_set)     			#b_set和c_set的并集
b_set.intersection(c_set) == c_set.intersection(b_set) 	#b_set和c_set的交集
b_set.difference(c_set) != c_set.difference(b_set)     	##difference() 方法返回的新集合中，装着所有在b_set出现但未在c_set中的元素。_set出现但未在b_set中的元素。


#Set
a_set = {1,2,3}
a_set.add(4)
a_set.update({5})
a_set.update({6,7,8})
a_set.update({6,7,8},{9,10,11})
a_set.remove(11)
a_set.remove(10)
a_set.pop(6)
a_set.discard(9)
a_set.discard(8)
a_set.clear()
a_set.update([1,2,3],[4,5,6])

#冻结集合 --> 无法往集合中添加或者删除元素。
frozenset()
