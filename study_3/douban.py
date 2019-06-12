import re
import requests
import time
from bs4 import BeautifulSoup
import requests
import pymysql

def ouput_url():
	for i in range(0,1000,20):
		url='https://book.douban.com/tag/%E7%BB%8F%E5%85%B8?start={}&type=T'.format(i)
		get_info(url)

def get_info(url):
	html=requests.get(url,timeout=5).text
	soup=BeautifulSoup(html,'html.parser')
	all_li=soup.find_all('li',attrs={'class':'subject-item'})
	db,cursor=connect_books()
	for li in all_li:
		img_url=li.find('img').get('src')
		book_name=li.find_all('a')[1].get('title')
		main_info=li.find('div',attrs={'class':'pub'}).string
		author=''
		press=''
		try:
			author,press=split_info(main_info)
			write_info(book_name,author,press,img_url,db,cursor)	
		except:
			print('分解失败')
			
def write_info(book_name,author,press,img_url,db,cursor):
	path='E:/wamp/apache/library/Public/books/'+book_name+'.jpg'

	img=requests.get(img_url).content
	try:
		with open(path,'wb') as f:
			f.write(img)
			f.close()
	except:
		print('写入失败')
	picture=" '{}' ".format(path)
	book_name=" '{}' ".format(book_name)
	press=" '{}' ".format(press)
	author=" '{}' ".format(author)
	sql="insert into books (book_name,author,press,picture) values ({},{},{},{})".format(book_name,author,press,picture)
	print(sql)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		print('存进数据库失败')
	
def connect_books():

	db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='learning')
	cursor=db.cursor()
	return db,cursor


#清洗数据
def split_info(main_info):
	main_info=str(main_info)
	main_info=main_info.strip().replace(' ','')
	info=main_info.split('/')
	info_num=len(info)
	author=''  #作者
	press='' #出版社

	if info_num==4:
		press=info[1]
		if '[' in info[0]:
			author=info[0].replace(re.findall("\[.+\]",info[0])[0],'')
			if '著、' in info[0]:
				author=author.replace(re.findall('著、.+',info[0])[0],'')
		elif '、' in info[0]:
			author=info[0].split('、')[0]
				
				#author=author.replace(re.findall(' '))
		elif  '（' in info[0]:
			author=info[0].replace(re.findall('（.）',info[0])[0],'')
		elif  '(' in info[0]:
			author=info[0].replace(re.findall('(.)',info[0])[0],'')
		else:
			author=info[0]
		return author,press
	if info_num==5:
		press=info[2]
		if '[' in info[0]:
			author=info[0].replace(re.findall("\[.+\]",info[0])[0],'')
			if '著、' in info[0]:
				author=author.replace(re.findall('著、.+',info[0])[0],'')
		elif '、' in info[0]:	
			author=info[0].split('、')[0]
		elif  '（' in info[0]:
			author=info[0].replace(re.findall('（.）',info[0])[0],'')
		elif  '(' in info[0]:
			author=info[0].replace(re.findall('(.)',info[0])[0],'')
		else:
			author=info[0]
		return author,press			
ouput_url()
