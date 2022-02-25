# coding:utf-8
lst=[4,56,3,78,40,56,89]
print('原列表:',lst)
#排序，默认是升序
lst.sort() #lst.sort(reverse=False)
print('升序：',lst)

#排序，降序
lst.sort(reverse=True)
print('降序：',lst)

print('--------------------')
lst2=['banana','apple','Cat','Orange']
print('原列表：',lst2)
#升序排序，先排大写，后排小写
lst2.sort()
print('升序：',lst2)

#降序，先排小写，后排大写
lst2.sort(reverse=True)
print('降序：',lst2)

#忽略大小写进行比较
lst2.sort(key=str.lower)
print(lst2)