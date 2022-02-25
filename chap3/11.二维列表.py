# coding:utf-8
lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',104,504],
    ['深圳',102,153]
]
print(lst)
#
for row in lst:#行
    for item in row:#列
        print(item,end='\t')
    print()#换行

#列表生成一个四行五列
lst2=[[j for j in range(5)] for i in range(4)]
print(lst2)
for row2 in lst2:
    for item2 in row2:
        print(item2,end='\\')
    print()