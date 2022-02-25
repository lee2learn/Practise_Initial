# coding:utf-8
d={1001:'李梅',1002:'王华',1003:'张峰'}
print(d)
#向字典中添加数据
d[1004]='张丽丽'#直接使用赋值运算符=向字典中添加元素
print(d)

#获取字典中所有的key
keys=d.keys()#d.keys()结果是dict_keys，python中一种内部数据结构，用于表示字典的key
#如果希望更好的显示数据，可以使用list或者tuple转成相应的数据类型
print(keys)
print(list(keys))
print(tuple(keys))

#获取字典中所有的value
values=d.values() #dict_values
print(values)

#字典遍历时用到的一个方法items
items=d.items()
print(items)

lst=list(items)
print(lst)

#直接可以使用dict函数将列表转化为字典
d=dict(lst)
print(d)
#直接可以使用tuple函数将元组转化为字典
tup=tuple(items)
print(tup)
d1=dict(tup)
print(d1)

#使用pop函数删除
print(d.pop(1001))
print(d)
print(d.pop(1009,'不存在'))#如果键不存在，结果输出默认值

#随机删除
print(d.popitem())#先获取key-value对，再删除
print(d)

#清空字典中所有元素
d.clear()
print(d)

#python中一切皆对象，而每个对象都有一个布尔值
#空字典、空列表、空元组的布尔值为False
print(bool(d)) #空字典的bool值为False

