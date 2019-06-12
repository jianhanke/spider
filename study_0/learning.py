import requests

def getHTMLText(url):
	try:
		r=requests.get(url,timeout=30) #timeout以秒为单位
		r.raise_for_status()  #状态码
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "产生异常"
if __name__=="__main__":
	url="http://www.baidu.com"
	print(getHTMLText(url))