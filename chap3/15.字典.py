# coding:utf-8
#字典没有索引，只能通过键值对，相当于用键代替索引
#字典是无序的
#字典和列表都是可变序列
#字典的键是不可变序列

#（1）直接使用｛｝创建
d={10:'cat',20:'dog',30:'pet',20:'zoo'} #key相同，值进行覆盖
print(d)

#zip函数的使用
lst1=[10,20,30,40]
lst2=['cat','dog','car','zoo']
zipobj=zip(lst1,lst2) #映射函数的结果是一个zip对象
#print(zipobj)
#print(list(zipobj))
d=dict(zipobj)
print(d)

#使用参数创建字典
d=dict(cat=10,dog=20)#注意事项，参数相当于变量，变量名不加引号
print(d)

t=(10,20,30)
print({t:10})

#lst=[10,20,30]
#print({lst:10}) 可变数据列表不可以做键