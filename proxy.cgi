#!/usr/bin/python

import os;

print "Content-Type: text/html\n\n"

print "Hello! This is my first CGI script, it prints out everything we know about the HTTP request and the server environment:<br><br><br>"

list = os.environ.keys()
log=""
#file=open("/home/devasia/Desktop/log.txt", "a")

for el in list:
	log=log+ el+": "+os.environ[el]+"<br>"

print log
#file.write(el+": "+os.environ[el]+"\n")
#file.close();
