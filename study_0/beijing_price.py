import requests
from bs4 import BeautifulSoup
import pymysql

all_div=[]
all_sql=[]
for num in range(1,12):
	url='https://bj.fang.lianjia.com/loupan/pg{}/'.format(num)
	r=requests.get(url)
	html=r.text
	soup=BeautifulSoup(html,'html.parser')
	all_div=soup.find_all('div',attrs={'class':'resblock-desc-wrapper'})

	for div in all_div:	
		all_li=div.find_all('div',attrs={'class':'resblock-name'})
		price=div.find('span',attrs={'class':'number'}).string
		price=" '{}' ".format(price)
		address=div.find('div',attrs={'class':'resblock-location'}).find('a').string
		address="'{}' ".format(address)
		for i in all_li:
			one=i.find('a')
			url='https://zz.fang.lianjia.com'+one.get('href')
			url="'{}' ".format(url)
			name=one.string
			name="'{}' ".format(name)
		sql="insert into bj_home_price (price,name,address,url) values ({},{},{},{})".format(price,name,address,url)
		all_sql.append(sql)
		print(sql)

	   #管理数据库方法，返回 db,cursor
	db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='spiders')
	cursor=db.cursor()
	for i in all_sql:
		try:
			cursor.execute(i)
			db.commit()
		except:
			pass