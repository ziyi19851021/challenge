#/usr/bin/env python

import Image
import urllib2
import difflib

def download():
	url = 'http://www.pythonchallenge.com/pc/hex/zigzag.gif'
	username = 'butter'
	password = 'fly'
	filename = 'zigzag.gif'

	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	password_mgr.add_password(None, url, username, password)
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)

	f = open(filename, 'w')
	f.write(response.read())
	f.close()

def diff():
	im = Image.open('./zigzag.gif')
	im_new = Image.new('RGB', (im.size[0], im.size[1]),(0,0,0)) 
	im_p = im.convert('P', palette=Image.WEB) 
	list1 = im.tostring() 
	list2 = im_p.getpalette()
	list3 = im.palette.getdata()[1][2]
	'''
	#print list1[20]
	#print list2[2]
	#print dir(im_p.__class__)
	#print ord(list3)

	for i in range(im.size[0]):
		for j in range(im.size[1]):
			x = im.getpixel((i, j)) * 3
			im_new.putpixel((i, j), (list2[x], list2[x+1], list2[x+2]))
	im_new.save('zigzag_palette.bmp')
	'''
	print list(im.palette.getdata()[1][::3])

if __name__ == '__main__':
	#download()
	diff()
	
