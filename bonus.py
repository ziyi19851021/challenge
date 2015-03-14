#/usr/bin/env python

import this

x = "va gur snpr bs jung"
t = ''
for j in range(26):
	for i in range(len(x)):
		if x[i] != ' ':
			if x[i] != 'z':
				t = t + chr(ord(x[i])+1)
			else:
				t = t + chr(ord(x[i])-25)
		else :
			t = t + ' '
	x = t
	t = ''
	print j
	print x
