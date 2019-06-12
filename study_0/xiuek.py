import requests
from bs4 import BeautifulSoup
import bs4
import os
import re

def getHTMLText(url):
	try:
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
		r=requests.get(url,timeout=30,headers=headers)
		r.raise_for_status()
		
		return r.text
	except:
		print('连接错误')

def PageInfo(url):
	try:
		
		info={}
		html=getHTMLText(url)
		soup=BeautifulSoup(html,'html.parser')
		author=soup.find('span',attrs={'class':'side-user-name'}).string
		age=soup.find('span',attrs={'class':'side-fans-num userM'}).find(string=re.compile('\d{2}'))
		content=soup.find('title').string
		information="author="+author+",age="+age+"\ncontent="+content+" \n"
		with open('123.txt','a+' ) as f:
			f.write(information)
	except:
		print('错误'+ url)
def getAll(url):
	urls="https://www.qiushibaike.com"
	info=[]
	num=0
	html=getHTMLText(url)
	soup=BeautifulSoup(html,'html.parser')
	info=soup.find_all('a',attrs={'class':'recmd-content'})
	for article in info:
		url=urls+article.get('href')
		num=num+1
		PageInfo(url)
def main():
	for i in range(1,3):
		url="https://www.qiushibaike.com/8hr/page/{}/".format(i)
		getAll(url)		
main()
