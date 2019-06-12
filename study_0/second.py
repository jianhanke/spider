import requests
import time 

def getHTMLText(url):
	try:
		r=requests.get(url)
		r.encoding=r.apparent_encoding
		r.raise_for_status
	except:
		print("访问错误")
if __name__=='__main__':
	url="http://www.qq.com/"
	start=time.time()
	for i in range(101):
		getHTMLText(url)
		print('the{}time have success'.format(i))
	end=time.time()
	print("访问100次的时间为:",end-start)