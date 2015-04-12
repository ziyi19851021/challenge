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
	im_rgb = im.convert('RGB')	
	im_l = im.convert('L')
	im_p = im.convert('P')
	
	list1 = []
	list2 = []
	for i in range(im.size[0]):
		for j in range(im.size[1]):
			list1.append(im.getpixel((i, j)))
			list2.append(im_l.getpixel((i, j)))
	d = difflib.Differ()
	diff = d.compare(list1,list2)
	for x in diff:
		print x

if __name__ == '__main__':
	#download()
	#diff()
	im = Image.open('./zigzag.gif')
	im_p = im.convert('P', palette=Image.WEB)
	list1 = im.tostring()
	list2 = im_p.getpalette()
	list3 = im_p.palette.getdata()[1][::3]
	print list1[20]
	print list2[2]
	print dir(im_p.__class__)
	print list3
