#/usr/bin/env python

x="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
i = 0
z=""
t=' '
while i <len(x):
	if ord(x[i]) >=ord('a') and ord(x[i])<=ord('z'):
		y=ord(x[i])+2
		if y>=ord('a') and y<=ord('z'):
			z=z+chr(y)
		else:
			z=z+chr(y-26)
	else:
		z=z+x[i]
	i=i+1
print z
xx ="http://www.pythonchallenge.com/pc/def/map.html"
print xx.maketrans()
