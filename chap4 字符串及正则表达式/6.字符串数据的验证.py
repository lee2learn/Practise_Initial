# coding:utf-8
#所有字符都是数字（十进制的阿拉伯数字）
print('123'.isdigit())#True
print('一二三'.isdigit())#False
print('0b001'.isdigit())#False
print('Ⅲ'.isdigit())#False
print('---------------------------')
#所有字符都是数字（阿拉伯数字，罗马数字...）
print('123'.isnumeric())#True
print('一二三'.isnumeric())#True
print('0b001'.isnumeric())#False
print('Ⅲ'.isnumeric())#True
print('壹贰叁'.isnumeric())#True
print('---------------------------')
#所有都是字母（英文，中文）
print('hello你好'.isalpha()) #True
print('hello你好123'.isalpha()) #False
print('hello你好一二三'.isalpha()) #True
print('hello你好Ⅲ'.isalpha())  #False

#所有都是字母+数字
print('--------------------')
print('hello你好123'.isalnum()) #True
print('hello你好123...'.isalnum()) #False
print('hello你好壹贰叁'.isalnum()) #True
print('hello你好Ⅲ'.isalnum()) #True
print('hello你好一二三'.isalnum()) #True
print('--------------------')
#所有字符都是小写吗？
print('Helloworld'.islower())#False
print('helloworld'.islower())#True
print('hello你好'.islower())#True中文没有大小写
#所有字符都是大写吗？
print('HelloWorld'.isupper())#False
print('HELLOWORLD'.isupper())#True
print('HELLO你好'.isupper())#True
print('----------------')
#每个单词首字母是否大写
print('Hello'.istitle()) #True
print('HelloWorld'.istitle())#False
print('Helloworld'.istitle())#True
print('Hello World'.istitle())#True
print('Hello world'.istitle())#False

#是否都是空白字符
print('--------------------------')
print('\t'.isspace()) #True
print('    '.isspace())#True
print('\n'.isspace())#True