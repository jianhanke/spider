import requests
from bs4 import BeautifulSoup
import bs4
import os
import re
def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print('连接错误')
def main():
	try:
		info=[]
		url="http://www.henu.edu.cn/"
		root="D://henan/"

		html=getHTMLText(url)
		soup=BeautifulSoup(html,'html.parser')
		for information in soup.find_all('img'):
			if  isinstance(information,bs4.element.Tag):
				info.append(url+information.get('src'))
		if not os.path.exists(root):
			os.mkdir(root)	
		num=0	
		for i in info:
			try:
				num+=1
				path=root+'{}.jpg'.format(num)
				if not os.path.exists(path):
					picture=requests.get(i)
					with open(path,'wb') as f:
						f.write(picture.content)
						f.close()
						pritn('保存成功')
				else:
					print('文件存在')
			except:
				continue
	except:
		print('错误')
main()