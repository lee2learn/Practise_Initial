# coding:utf-8
s={10,20,30}
#向集合中添加元素
s.add(100)
print(s)

#删除元素
s.remove(20)
print(s)

#清楚集合中所有元素
#s.clear()
#print(s,bool(s))

#遍历集合的元素
for item in s:
    print(item)

for index,item in enumerate(s,10):#10表示元素的序号，不是索引，可以自定义
    print(index,item)

#集合声称是
s={i for i in range(10)}
print(s)

s={i for i in range(10) if i%2}
print(s)