# coding:utf-8
#创建字典，用于存储车票的信息，使用车次做key，使用其他信息做value
dict_ticket={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8917':['北京南-天津西','18:20','19:19','00:39'],
    'G203':['北京南-天津南','18:35','19:09','00:34'],
}
print('车次   出发站-到达站   出发时间   到达间隔   历时时长')
#遍历字典中的元素
for key in dict_ticket.keys():
    print(key,end='   ')#为什么不换行，因为车次和车次信息在一行输出
    #遍历车次的详细信息，是一个列表
    for item in dict_ticket.get(key):#根据Key获取值，dict_ticket(key)
        print(item,end='   ')


    #换行
    print()

#输入用户的购票车次
train_no=input('请输入要购买的车次：')
#根据键获取值
info=dict_ticket.get(train_no,'车次不存在')#info表示车次信息
#判断车次是否存在
if info!='车次不存在':
    person=input('请输入乘车人，如果是多位乘车人使用逗号分隔：')
    #获取车次的出发站-到达站，还有出发时间
    s=info[0]+'   '+info[1]+'开'
    print('您已购买了'+train_no+' '+s+'请'+person+'尽快换取纸质车票。【忒路客服】')
else:
    print(info)
