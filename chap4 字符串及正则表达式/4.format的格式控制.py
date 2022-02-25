# coding:utf-8
s='helloworld'
print('{0:*<20}'.format(s)) #字符串的显示宽度是20，左对齐，空白部分使用*填充
print('{0:*>20}'.format(s))#右对齐
print('{0:*^20}'.format(s))#居中对齐

print(s.center(20,'*'))#字符串的center方法实现居中效果

#,千位分隔符(只适用于整数和浮点数)
print('{0:,}'.format(987654321))
print('{0:,}'.format(8374823894.42342))

#浮点数小数部门的精度
print('{0:.2f}'.format(3.1415926))
#或者是字符串类型的最大显示长度
print('{0:.5}'.format('helloworld'))

#整数类型
a=432
print('{0:b}，{0:c},{0:d},{0:o},{0:x},{0:X}'.format(a))

#浮点数类型
b=3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))