# coding:utf-8
user_name=input('请输入您的用户名：')
pwd=input('请输入您的密码：')
if user_name=='ysj' and pwd=='888888':
    print('登录成功')
else:
    print('用户名或密码不正确')


print('-----------------------')
score=eval(input('请输入您的成绩：'))
if score<0 or score>100:
    print('成绩无效')
else:
    print('您的成绩为:',score)