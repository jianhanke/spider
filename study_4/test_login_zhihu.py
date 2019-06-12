import requests
from selenium import webdriver
import time
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor

def ceshi_login():
	url="https://www.zhihu.com/"
	headers={
		'authority':'www.zhihu.com',
		'scheme': 'https',
		'cookie':'_xsrf=Kz7ax5pkAC5wggWGjMcHbfAPnIhJzJS3; z_c0="2|1:0|10:1550891197|4:z_c0|80:MS4xa2hfb0NRQUFBQUFtQUFBQVlBSlZUYjBHWGwwZHRDUFlaWHVqWUpYcXhkeF9BMm1JMTEyV1FRPT0=|12e721cd96af5d3833bfafc66d1cfe5070f40b43c4611b3e6e73fabf7224f6a7"; _zap=2ec0d1c9-e13b-463d-9b09-9079b889beb7; d_c0="ADCiDRQoBg-PTl_PbOrPO0_0deqHYqer9vo=|1550891197"; q_c1=c2734af1a4094ba08fe26afa091f2e13|1554896130000|1554896130000; __gads=ID=740bd88790d19716:T=1556636166:S=ALNI_MYwuiu27Y6VyjOX468X6ZLzdBJeCQ; tst=r; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
		'method': 'GET',
		'path': '/',
		'referer': 'https://www.zhihu.com/',
		'scheme': 'https',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
	}
	response=requests.get(url,headers=headers).text
	soup=BeautifulSoup(response,'html.parser')
	all_div=soup.find_all('div',attrs={"itemprop":"zhihu:question"})
	for div in all_div:
		meat=div.find_all('meta')[1]
		print(meat.get('content'))
def long_ceshi():
	headers={
		'authority':'www.zhihu.com',
		'scheme': 'https',
		'cookie':'_xsrf=Kz7ax5pkAC5wggWGjMcHbfAPnIhJzJS3; z_c0="2|1:0|10:1550891197|4:z_c0|80:MS4xa2hfb0NRQUFBQUFtQUFBQVlBSlZUYjBHWGwwZHRDUFlaWHVqWUpYcXhkeF9BMm1JMTEyV1FRPT0=|12e721cd96af5d3833bfafc66d1cfe5070f40b43c4611b3e6e73fabf7224f6a7"; _zap=2ec0d1c9-e13b-463d-9b09-9079b889beb7; d_c0="ADCiDRQoBg-PTl_PbOrPO0_0deqHYqer9vo=|1550891197"; q_c1=c2734af1a4094ba08fe26afa091f2e13|1554896130000|1554896130000; __gads=ID=740bd88790d19716:T=1556636166:S=ALNI_MYwuiu27Y6VyjOX468X6ZLzdBJeCQ; tst=r; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
		'method': 'GET',
		'path': '/',
		'referer': 'https://www.zhihu.com/',
		'scheme': 'https',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
	}
	count=0	
	for i in range(10):
		params={
			'session_token': 'de68db84fe51e446678da71a0b31960f',
			'desktop': 'true',
			'page_number': '6',
			'limit': '6',
			'action': 'down',
			'after_id': '23',
		}
		base_url='https://www.zhihu.com/api/v3/feed/topstory/recommend?'
		url=base_url+urlencode(params)
		response2=requests.get(url,headers=headers)
		all_json=response2.json()
		for one in range(len(all_json['data'])):
			try:
				print(all_json['data'][one]['target']['question']['title'])
				count+=1
			except:
				pass
	return count
def main():
	# long_ceshi()
	count=0
	pool=ThreadPoolExecutor(10)
	for i in range(10):
		v=pool.submit(long_ceshi)
		count+=v.result()
	print(count)
	pool.shutdown(True)



main()
		
		


