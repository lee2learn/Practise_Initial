# coding:utf-8
t=(i for i in range(1,4)) #结果是一个生成器对象
print(t)
#t=tuple(t)
#print(t)
#y=list(t)
#print(y)
#t=tuple(t)#必须通过转化才可以查看
#print(t)
#for item in t:#生成器对象直接可以遍历
  #  print(item)

#__next__()方法,取完了就没有了
print(t.__next__())
print(t.__next__())
print(t.__next__())

#t1=tuple(t)
#print(t1)
print('-----------------')
for item in t:
    print(item)