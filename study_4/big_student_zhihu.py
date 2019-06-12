import requests
from selenium import webdriver
import time
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor

headers={
		'authority':'www.zhihu.com',
		'scheme': 'https',
		'cookie':'_xsrf=Kz7ax5pkAC5wggWGjMcHbfAPnIhJzJS3; z_c0="2|1:0|10:1550891197|4:z_c0|80:MS4xa2hfb0NRQUFBQUFtQUFBQVlBSlZUYjBHWGwwZHRDUFlaWHVqWUpYcXhkeF9BMm1JMTEyV1FRPT0=|12e721cd96af5d3833bfafc66d1cfe5070f40b43c4611b3e6e73fabf7224f6a7"; _zap=2ec0d1c9-e13b-463d-9b09-9079b889beb7; d_c0="ADCiDRQoBg-PTl_PbOrPO0_0deqHYqer9vo=|1550891197"; q_c1=c2734af1a4094ba08fe26afa091f2e13|1554896130000|1554896130000; __gads=ID=740bd88790d19716:T=1556636166:S=ALNI_MYwuiu27Y6VyjOX468X6ZLzdBJeCQ; tst=r; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
		'method': 'GET',
		'referer': 'https://www.zhihu.com/topic/19555480/hot',
		'scheme': 'https',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
	}
url='https://zhihu-web-analytics.zhihu.com/api/v1/logs/batch'
res=requests.post(url,headers=headers)
print(res.text)

