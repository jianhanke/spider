import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_info(url):
	result=requests.get(url)
	return result
	
def ceshi():               #线程调用，错误不会提醒，正常调用，则会出错
	result=request.get('http://www.baidu.com')
	print(result.text)
def call_back(fulture):
	print(fulture.result().text)
url_list = [
    'http://www.baidu.com',
    'http://www.bing.com',
    'http://www.cnblogs.com/'
]
pool=ThreadPoolExecutor(10)
for url in url_list:
	v=pool.submit(fetch_info,url) #拿出一个线程去执行,得出的v 是线程格式,需要转换 
	print(v)
	v.add_done_callback(call_back)

pool.shutdown(True)






