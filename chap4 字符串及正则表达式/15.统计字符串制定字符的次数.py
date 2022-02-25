# coding:utf-8
s='HelloPython,HelloJava,hellophp'
word=input('请输入要统计的字符：')
print('{0}在{1}中一共出现了{2}次'.format(word.upper(),s,s.upper().count(word)))