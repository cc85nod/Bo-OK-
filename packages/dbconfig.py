"""
database name: finalproject
table: bookprice
column: id, name, writter, img, price, link
"""
import sqlite3

class db():
	def __init__(self):
		self.conn = sqlite3.connect('finalproject')
		self.cursor = self.conn.cursor()

	def __del__(self):
		self.conn.close()

	def insert(self, name, writter, img, price, link):
		self.cursor.execute("""\
		INSERT INTO bookprice (name,writter,img,price,link)
		VALUES ({},{},{},{},{})\
		""".format(name, writter, img, price, link))
		self.conn.commit()

	def insertDatas(self, datas):
		for data in datas:
			self.insert(data.name, data.writter, data.img, data.price, data.link)

	def select(self, name):
		datas = self.cursor.execute("""\
		SELECT name,writter, img, price, link from bookprice where name={}\
		""".format(name))
	
		return datas