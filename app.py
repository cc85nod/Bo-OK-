from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy
# import packages.dbconfig
# import packages.crawler

app = Flask(__name__, template_folder='templates')
# mydb = packages.dbconfig.db()

test_hot_datas = [
	{
		"name": "早什麼安啊：才剛打卡就想回家，今天又是來混日子的一天",
		"writter": "安成敏",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/94/0010859413_bc_01.jpg&v=5ec66645&w=655&h=609",
		"price": "284",
		"link": "https://www.books.com.tw/products/0010859413?loc=P_0032_1_003",
	},
	{
		"name": "我就賤 ： 喵星人Sola、洽米開示，一賤天下無難事",
		"writter": "宇宙垃圾",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/83/0010858340_bc_01.jpg&v=5ec514f2&w=655&h=609",
		"price": "253",
		"link": "https://www.books.com.tw/products/0010858340?loc=P_0025_1_004",
	},
]

test_datas = [
	{
		"name": "早什麼安啊：才剛打卡就想回家，今天又是來混日子的一天",
		"writter": "安成敏",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/94/0010859413_bc_01.jpg&v=5ec66645&w=655&h=609",
		"price": "285",
		"link": "https://www.books.com.tw/products/0010859413?loc=P_0032_1_003",
	},
	{
		"name": "早什麼安啊：才剛打卡就想回家，今天又是來混日子的一天",
		"writter": "安成敏",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/94/0010859413_bc_01.jpg&v=5ec66645&w=655&h=609",
		"price": "285",
		"link": "https://www.books.com.tw/products/0010859413?loc=P_0032_1_003",
	},
	{
		"name": "早什麼安啊：才剛打卡就想回家，今天又是來混日子的一天",
		"writter": "安成敏",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/94/0010859413_bc_01.jpg&v=5ec66645&w=655&h=609",
		"price": "282",
		"link": "https://www.books.com.tw/products/0010859413?loc=P_0032_1_003",
	},
	{
		"name": "早什麼安啊：才剛打卡就想回家，今天又是來混日子的一天",
		"writter": "安成敏",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/94/0010859413_bc_01.jpg&v=5ec66645&w=655&h=609",
		"price": "281",
		"link": "https://www.books.com.tw/products/0010859413?loc=P_0032_1_003",
	},
	{
		"name": "早什麼安啊：才剛打卡就想回家，今天又是來混日子的一天",
		"writter": "安成敏",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/94/0010859413_bc_01.jpg&v=5ec66645&w=655&h=609",
		"price": "281",
		"link": "https://www.books.com.tw/products/0010859413?loc=P_0032_1_003",
	},
	{
		"name": "早什麼安啊：才剛打卡就想回家，今天又是來混日子的一天",
		"writter": "安成敏",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/94/0010859413_bc_01.jpg&v=5ec66645&w=655&h=609",
		"price": "281",
		"link": "https://www.books.com.tw/products/0010859413?loc=P_0032_1_003",
	},
	{
		"name": "早什麼安啊：才剛打卡就想回家，今天又是來混日子的一天",
		"writter": "安成敏",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/94/0010859413_bc_01.jpg&v=5ec66645&w=655&h=609",
		"price": "281",
		"link": "https://www.books.com.tw/products/0010859413?loc=P_0032_1_003",
	},
	{
		"name": "早什麼安啊：才剛打卡就想回家，今天又是來混日子的一天",
		"writter": "安成敏",
		"img": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/085/94/0010859413_bc_01.jpg&v=5ec66645&w=655&h=609",
		"price": "281",
		"link": "https://www.books.com.tw/products/0010859413?loc=P_0032_1_003",
	},
]

# 首頁
@app.route('/')
def index():
	sdatas = split_data(test_hot_datas)
	return render_template('index.html', sdatas=sdatas)

# 熱門書單
@app.route('/hot')
def hot():
	pass

# 訂閱
@app.route('/register')
def register():
	pass

# 找書
@app.route('/show')
def show():
	# book_name = request.args.get('book_name', type=str)
	# if book_name is None:
	# 	return render_template('index.html')
	
	# datas = mydb.select(book_name)

	# if not datas:
	# 	datas = crawler.find(book_name)
	# 	mydb.insertDatas(datas)
	
	return render_template('show.html', datas=test_datas)

"""
Split datas to 3,3,3... because a row contains only 3 datas
"""
def split_data(datas):
	new_datas = []
	for i in range(0, len(datas), 3):
		new_datas.append(datas[i:i+3])
	
	return new_datas

if __name__=='__main__':
	app.run(port=10000, threaded=True)