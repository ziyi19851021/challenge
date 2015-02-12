#/usr/bin/env python

import base64,wave
import urllib2
import urllib

file = open('./bin.txt','r')
file1 = open('./indian.wav','w')
context = file.readlines()
#print context

for i in range(12,len(context)-3):
	#print context[i]
	a = base64.b64decode(context[i])
	file1.write(a)
	#print a
file.close()
file1.close()
gh_url = 'http://www.pythonchallenge.com/pc/hex/sorry.html'

audio1 = wave.open('./indian.wav','r')
audio2 = wave.open('./bin.wav','w')
print audio1.getparams()
audio2.setparams(audio1.getparams())
print audio1.tell()

#audio2.setnchannels(2)
#audio2.setnframes(audio1.getnframes()/2)
audio2.setframerate(audio1.getframerate()/2)
#audio1.setpos(audio1.getnframes()/2)

audio2.writeframes(audio1.readframes(audio1.getnframes())[0::2])
print audio2.getparams()
audio1.close()
audio2.close()

'''
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
username = 'butter'
password = 'fly'
top_level_url = 'www.pythonchallenge.com:80'
password_mgr.add_password(None,gh_url,username,password)
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
#opener.open(gh_url)
urllib2.install_opener(opener)
req = urllib2.Request(gh_url)
response = urllib2.urlopen(req)
page = response.read()
print str(page)

response = urllib.urlopen('http://www.pythonchallenge.com/pc/hex/sorry.html')
page = response.read()
print str(page)
'''
