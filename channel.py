#/usr/bin/env python

import zipfile

myzip = zipfile.ZipFile("channel.zip","r")
mydict = {}
myin = myzip.infolist()
for j in myin:
	mydict[j.filename.split('.')[0]] = str(j.comment.decode())
	#print (j.filename.split('.')[0])

dir = "./channel/"
argument = "90052"

while not argument =="":
	print (mydict[argument],end='')
	f = open(dir + argument+".txt","r")
	content = f.readline() 
	#print (content)
	f.close()
	argument = ''
	for i in range(len(content)):
		if content[i].isdigit():
			argument += content[i]


	#print (type(j.comment.decode()),end='')
