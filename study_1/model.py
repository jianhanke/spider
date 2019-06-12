import requests
from bs4 import BeautifulSoup
import bs4
import os
import re
def getHTMLText(url):
	try:
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
		r=requests.get(url,headers=headers)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print('连接错误')
def main():

	info=[]
	url='https://www.pku.edu.cn/'
	#root="D://anshi/"
	html=getHTMLText(url)
	soup=BeautifulSoup(html,'html.parser')
	address=None
	title=None
	print(title)
	href_a=soup.find_all('a');
	print('{:^80}\t{:^25}'.format('链接','标题'))
	for information in href_a:
		if isinstance(information,bs4.element.Tag):
			try:
				address=information.get('href')
				if not('http' in address):
					address=url+address
				title=information.string
				if title is None:
					tilte=information.find('a',attrs='span').string
					if title is None:
						title='空'
			except:
				pass
			print('{:<65}\t{:<10}'.format(str(address),str(title)))
			# all_Info='链接:'+str(address)+'标题:'+str(title)+'\r'
			# info.append(all_Info)
			#writeText(info)
def writeText(info):
	root='G://study_first/'
	path=root+'北京大学.txt'
	if not os.path.exists(root):
		os.mkdir(root)
	for i in info:
		with open(path,'a') as f:
			f.write(i)
			f.close

main()