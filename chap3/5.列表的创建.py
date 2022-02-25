# coding:utf-8
#直接使用[]创建
lst=['hello','world',99.8,100]
print(lst)

#可以使用内置的list函数创建列表
lst2=list('helloworld')
lst3=list(range(1,10,2))
print(lst2)
print(lst3)

#列表是序列中的一种，对序列操作的运算符，操作符，函数均可以使用
print(lst+lst2+lst3)
print(lst*3)
print(len(lst))
print(max(lst3))
print(min(lst3))
print(lst2.count('o')) #统计o的个数
print(lst2.index('o')) #o在列表lst2中第一次出现的位置

#列表的删除
lst4=[10,20,30]
print(lst4)
#删除列表lst4
del lst4
print(lst4)