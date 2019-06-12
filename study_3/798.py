import requests
import time

url='http://106.14.125.42:6767/kzy/home?types=8&types=9'
url2='http://106.14.125.42:6767/dev/wp/billing/start?did=8658860300896490&eid=14d87c1e0ea4aab6'
url3='http://106.14.125.42:6767/dev/wp/billing/start?did=8658860300896491&eid=14d87c1e0ea4aab6'
url4='http://798.hnkzy.com:6767/version/info?type=ANDROID&appKey=KZY'
url5='http://106.14.125.42:6767/dev/wp/billing/start?did=8658860300896490&eid=14d87c1e0ea4aab6'
#url6='http://106.14.125.42:6767/acc/'
url7='http://106.14.125.42:6767/dev/wp/billing/end?eid=14d87c1e0ea4aab6'
url8='http://106.14.125.42:6767/dev/wp/billing/balance?eid=14d87c1e0ea4aab6'
url9='http://47.100.33.146:6767/dev/wp/billing/start?did=8658860300896490&eid=14d87c1e0ea4aab6'
url10='http://47.100.33.146:6767/dev/wp/billing/end?eid=14d87c1e0ea4aab6'
balance_url='http://47.100.33.146:6767/dev/wp/billing/balance?eid=14d87c1e0ea4aab6'


headers={
	'User-Agent'	:'Apache-HttpClient/UNAVAILABLE (java 1.4)',
	'Content-Type'	:'application/json;charset=UTF-8',
	'Host'			:'47.100.33.146:6767',
	'Authorization':'Basic 14e579500e4d63aa1bd5ad6e125b3bc5',
	'Connection':	'keep-alive'
}

r=requests.put(url5,headers=headers)
str2=502 & 1
print(type(str2))
print(str2)
#update_time=time.time()
#print(update_time)
print(r)
# print(html)
# time.sleep(15)
# r2=requests.put(url10,headers=headers)
# print(r2.text)
