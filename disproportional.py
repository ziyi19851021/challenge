#/usr/bin/env python

import urllib,xmlrpclib

name = urllib.urlopen("http://www.pythonchallenge.com/pc/return/evil4.jpg")
print str(name.read())
proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
try:
#	proxy.call(105)
	print proxy.phone("Bert")
	print proxy.phone("Leopold")
	print proxy.system.listMethods()
	print proxy.system.methodHelp('phone')
except xmlrpclib.Fault as err:
	print "A fault occurred"
	print "Fault code: %d" % err.faultCode
	print "Fault string:%s" % err.faultString
