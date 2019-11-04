#!/usr/bin/env python3
# coding=UTF-8
import  socket

soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#AF_INET指IPv4协议，SOCK_STREAM指流数据

soc.connect(('www.sina.com.cn',80))
#域名orIP和端口组成一个元组

soc.send(b'GET / HTTP/1.1\r\nHOST: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#发送二进制数据，一个request headers

buffer=[]
while True:

    d=soc.recv(1024)
    #一次最多制定接受的字节数

    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
#以''连接buffer內的内容

soc.close()
print(data.decode('utf-8'))

# header,html=data.split(b'\r\n\r\n',1)
##\r\n代表一个换行，header和html以两行隔开
#print(header.decode('utf-8')
# with open('sina.html','wb') as f:
#     f.write(html)
