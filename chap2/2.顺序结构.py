# coding:utf-8
name='张三'#将张三赋值给变量name
age=20

a=b=c=d=100 #同时赋值100给abcd,链式赋值
name1,age1='李四',22
print(name,age)
print(name1,age1)
[name2,age2]=['王五',30]
print(name2,age2)
#字符串分解赋值
a,b,c,d='room'
print(a,b,c,d)
#扩展字符串解包赋值
a,*b='room'
print(a)
print(b)
print('------------')
name=input('请输入您的姓名:')
age=eval(input('请输入您的年龄：'))
lucky_number=eval(input('请输入您的幸运数字：'))
print('姓名：',name)
print('年龄',age)
print('幸运数字：',lucky_number)