# coding:utf-8
number=eval(input('请输入您的6位中奖号码'))
#if...else
if number==987654:
    print('恭喜您中奖了')
else:
    print('您未中奖')

print('以上代码还可以使用条件表达式简化')
#number==987654为True,
result='恭喜您中奖了'if number==987654 else'您未中本次大奖'
print(result)