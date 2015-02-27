#/usr/bin/env python

import zlib, bz2

data = open("./unreal/package.pack", 'r+')
b = data.read()
#print b
n = 0
while n <= 1:
	try:
		b = bz2.decompress(b)
		n = 0
		print 1,
#		break
	except:
		try:
			b = zlib.decompress(b)
			n = 0
			print ' ',
#			break
		except:
			b = b[::-1]
			n = n + 1
			print '\n',
print b

aa = "1234567"
bb = aa[::-1]
print bb
print zlib.decompress("1234567")

