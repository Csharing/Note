#!/usr/bin/env python3
#coding=utf-8
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto(b'bob',('127.0.0.1',5500))

data,addr=client.recvfrom(1024)

print(data.decode('utf-8'),addr)

client.close()