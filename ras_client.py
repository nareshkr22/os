#!/usr/bin/env python3

import sys
from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP   = '192.168.1.129'
PORT_NUMBER = 1215
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
myMessage = "Hello!"
myMessage1 = ""
i = 0
while True:
    i = i + 1
    msg = raw_input("Enter Data : ")
    mySocket.sendto(msg.encode('utf-8'),(SERVER_IP,PORT_NUMBER))

sys.exit()
