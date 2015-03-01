#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from datetime import datetime
from email.header import Header
from email.utils import parseaddr, formataddr

from_addr = 'zhouquantest16@gmail.com'
password = 'zqtest123'
smtp_server = 'smtp.gmail.com'
#to_addr = 'raw_input()'
to_addr = 'chandlerchou@yahoo.com'
text = '<html><body><p>你好,</p><p> 我是周周写的机器人</p>\
        <p>柏林时间： %s </p> <p>啦啦啦啦~~~快来打死我~~~</p><p>Code in <a href="http://www.python.org">Python</a>...</p></body></html>'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))	

def mailbomb():
	print 'Sending now...'
	server = smtplib.SMTP(smtp_server,587)
	server.starttls()
	server.set_debuglevel(1)
	server.login(from_addr,password)
	server.sendmail(from_addr,[to_addr],msg.as_string())
	server.quit()

count = 0
while count < 1:
	try:
		count +=1
		currenttime = str(datetime.now())[:-7]
		
		#define message
		msg = MIMEMultipart()
		msg['From'] = _format_addr(u'我的表情好贱吶~~ <%s>' % from_addr)
		msg['To'] = _format_addr(u'赵赵 <%s>' % to_addr)
		if count == 10:
			msg['Subject'] = Header(u'周周机器不再骚扰……', 'utf-8').encode()
		else:
			msg['Subject'] = Header(u'来自周周机器人的骚扰……', 'utf-8').encode()
		
		#define content
		msg.attach(MIMEText(text % currenttime , 'html', 'utf-8'))
		with open('/Users/JoshPAT/Desktop/seal.png') as f:
			mime = MIMEBase('image','png',filename  = 'seal.png')
			mime.add_header('Content-Disposition','attachment',filename ='seal.png')
			mime.add_header('Content-ID', '<0>')
			mime.add_header('X-Attachment-Id', '0')
			mime.set_payload(f.read())
			#用Base64来编码
			email.encoders.encode_base64(mime)
			msg.attach(mime)
		
		mailbomb()
		print '\nSuccessfully Sent %s\n'% count
		time.sleep(0.1)
	except KeyboardInterrupt:
		print 'Terminated'
		break

