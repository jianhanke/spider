from ip_ceshi2 import GetProxy
import requests
from fake_useragent import UserAgent
#from ip_module import get
from ip_ceshi_github import github

proxy=github().ceshi()
print(proxy)
url='http://icanhazip.com/'
ua = UserAgent().random
headers = {'User-Agent': ua}
r=requests.get(url=url,headers=headers,proxies=proxy)
print(r.text)
# for i in proxies:
# 	ua = UserAgent().random
# 	headers = {'User-Agent': ua}
# 	print(i)
# 	url='http://httpbin.org/get'
# 	try:
# 		r=requests.get(url=url,headers=headers,proxies=i)
# 		print(r.text)
# 	except:
# 		pass