"""
database name: finalproject
table: bookprice
column: id, name, writer, img, price, link
"""
import sqlite3
from packages.BookCrawler import *

class DB():
	def __init__(self):
		self.conn = sqlite3.connect('book.db')
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

	def getBook(self, name):
		datas = self.cursor.execute("""\
		SELECT name,writer,img,price_books,link_books from bookprice where name='{}'\
		""".format(name))

		if not datas:
			datas = searchbook(target)
			self.storeSearch(datas)

		return datas.fetchall()
	"""
	更新資料庫
	"""
	def resetHotBook(self):
		# 歸零id
		self.cursor.execute('update sqlite_sequence set seq = 0 where name = "hotbook"')
		# 清空資料庫
		self.cursor.execute('DELETC FROM hotbook')

		for binfo in getBOOKSrank():       
			self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update hotbook set link_books = ? where id = ?', updatelink)
				self.cursor.execute('update hotbook set price_books = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"hotbook")
			else:
				self.cursor.execute('insert into hotbook(name,link_books,img,writer,price_books) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"hotbook")
		
		for binfo in getKINGSTONErank():
			self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update hotbook set link_kingstone = ? where id = ?', updatelink)
				self.cursor.execute('update hotbook set price_kingstone = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"hotbook")
			else:
				self.cursor.execute('insert into hotbook(name,link_kingstone,img,writer,price_kingstone) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"hotbook")
		for binfo in getSANMINrank():
			#print()
			self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update hotbook set link_sanmin = ? where id = ?', updatelink)
				self.cursor.execute('update hotbook set price_sanmin = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"hotbook")
			else:
				self.cursor.execute('insert into hotbook(name,link_sanmin,img,writer,price_sanmin) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from hotbook where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"hotbook")
		self.conn.commit()
	"""
	儲存搜尋的結果
	"""
	def storeSearch(self, searchlist):
		for binfo in searchlist[0]:
			self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update book set link_books = ? where id = ?', updatelink)
				self.cursor.execute('update book set price_books = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"search")
			else:
				self.cursor.execute('insert into book(name,link_books,img,writer,price_books) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"search")
		for binfo in searchlist[1]:
			self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update book set link_kingstone = ? where id = ?', updatelink)
				self.cursor.execute('update book set price_kingstone = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"search")
			else:
				self.cursor.execute('insert into book(name,link_kingstone,img,writer,price_kingstone) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"search")
		for binfo in searchlist[2]:
			self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
			tmplist=self.cursor.fetchall()
			if(tmplist):
				updatelink = [binfo["List"][1],tmplist[0][0]]
				updateprice = [binfo["List"][4],tmplist[0][0]]
				self.cursor.execute('update book set link_sanmin = ? where id = ?', updatelink)
				self.cursor.execute('update book set price_sanmin = ? where id = ?', updateprice)
				self.CountRank(tmplist[0][0],"search")
			else:
				self.cursor.execute('insert into book(name,link_sanmin,img,writer,price_sanmin) values (?,?,?,?,?)', binfo["List"])
				self.cursor.execute('select id from book where name = ? ',(binfo["List"][0],))
				tmplist=self.cursor.fetchall()
				self.CountRank(tmplist[0][0],"search")
		self.conn.commit()

		"""
		計算書籍在各熱門榜單的出現次數
		找出最低價格&書店名字
		bookid => 書本的 id
		mode => 搜尋, 暢銷書
		"""
		def CountRank(self, bookid, mode):
			count=0
			lowestprice=1000000
			lowestname=""

			if(mode=="hotbook"):
				self.cursor.execute('select price_books from hotbook where id = ? ',(bookid,))
			elif(mode=="search"):
				self.cursor.execute('select price_books from book where id = ? ',(bookid,))
			tmp = self.cursor.fetchall()
			if(tmp!=[(None,)]):
				count += 1
				if(tmp[0][0]<=lowestprice):
					lowestprice=tmp[0][0]
					lowestname="博客來"
			if(mode=="hotbook"):
				self.cursor.execute('select price_kingstone from hotbook where id = ? ',(bookid,))
			elif(mode=="search"):
				self.cursor.execute('select price_kingstone from book where id = ? ',(bookid,))
			tmp = self.cursor.fetchall()
			if(tmp!=[(None,)]):
				count += 1
				if(tmp[0][0]<lowestprice):
					lowestprice=tmp[0][0]
					lowestname="金石堂"
				elif(tmp[0][0]==lowestprice):
					lowestname+=",金石堂"
			if(mode=="hotbook"):
				self.cursor.execute('select price_sanmin from hotbook where id = ? ',(bookid,))
			elif(mode=="search"):
				self.cursor.execute('select price_sanmin from book where id = ? ',(bookid,))
			tmp = self.cursor.fetchall()
			if(tmp!=[(None,)]):
				count += 1
				if(tmp[0][0]<lowestprice):
					lowestprice=tmp[0][0]
					lowestname="三民"
				elif(tmp[0][0]==lowestprice):
					lowestname+=",三民"
			if(mode=="hotbook"):
				self.cursor.execute('update hotbook set ranktimes = ? where id = ?', (count,bookid))
				self.cursor.execute('update hotbook set lowest_price = ? where id = ?', (lowestprice,bookid))
				self.cursor.execute('update hotbook set lowest_name = ? where id = ?', (lowestname,bookid))
			elif(mode=="search"): 
				self.cursor.execute('update book set ranktimes = ? where id = ?', (count,bookid))
				self.cursor.execute('update book set lowest_price = ? where id = ?', (lowestprice,bookid))
				self.cursor.execute('update book set lowest_name = ? where id = ?', (lowestname,bookid))