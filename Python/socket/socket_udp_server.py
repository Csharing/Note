#!/usr/bin/env python3
#coding=utf-8
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(('127.0.0.1',5500))

print('server bind in 5500...')

while True:
    data,addr = server.recvfrom(1024)
    rep='Hello,%s!'% data.decode('utf-8')
    server.sendto(rep.encode('utf-8'),addr)