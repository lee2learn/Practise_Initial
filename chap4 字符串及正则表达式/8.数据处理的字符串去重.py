# coding:utf-8
s='helloworldhelloworldfafafaggaeewefs'
#(1)字符串的拼接及not in
new_s=''
for item in s:
    if item not in new_s:#判断s中每个字符在new_s中是否存在
        new_s+=item
print(new_s)

#(2)使用索引+not in +for
new_s2=''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2+=s[i]
print(new_s2)

#(3)通过集合去重+列表的排序
new_s3=set(s)#结果是集合类型
lst=list(new_s3)
lst.sort(key=s.index)#排序的关键字
print(lst)
print(''.join(lst))