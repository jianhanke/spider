import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print("访问错误")

def main():

	infoList=[]
	try:
		url="http://search.dangdang.com/?key=沈石溪&act=input&page_index=1"
		
		demo=getHTMLText(url)
		soup=BeautifulSoup(demo,"html.parser")
		for tagff in soup.find_all('p'):
			print(tagff.attrs)
		
			
	except:
		print("错误")
	
main()
