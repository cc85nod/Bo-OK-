import packages.DBconfig
import packages.Emailer
import time

mydb = packages.DBconfig.DB()
emailer = packages.Emailer.Emailer()
second = 1
minute = 60
hour = 60*60
day = 24*60*60

def UpdateHotBook():
	mydb.resetHotBook()
	mydb.updateAllHotBookFromAllBookStore()
	print("Update Hot Book Done")

def UpdateNewBook():
	mydb.resetNewBook()
	mydb.updateAllNewBookFromAllBookStore()
	print("Update New Book Done")

def UpdateBook():
	mydb.resetBook()
	print("Update Book Done")

def MailNews():
	users = mydb.getUsers()
	
	for user in users:
		if user[0]:
			emailer.sendMail(user[0], "Hello~")

	print("Mail Done")

UpdateHotBook() # Uncomment it if you want to update hotbook
# UpdateNewBook() # Uncomment it if you want to update newbook
# UpdateBook() # Uncomment it if you want to clear book