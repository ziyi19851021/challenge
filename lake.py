#/usr/bin/env python 

import urllib, urllib2
import wave, Image

def getwav(url, filename):
	username = 'butter'
	password = 'fly'
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

def wav_change_img(filename, imgpath):
	audio = wave.open(filename, 'r')
	#print audio.getparams()
	#print ord(audio.readframes(audio.getnframes())[10790])
	data = audio.readframes(audio.getnframes())
	img = Image.new('RGB', (60, 60),(255, 255, 255))
	for i in range(0, 10800, 3):
		print i
		r = ord(data[i])
		g = ord(data[i + 1])
		b = ord(data[i + 2])
		x = i/3
		img.putpixel((x%60, x/60), (r, g, b))
	img.save(imgpath)

if __name__ == '__main__':
	prefix_url = 'http://www.pythonchallenge.com/pc/hex/'
	prefix_path = './lakewav/'
	prefix_file = 'lake'
	suffix_file = '.wav'
	suffix_img = '.png'
	for i in range(1,26):
		filename = prefix_file + str(i) + suffix_file
		print filename
		url = prefix_url + filename
		path = prefix_path + filename
		imgpath = prefix_path + prefix_file + str(i) + suffix_img
		#getwav(url, path)
		wav_change_img(path, imgpath)

