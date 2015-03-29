#/usr/bin/env python

import email
import smtplib
import imaplib, os, ConfigParser

if __name__ == '__main__':
	sender = 'leopold.moz@pythonchallenge.com' 
	content = 'sorry'
	server = 'smtp.126.com'
	usr = 'wjr357220402@126.com'
	password = '7225214qq3528'
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
	'''
	box = imaplib.IMAP4_SSL('imap.126.com', 993)
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
