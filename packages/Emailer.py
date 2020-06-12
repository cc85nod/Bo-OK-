import smtplib
from .settings import *
from email.mime.text import MIMEText

class Emailer():
	def __init__(self):
		self.emailer = {
			"account": ACCOUNT,
			"password": PASSWORD,
		}

	def sendMail(self, email, content):
		msg = MIMEText(content)
		msg["Subject"] = "Bo OK! 最新消息"
		msg["From"] = self.emailer["account"]
		msg["To"] = email

		server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		server.ehlo()
		server.login(self.emailer["account"], self.emailer["password"])
		server.send_message(msg)
		server.quit()
