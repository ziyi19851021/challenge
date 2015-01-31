#/usr/bin/env python

import pprint, pickle

pkl_file = open('peak.pkl', 'rb')

#print (pkl_file.readline())
data1 = pickle.load(pkl_file)
#pprint.pprint(data1)

pkl_file.close()

a =list (data1)
for i in range(len(a)):
	b = a[i]
	print('')
	for j in range(len(b)):
		x = tuple(b[j])
		for n in range(int(x[1])):
			print (x[0],end='')
