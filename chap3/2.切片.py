# coding:utf-8
s='HelloWorld'
s1=s[0:5:1] #索引从0开始，到5结束，步长为1
print(s1)
#省略开始位置start,默认从0开始
print(s[:5:1])
#省略开始位置start,也省略步长
print(s[:5])
#省略结束位置end
print(s[0::1])
#省略结束位置和步长
print(s[5:])
#更换步长
print(s[0:5:2]) #从0开始，到5结束，步长为2
#省略开始和结束，只写步长
print(s[::3])
#步长可以为负数
print(s[::-1])