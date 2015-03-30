#/usr/bin/env python

import email
import smtplib
import imaplib, os, ConfigParser
import poplib
import md5

def review(md5_r):
	file = open("./mybroken.zip", 'rb')
	file2 = open("./mybroken2.zip", 'wb')
	con = file.read()
	print ord(con[0])
	for i in range(len(con)):
		print len(con) - i	
		for j in range(256):
			tem_num = ord(con[i])
			if tem_num < 255:
				con = con[:i] + chr(tem_num + 1) + con[(i+1):]
			else:
				con = con[:i] + chr(0) + con[(i+1):]
			tem = md5.new(con).hexdigest()
			if tem == md5_r:
				print tem
				file2.write(con)
				return
	
if __name__ == '__main__':
	sender = 'leopold.moz@pythonchallenge.com' 
	content = 'sorry'
	server = 'smtp.126.com'
	usr = 'wjr357220402@126.com'
	password = '7225214qq3528'
	md5_r = 'bbb8b499a0eef99b52c7f13f4e78c24b'
	review(md5_r)
	'''
	message = email.Message.Message()
	message['Subject'] = content
	message['From'] = usr
	message['To'] = sender
	message.set_payload('sorry')
	msg = message.as_string()
	
	recipients = [usr, sender]
	session = smtplib.SMTP(server, port = 25, timeout = 20)
	#session.set_debuglevel(1)
	session.login(usr, password)
	#session.sendmail(usr, recipients, msg)
	session.quit()
	
	box = imaplib.IMAP4_SSL('imap.126.com')
	box.login(usr, password)
	box.list()
	box.select('inbox')
	result, data = box.search(None, 'All')
	ids = data[0]
	id_list = ids.split()
	latest_email_id = id_list[-1]
	result, data = box.fetch(latest_email_id, "(RFC822)")
	raw_email = data[0][1]
	print raw_email
	
	box = poplib.POP3_SSL('pop3.126.com')
	box.user(usr)
	box.pass_(password)
	numMessage = len(box.list()[1])

	for i in range(numMessage):
		print box.retr(numMessage-i)[2]
		print i

	for j in box.retr(numMessage-5)[1]:
		print j
	box.quit()
	'''
	
