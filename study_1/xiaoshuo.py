import requests
from bs4 import BeautifulSoup
import bs4
import os
import re

def getHTMLText(url):
	try:
		r=requests.get(url)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print('连接错误')
def main(url):
	html=getHTMLText(url)
	soup=BeautifulSoup(html,'html.parser')
	texts=soup.find('div',attrs={'class':'showtxt'})
	 #find_all 返回的是一个列表 ,因为只找到了一个 所以要用 texts[0]
	 # text属性，提取文本内容，清楚 <br>标签 $nbsq不是标签
	return (texts.text.replace('\xa0'*8,'\n'))

def all():
	url='https://www.biqukan.com/1_1094/'
	info=[]
	hrefs=[]
	titles=[]
	nums=0
	shu={}
	html=getHTMLText(url)
	soup=BeautifulSoup(html,'html.parser')
	info=soup.find_all('dd')
	root='G:\study_first\小说\ '
	for i in info:
		href=i.find('a').get('href')
		href='https://www.biqukan.com'+href
		hrefs.append(href)
		title=i.find('a').string
		titles.append(title)
		nums+=1
	for i in range(50,100):
		try:
			print(i)
			path_name=root+titles[i]+'.txt'
			url=hrefs[i]
			information=main(url)
			with open(path_name,'w',encoding='utf-8') as f:
				f.write(information)
				f.close()
		except:
			continue
all()
