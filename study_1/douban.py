import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=10)
		r.raise_for_status()
		return r.text
	except:
		print('连接错误')
def movie(url):
	html=getHTMLText(url)
	soup=BeautifulSoup(html,'html.parser')
	all_div=soup.find_all('div',attrs={'class':'pic'})
	for i  in all_div:
		topic=i.find('em',attrs={'class':''}).string
		name=i.find('img').get('alt')
		string="排名:"+topic+"  "+'名字:'+name+'\n'
		with open('douban.csv','a') as f:
			f.write(string)
def movie_main():
	num=0
	for i in range(10):
		url='https://movie.douban.com/top250?start={}&filter='.format(num)
		num+=25
		movie(url)
  #######分解新啊#####################
def music(url):
	html=getHTMLText(url)
	soup=BeautifulSoup(html,'html.parser')
	all_div=soup.find_all('tr',attrs={'class':'item'})
	for i in all_div:
		num_person=i.find('span',attrs={'class':'pl'}).string
		num_person=num_person.replace('(','')
		num_person=num_person.replace(')','').strip()
		
		#
		num_music=i.find('a').get('title')
		all_information="{0:{2}<50}{1:<10}".format(num_music,num_person,chr(12288))+'\n'
		try:
			with open ('music.csv','a',encoding='gbk') as f:
				f.write(all_information)
		except:
			pass
def music_main():
	num=0
	for i in range(10):
		url='https://music.douban.com/top250?start={}'.format(num)
		num+=25
		music(url)
music_main()