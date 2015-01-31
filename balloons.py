#/usr/bin/env python

import struct
from struct import *

file = open('./deltas/delta.txt','r')
file2 = open('./cave.jpg','r')
pic1 = open('./deltas/pic1.png','wb')
pic2 = open('./deltas/pic2.png','wb')
pic3 = open('./deltas/pic3.png','wb')

test = '1a'
print chr(int(test,16))
print len('       1')
list1 = []
list2 = []
list3 = []
for i in file:
#	print len(i)
	tem1 = i[0:55]
	list1 = tem1.split()
	for j in range(len(list1)):
		pic1.write(chr(int(list1[j],16)))
#	print list1

	tem2 = i[55:len(i)]
	list2 = tem2.split()
	for j in range(len(list2)):
		pic2.write(chr(int(list2[j],16)))
	for j in range(len(list1)):
		if list1[j] == list2[j]:
			pic3.write(chr(int(list1[j],16)))

file.close()
