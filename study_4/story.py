import requests
import os
from bs4 import BeautifulSoup
import pymysql
import sys
from w3lib.html import remove_tags

def get_info(url):
	
	r=requests.get(url)
	r.encoding=r.apparent_encoding
	demo=r.text
	
	soup=BeautifulSoup(demo,'html.parser')
	ul=soup.find('ul',attrs={'class':'zw'})
	story_classify=soup.find('div',attrs={'class':'dqian'}).find('ul').find('li').find_all('a')[1].string
	story_name=ul.find_all('p')[1].string
	story_text=ul.find_all('p')[2:]
	text=[]
	for i in story_text:
		string=str(i.string)
		if string !='None':
			text.append(string)
	mange_info(story_classify,story_name,text)

def mange_info(story_classify,story_name,text):
	root='E:/wamp/apache/library'
	path='/Public/Story/'+story_name+'.txt'
	root=root+path
	with open(root,'w',encoding='utf-8') as f:
		for i in text:
			f.write(i+'\n')
		f.close()
	write_info(story_name,path,story_classify)

def write_info(story_name,path,story_classify):
	path='.'+path
	db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='learning')
	cursor=db.cursor()
	story_name=" '{}' ".format(story_name)
	path=" '{}' ".format(path)
	story_classify=" '{}' ".format(story_classify)
	sql="insert into story (story_name,story_path,story_classify) values ({},{},{}) ".format(story_name,path,story_classify)
	print(sql)
	cursor.execute(sql)
	db.commit()
def main():
	for i in range(1400,1500):
		url="http://www.bqw123.cn/lizhi/{}.html".format(i)
		try:
			get_info(url)
		except:
			pass
	
main()


