#!/usr/bin/env python3
#coding=utf-8
import socket
import threading,time

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('127.0.01',5500))

server.listen(10)


def tcplink(sock, addr):
    sock.send(b'welcome')
    while True:
        data=sock.recv(1024)
        #time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            sock.close()
            break
        sock.send(('hello,%s'% data.decode('utf-8')).encode('utf-8'))
        #含中文的str可以利用utf-8来编码为bytes
        #ba64，salt可以对二进制数据加密

    print("connection closed")



while True:
    sock,addr=server.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

