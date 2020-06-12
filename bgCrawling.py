import packages.DBconfig
import packages.Emailer
import time
from threading import Thread

mydb = packages.DBconfig.DB()
emailer = packages.Emailer.Emailer()
second = 1
minute = 60
hour = 60*60
day = 24*60*60

def UpdateHotBook(Thread):
	def run(self):
		mydb.resetHotBook()
		sleep(day)

def UpdateNewBook(Thread):
	def run(self):
		mydb.resetNewBook()
		sleep(day)

def MailNews(Thread):
	def run(self):
		users = mydb.getUsers()

		for user in users:
			emailer.sendMail(user, "Hello~")

		sleep(6*hour)

def run():
	UpdateHotBook().start()
	UpdateNewBook().start()
	MailNews().start()