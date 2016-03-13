#!/usr/bin/env python
import smtplib
from getpass import getpass
import sys
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
username = 'nsd.cicco@gmail.com'
password = getpass('Password: ')
smtp.ehlo()
smtp.login(username,password)
sys.stdout.write('Recipient: ')
recipient = sys.stdin.readline()
msg = "\r\n".join([
"From: " + username,
"To: " + recipient,
"Subject: " + "Hello!",
"",
"Body"
])
smtp.sendmail(username, recipient, msg)
smtp.quit()
