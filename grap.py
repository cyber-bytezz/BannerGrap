#! /usr/bin/python3

TCP_Address="192.168.100.7"        #Change Your IP Here

PORT=22

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_Address, PORT))

answer=s.recv(1024)

print(answer)

s.close