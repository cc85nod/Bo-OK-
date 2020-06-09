"""
database name: finalproject
table: bookprice
column: id, name, writer, img, price, link
"""
import sqlite3

class db():
	def __init__(self):
		self.conn = sqlite3.connect('test.db')
		self.cursor = self.conn.cursor()

	def __del__(self):
		self.conn.close()

	def insert(self, name, writer, img, price, link):
		self.cursor.execute("""\
		INSERT INTO bookprice (name,writer,img,price,link)
		VALUES ('{}','{}','{}','{}','{}')\
		""".format(name, writer, img, price, link))
		self.conn.commit()

	def insertDatas(self, datas):
		for data in datas:
			self.insert(data.name, data.writer, data.img, data.price, data.link)
			self.conn.commit()

	def select(self, name):
		# datas = self.cursor.execute("""\
		# SELECT name,writer, img, price, link from bookprice where name='{}'\
		# """.format(name))
		datas = self.cursor.execute("""\
		SELECT name,writer,img,price_books,link_books from bookprice where name='{}'\
		""".format(name))
	
		return datas.fetchall()