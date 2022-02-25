# coding:utf-8
#字符串的拼接
s1='hello'
s2='world'
#（1）使用+号拼接
print(s1+s2)#序列可以使用+

#（2）使用join方法进行拼接
print(''.join(['hello','world']))
#
print('*'.join(['hello','world','python','java','php']))
print('你好'.join(['hello','world','python','java','php']))

#(3)直接拼接
print('hello''world')
#(4)使用格式化字符串拼接
print('%s%s'%(s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))