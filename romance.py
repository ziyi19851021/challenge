#/usr/bin/env python

import cookielib,urllib,re,urllib2,bz2

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
info = re.compile(r'info=\S+')
search_pat = re.compile(r'next\s*busynothing\s*is\s*(\d+)')
argument = "12345"
password = ""
a = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
b="BZh91AY\x26SY\x94\x3A\xE2I\x00"

#a2 = urllib.unquote_plus(a)
print bz2.BZ2Decompressor().decompress(urllib.unquote_plus(a))
#print a2
#a1 = urllib.unquote(a)
#print b.decode("bz2")
#print a1.decode("bz2").flush()

v = "file"
v1 = v.encode("bz2")
v2 = urllib.quote(v1)
print v1
print "123123123"
v4 = urllib.unquote(v2)
#print v4 
#print v1.decode("bz2")
'''
while not argument == "":
	response = urllib.urlopen(url+argument)
	r = opener.open(url+argument)
#	print help(cj)
	print r.read()

	for cookie in cj:
		passchar = re.search(info, str(cookie))
		if passchar != None:
#			print passchar.group(0) 
			tem = urllib.unquote(passchar.group(0).split("=")[-1])
			password += tem
		#	print password
		#	password += passchar.group(0).split("=")[-1]
	#	print str(cookie)
	html = str(response.read())
#	print (r)
	print (password)
	argument = ''
	result = re.search(search_pat,html)
	if result != None:
		argument = result.group(0).split()[-1]
	if argument == '':
		argument = raw_input(":")
print passchar.decode("bz2")
'''
cj2 = cookielib.CookieJar()
opener2 = urllib2.build_opener()
#cj2['info'] = "the flowers are on their way"
values = {'Cookie':urllib.quote_plus('the flowers are on their way')}
data = urllib.urlencode(values)
opener2 = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj2))
url2 = "http://www.pythonchallenge.com/pc/stuff/violin.php"
req = urllib2.Request(url2,data)
req.add_header('Cookie','info=the flowers are on their way')
res3 = opener2.open(req)
print res3.info()
print res3.read()
#print req.read()
#opener2.addheader.append(('Cookie','info=the flowers are on their way'))
#f = opener2.open("http://www.pythonchallenge.com/pc/stuff/violin.php")
#from http import cookies
#C = cookies.SimpleCookie()
#C["info"] = "the flowers are on their way"
