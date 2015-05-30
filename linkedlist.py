#!/usr/bin/env python

import urllib,re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

search_pat = re.compile(r'next\s*nothing\s*is\s*(\d+)')
argument = "66831"

while not argument == "":
	response = urllib.urlopen(url+argument)
	html = str(response.read())
	print (html)
	argument = ''
	result = re.search(search_pat,html)
	if result != None:
		argument = result.group(0).split()[3]
	if argument == '':
		argument = raw_input(":")
