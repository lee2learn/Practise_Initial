# coding:utf-8
'''
python中的集合和数学中集合概念是一致的
集成也适用{}创建
'''
#使用{}直接创建集合
s={10,20,30,40}
print(s)
#s={[10,20],[30,40]}
#print(s)
#s={([10,20],30),(40,)} #可变数列放在不可变数列中也不行，集合中不可以出现可变数列
s={(10,20,30),(30,)}
print(s)

s={}#创建的是字典还是集合？
print(type(s))#创建的是字典

#如何去创建一个空的集合
s=set()
print(s,type(s),bool())

#第二种创建集合的方式
s=set('helloworld') #集合中的元素不可以重复，集合可以实现元素的去重
s2=set([10,20,30])
s3=set(range(1,10))
print(s,s2,s3)

#集合属于序列中的一种
print('max',max(s3))
print('min:',min(s3))
print('len:',len(s3))

print('9在集合中是否存在',(9 in s3))
print('9在继承中不存在？',(9 not in s3))

#集合删除
del s3
print(s3)

