# coding:utf-8
#编码
s='伟大的中国梦'
#编码
scode_gbk=s.encode('gbk')
print(scode_gbk)#一个中文字使用2个字节存储

scode_utf8=s.encode()#默认utf-8
print(scode_utf8)#一个中文字使用3个字节存储

#编码中的error处理
s2='耶❤'
scode=s2.encode('gbk',errors='ignore')
print(scode)

#解码 bytes--->str
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode_utf8,'utf-8'))
print(bytes.decode(scode,'gbk',errors='ignore'))
