# coding:utf-8
#创建一个空集合
phones=set()
#录入5位好友的姓名和手机号
for i in range(1,6):
    info=input('请输入第'+str(i)+'位好友的姓名与电话号码')
    #添加到集合中
    phones.add(info)


#遍历集合
for item in phones:
    print(item)