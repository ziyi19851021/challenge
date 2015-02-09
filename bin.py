#/usr/bin/env python

import base64
import urllib2

file = open('./bin.txt','r')
file1 = open('./indian.wav','w')
context = file.readlines()
#print context

for i in range(12,len(context)-3):
	#print context[i]
	a = base64.b64decode(context[i])
	file1.write(a)
	#print a
file.close()
file1.close()

response = urllib2.Request('http://www.pythonchallenge.com/pc/hex/sorry.html')
html = urllib2.urlopen(response)
html1 = html.read()

print html1
