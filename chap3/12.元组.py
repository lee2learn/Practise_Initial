# coding:utf-8
#直接使用（）创建元组
t=('hello',[10,20,30],'python','world')
print(t)

#使用内置tuple()创建元组
t=tuple('helloworld')
print(t)
#序列也可以创建元组
t=tuple([10,20,30])
print(t)
#range也可以生成序列
t=tuple(range(1,10))
print(t)

#元组的相关操作
print('10在元组中是否存在：',(10 in t))
print('10在元组中不存在：',(10 not in t))
print('max:',max(t))
print('min:',min(t))
print('len:',len(t))
print('t.index',t.index(1))
print('t.count',t.count(3))

x=(10)
print(x,type(x))#x为int类型，而不是元组

age=(10,) #元组只有一个元素，逗号不能省
print(age, type(age))
#元组的删除
del age
print(age)