# coding:utf-8
s='helloworld'
print('e在helloworld中存在吗？',('e'in s))
print('v在helloworld中存在吗？',('v'in s))

print('e不在helloworld中存在吗？',('e'not in s))
print('v不在helloworld中存在吗？',('v'not in s))
#内置的函数
print('len():',len(s))
print('max()',max(s))
print('min()',min(s))

#序列对象的方法， 使用序列的名称，打点调用
print('s.index()',s.index('o')) #o第一次出现的位置是索引4的位置
print('s.count()',s.count('o'))