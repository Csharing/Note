#!/usr/bin/env python3
#coding=utf-8
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.01',5500))

print(client.recv(1024).decode('utf-8'))

for data in [b'welcome1',b'welcome2']:
    client.send(data)
    print(client.recv(1024).decode('utf-8'))
#client.send(b'exit')
client.close()