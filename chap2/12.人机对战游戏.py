# coding:utf-8
import random
player_store=0
computer_store=0
print('''
* * * * * * *欢迎来到4399游戏平台* * * * * * *
            石头  剪刀  布
* * * * * * * * * * * * * * * * * * * * * * *
''')
player_name=input('请输入玩家姓名：')
print('1.貂蝉 2.曹操 3.诸葛亮')
choice=eval(input('请输入电脑角色：'))
if choice==1:
    computer_name='貂蝉'
elif choice==2:
    computer_name='曹操'
elif choice == 3:
    computer_name='诸葛亮'
else:
    computer_name='匿名'
print(player_name,'VS',computer_name)
while True:
    #玩家出拳
    player_first=eval(input('-------------请出拳：1.石头 2.剪刀 3.布--------\n'))
    if player_first==1:
        player_first_name='石头'
    elif player_first==2:
        player_first_name='剪刀'
    elif player_first==3:
        player_first_name='布'
    else:
        player_first_name='石头'
        player_first=1
    #电脑角色出拳
    computer_first=random.randint(1, 3)
    if computer_first==1:
        computer_first_name='石头'
    elif computer_first==2:
        computer_first_name='剪刀'
    else:
        computer_first_name='布'
    print(player_name,'出拳：',player_first_name)
    print(computer_name,'出拳：',computer_first_name)
    if player_first==computer_first:
        print('平局')
    elif player_first==1 and computer_first==2 or player_first==2 and computer_first==3 or player_first==3 and computer_first==1:
        print('玩家：',player_name,'胜')
        player_store+=1
    else:
        print('电脑：',computer_name,'胜')
        computer_store+=1
    answer=input('再来一局不？y/n')
    if answer!='y':
        break

print('--------------------------------------------------')
print(player_name,player_store)
print(computer_name,computer_store)
print('--------------------------------------------------')
if player_store==computer_store:
    print('平局')
elif player_store>computer_store:
    print(player_name,'胜利')
else:
    print(computer_name,'胜利')