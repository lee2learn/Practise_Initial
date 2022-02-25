# coding:utf-8
d={'hello':10,'world':20,'python':30}
# 访问字典元素
#（1）使用【key】
print(d['hello'])
#(2)使用d.get(key)
print(d.get('hello'))

#两种访问字典元素是有区别的,如果key不存在时，d[keg]报错，而适应get(key)可以指定默认值
#print(d['java']) #keyError:'java'
print(d.get('java')) #没有报错
print(d.get('java','不存在'))

#字典的遍历
for item in d.items():
    print(item) #得到key-value组成的元组

#在使用for循环遍历时，分别获取key和value
for key,value in d.items():
    print(key,value)