#/usr/bin/env python

import urllib, urllib2, re

gh_url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
username = 'butter'
password = 'fly'
password_mgr.add_password(None, gh_url,username, password)
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
values = {'Range' : 'bytes=0-2123456789'}
data = urllib.urlencode(values)

req = urllib2.Request(gh_url)
#req.add_data(data)
f = open('unreal.zip', 'w')
num = 1152983631
while num < 1152983632:
	search_pat = re.compile(r'Content-Range:\s*bytes\s*(\d+)-(\d+)')
	req.headers['Range'] = 'bytes=%s-%s' % (num, 2123456788)
	print req.header_items()
	try:
		response = urllib2.urlopen(req)
		result = re.search(search_pat,str(response.info()))
		num = int(result.group(0).split('-')[-1])+1
	
	except:
		num = num+1
	print response.info()
	print num
	f.write(response.read())
	#print response.read()

#page = response.read()
#print str(page)


