# coding:utf-8
#1.初始化变量
answer=input('今天上课吗？y/n')
while answer=='y': #2.条件判断
    print('好好学习，天天向上') #3.语句块
    #4.改变变量
    answer=input('今天上课吗？y/n')

# 1-100之间的累加和
s=0 #存储累加和
i=1 #(1)初始化变量
while i<=100: #(2)条件判断
    s+=i #(3)语句块
    #（4）改变变量
    i+=1
print('1-100之间的累加和：',s)