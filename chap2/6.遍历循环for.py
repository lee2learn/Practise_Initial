# coding:utf-8
#遍历字符串
for i in 'hello':
    print(i)

# range()函数,产生一个[n,m]的整数序列，包含n，不包含m
for i in range(1,11):
    if i%2==0:
        print(i,'是偶数')
    #print(i)

#计算1-10之间的累加和
s=0 #用户存储累加和
for i in range(1,11):
    s+=i #相当于s=s+i
print(s)

print('----------------100-999之间的水仙花数----------------------')
'''
153
3*3*3+5*5*5+1*1*1=153
'''
for i in range(100,1000):
    sd=i%10 #获取个位上数字
    tens=i//10%10 #十位上的数字
    hundred=i//100 #百位上的数字
    if sd**3+tens**3+hundred**3==i:
        print(i)