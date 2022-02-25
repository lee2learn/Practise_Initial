# coding:utf-8
number=eval(input('请输入你的6位中奖号码：'))
#使用if语句，语句后面有冒号
if number==987654:
    print('恭喜您中奖了')

if number!=987654:
    print('您未中奖')
print('-----------以上if判断的表达式，使用比较运算符，比较表达式---------------')

n=98
if n%2: #98%2的余数为0，0的布尔值为False,非0的布尔值为True
    print(n,'n为奇数')
if not n%2: # 98%2的余数为0，0的布尔值为False,结果为True
    print(n,'为偶数')
print('-------表示式也可以是一个单纯的变量-------')
flag=eval(input('请输入一个布尔类型的值：True 或 False'))
if flag: #flag是一个布尔类型的变量，值为True 或 False
    print('flag的值为True')

if not flag:
    print('flag的值为False')

print('----使用if语句时，如果语句块只有一句代码，可以将语句块直接卸载冒号的后面-----')
a=10
b=5
if a>b:max=a
print('a和b的最大值为：',max)


