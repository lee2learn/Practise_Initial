# coding:utf-8
import re
pattern=r'\d\.\d+'
s='I study Python3.10 every day Python2.10 I love you '
s2='4.10Python I study every day'
s3='I study Python every day'
match=re.search(pattern,s)

match2=re.search(pattern,s2)

match3=re.search(pattern,s3)

print(match)
print(match2)
print(match3)

print(match.group())
print(match2.group())