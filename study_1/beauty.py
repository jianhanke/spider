import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		return r.text
	except:
		print('连接错误')
def main():
	url='http://www.mm131.com/qingchun/1486_2.html'
	html=getHTMLText(url)
	soup=BeautifulSoup(html,'html.parser')
	print(soup)
main()