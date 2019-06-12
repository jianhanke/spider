import requests
from concurrent.futures import ProcessPoolExecutor

def fetch_request(url):
    result = requests.get(url)
    print(result.text)

url_list = [
    'http://www.baidu.com',
    'http://www.bing.com',
    'http://www.cnblogs.com/'
]
pool=ProcessPoolExecutor(10)
for url in url_list:
	print(url)
	pool.submit(fetch_request,url)
pool.shutdown(True)