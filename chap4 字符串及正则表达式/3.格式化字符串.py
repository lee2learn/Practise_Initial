# coding:utf-8
#（1）使用占位符进行格式化
name='马冬梅'
age=18
score=98.5
print('姓名：%s,年龄：%d,成绩：%f' %(name,age,score))
print('姓名：%s,年龄：%d,成绩：%.1f' %(name,age,score))

#(2)f-string格式化字符串
print(f'姓名：{name},年龄：{age},成绩：{score}')

#(3)使用字符串format()方法，｛｝中内容相当于索引
print('姓名：{0},年龄：{1},成绩：{2}'.format(name,age,score))
print('姓名：{2},年龄：{1},成绩：{0}'.format(name,age,score))