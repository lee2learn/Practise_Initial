# coding:utf-8
lst=['hello','world','python']
print('原列表:',lst,id(lst)) #id为列表的内存地址

#新增元素的操作
lst.append('sql')
print('增加元素之后',lst,id(lst))

#使用insert(index,x)在指定的位置上插入元素
lst.insert(1,100)
print(lst)

#列表元素的删除操作
lst.remove('world')
print('删除元素之后的列表',lst,id(lst))

#使用pop(index)根据索引移出元素，先将元素取出，再将元素删除
print(lst.pop(1))
print(lst)

#清除列表中的所有元素
#lst.clear()
#print(lst,id(lst))

#列表反向
lst.reverse()
print(lst)
print(lst.reverse())

#列表的拷贝，将产生一个新的列表对象
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#列表元素的修改
#根据索引进行修改元素
lst[1]='mysql'
print(lst)