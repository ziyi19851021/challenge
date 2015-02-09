#/usr/bin/env python

import struct
from struct import *
import difflib
from difflib import *

def comlist():
	file = open('./deltas/delta.txt','r')
	pic1 = open('./deltas/pic1.png','wb')
	pic2 = open('./deltas/pic2.png','wb')
	pic3 = open('./deltas/pic3.png','wb')

#	test the hex number convert to the chr
#	test = '1a'
#	print chr(int(test,16))
#	print len('    1')

	list1 = []
	list2 = []
	list3 = []
	list4 = []
	list5 = []
	for i in file:
		tem1 = i[0:53]
#		print tem1
		list1[len(list1):] = [tem1]
		tem2 = i[56:109]
#		print tem2
		list2[len(list2):] = [tem2]
	d = difflib.Differ()
	diff = d.compare(list1,list2)
	print list1[0]
	print list2[0]
	for x in diff:
		if x.startswith('  '):
			list3 = x.replace('  ','').split()	
			for i in range(len(list3)):
				pic1.write(chr(int(list3[i],16)))
		elif x.startswith('+ '):
			list4 = x.replace('+ ','').split()
			for i in range(len(list4)):
				pic2.write(chr(int(list4[i],16)))
		elif x.startswith('- '):
			list5 = x.replace('- ','').split()
			for i in range(len(list5)):
				pic3.write(chr(int(list5[i],16)))
			

	file.close()
	pic1.close()
	pic2.close()
	pic3.close()

if __name__ == "__main__":
	comlist()
	for x in difflib.Differ().compare([1,2,3],[0,2,1]):
		print x
