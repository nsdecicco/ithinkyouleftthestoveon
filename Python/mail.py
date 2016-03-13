#!/usr/bin/env python
import smtplib
from getpass import getpass
import sys
import BaseHTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import cgi

RECPT_TYPE_SMS = 1
RECPT_TYPE_EMAIL = 2

registeredDevices = []

class Device():
	carrierAddr = ''
	recptType = ''
	emailAddr = ''
	emailPasswd = ''
	phoneNumber = ''
	macAddr = ''
	def __init__(self, carrierAddr, recptType, emailAddr, emailPasswd, phoneNumber, macAddr):
		self.carrierAddr  = carrierAddr
		self.recptType    = recptType
		self.emailAddr    = emailAddr
		self.emailPasswd  = emailPasswd
		self.phoneNumber  = phoneNumber
		self.macAddr      = macAddr
	def notifyDevice():
		subject = ''
		body = ''
		if self.recptType == 'sms':
			print 'Sending e-mail notification to ' + self.phoneNumber + self.carrierAddr + ' via ' + self.emailAddr
			send_email(self.emailAddr, self.emailPasswd, self.phoneNumber + self.carrierAddr, subject, body)
		elif self.recptType == 'email':
			print 'Sending e-mail notification to ' + self.emailAddr + ' via ' + self.emailAddr
			send_email(self.emailAddr, self.emailPasswd, self.emailAddr, subject, body)

def send_email(username, password, recipient, subject, body):
	smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp.ehlo()
	smtp.login(username,password)
	msg = "\r\n".join([
	"From: " + username,
	"To: " + recipient,
	"Subject: " + subject,
	"",
	body
	])
	smtp.sendmail(username, recipient, msg)
	smtp.quit()

def registerDevice(carrierAddr, recptType, emailAddr, emailPasswd, phoneNumber, macAddr):
	registeredDevices.append(Device(carrierAddr, recptType, emailAddr, emailPasswd, phoneNumber, macAddr))

class RequestHandler(BaseHTTPRequestHandler):
	services = [
		{ 'name': "T-Mobile", 'address': "@tmomail.net" },
		{ 'name': "AT&amp;T", 'address': "@txt.att.net" },
		{ 'name': "Verizon",  'address': "@vtext.com" },
		{ 'name': "Sprint",   'address': "@messaging.sprintpcs.com" },
	]

	registerPage = '\r\n'.join([
		'<!DOCTYPE html>',
		'<html>',
		'<head>',
		'<title>I Think I Left The Stove On</title>',
		'<meta charset="utf-8">',
		'<script type="text/javascript">',
		'function update(e) {',
		'var phoneNumPanel = document.getElementById("phoneNum");',
		'if (e.value === "email") {',
		'	phoneNumPanel.style.display = "none";',
		'} else if (e.value === "sms") {',
		'	phoneNumPanel.style.display = "table-row";',
		'}',
#		'document.getElementsByName("email")[0].value',
		'}',
		'</script>',
		'<style type="text/css">',
		'* {',
		'	font-family: sans-serif;',
		'}',
		'body {',
		'	background: #1d39ae;',
		'}',
		'div {',
		'	background: #eee;',
		'	padding: 5px 15px 15px 15px;',
		'	',
		'}',
		'h1 {',
		'	text-align: center;',
		'	font-size: 16pt;',
		'	font-family: Verdana, sans-serif;',
		'}',
		'ul.radiolist, ul.radiolist li {',
		'	padding: 0px;',
		'	list-style-type: none;',
		'}',
		'input[type="submit"] {',
		'	padding: 10px 15px;',
		'	font-size: 15pt;',
		'	font-weight: bold;',
		'	color: white;',
		'	background: #1d39ae;',
		'	border-color: #1d39ae;',
		'	border-style: solid;',
		'	border-radius: 5px;',
		'}',
		'input[type="submit"]:hover {',
		'	background: #2f54f4;',
		'	border-background: #2f54f4;',
		'}',
		'input[type="submit"]:active {',
		'	background: #122577;',
		'	border-color: #122577;',
		'	padding: 12px 15px 8px 15px;',
		'}',
		'div.center {',
		'	text-align: center;',
		'}',
		'</style>',
		'</head>',
		'<body>',
		'<div class="main">',
		'<form action="register" method="post">',
		'<h1>I Think I Left The Stove On</h1>',
		'<p>Select your carrier:</p>',
		'<select name="carrier">',
		'\r\n'.join([ ('<option value="%d">' % (i)) + service['name'] + '</option>' for i, service in enumerate(services,0) ]),
		'</select>',
		'<p>How do you want to be notified?</p>',
		'<ul class="radiolist">',
		'<li><input onchange="update(this)" checked type="radio" name="deliveryPref" value="sms">SMS</input></li>',
		'<li><input onchange="update(this)" type="radio" name="deliveryPref" value="email">E-mail</input></li>',
		'</ul>',
		'<table>',
		'<tr id="phoneNum"><td><label for="phoneNumber">10-digit phone number:</label></td><td><input type="text" name="phoneNumber"></tr>',
		'<tr><td><label for="emailaddr">E-mail address:</label></td><td><input type="text" name="emailaddr"></tr>',
		'<tr><td><label for="emailpasswd">Password:</label></td><td><input type="password" name="emailpasswd"></tr>',
		'</table>',
		'<div class="center">',
		'<input type="submit" value="Notify me!">',
		'</div>',
		'</form>',
		'</div>',
		'</body>',
		'</html>'
	])

	confirmPage = '\r\n'.join([
		'<!DOCTYPE html>',
		'<html>',
		'<head>',
		'<title>I Think I Left The Stove On</title>',
		'<meta charset="utf-8">',
		'<style type="text/css">',
		'* {',
		'	font-family: sans-serif;',
		'}',
		'body {',
		'	background: #1d39ae;',
		'}',
		'div {',
		'	background: #eee;',
		'	padding: 5px 15px 15px 15px;',
		'	',
		'}',
		'h1 {',
		'	text-align: center;',
		'	font-size: 16pt;',
		'	font-family: Verdana, sans-serif;',
		'}',
		'</style>',
		'</head>'
		'<body>'
		'<div class="main">',
		'<h1>Request confirmed!</h1>',
		'</div>',
		'</body>',
		'</html>'
	])

#	def __init__(self):

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-Type", "text/html")
		self.send_header("Content-Length", len(self.registerPage))
		self.end_headers()
		self.wfile.write(self.registerPage)

	def do_POST(self):
		# Courtesy of http://stackoverflow.com/a/4233452
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
		if ctype == 'multipart/form-data':
			postvars = cgi.parse_multipart(self.rfile, pdict)
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers.getheader('content-length'))
			postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
		else:
			postvars = {}
#		carrierAddr = [ service['address'] for service in self.services if service['name'] == postvars['carrier'] ]
		carrierAddr = self.services[int(postvars['carrier'][0])]['address']
		registerDevice(carrierAddr, postvars['deliveryPref'][0], postvars['emailaddr'][0], postvars['emailpasswd'][0], postvars['phoneNumber'][0], macAddr)
		self.send_response(200)
		self.send_header("Content-Type", "text/html")
		self.send_header("Content-Length", len(self.confirmPage))
		self.end_headers()
		self.wfile.write(self.confirmPage)
		print 'post from ' + self.client_Address[0]

server = BaseHTTPServer.HTTPServer(("", 3000), RequestHandler)
server.serve_forever()
