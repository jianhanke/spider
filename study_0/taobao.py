import requests
import re

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		print("访问错误")
def parsePage(ilt,html):
	try:
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
		tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price=eval(plt[i].split(':')[1])#eval 将price的双引号和单引号去掉
			title=eval(tlt[i].split(':')[1])
			ilt.append([price,title])
	except:
		print("包含出错")
def printGoodsList(ilt):
	tplt="{:4}\t{:8}\t{:16}"
	print(tplt.format("序号","价格","商品名称"))
	count=0
	for g in ilt:
		count=count+1
		print(tplt.format(count,g[0],g[1]))
	print(len(ilt))
	
def main():
	goods='书包'
	depth=2
	start_url=''
	infoList=[]
	for i in range(depth):
		try:
			url=start_url+'$s='+str(44*i)
			html=getHTMLText(url)
			parsePage(infoList,html)
		except:
			continue
	printGoodsList(infoList)
main()
