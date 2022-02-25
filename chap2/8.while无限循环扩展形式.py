# coding:utf-8
# 1-100之间的累加和
s=0 #存储累加和
i=1 #(1)初始化变量
while i<=100: #(2)条件判断
    s+=i #(3)语句块
    #（4）改变变量
    i+=1
else:
    print('1-100之间的累加和：',s)

i=0 #统计循环执行的次数
while i<3:
    user_name=input('请输入您的用户名')
    pwd=input('请输入您对密码')
    #判断
    if user_name=='ysj' and pwd=='888888':
        print('系统正在登陆，请稍后')
        #改变循环条件，退出循环
        i=8
    else:
        if i<2:
            print('用户名或密码不正确，您还有',2-i,'次机会')
        i+=1
if i==3:
    print('对不起，三次均输入错误')