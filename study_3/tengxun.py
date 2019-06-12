import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url='https://ac.qq.com/ComicView/setPgvCountEx'
headers={
	"Host":	"ac.qq.com",
	"Connection":	"keep-alive",
	"Content-Length":	"38",
	"Origin":	"https://ac.qq.com",
	"User-Agent":	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
	"Content-Type":	"application/x-www-form-urlencoded",
	"Accept" :	"*/*",
	"Referer":	"https://ac.qq.com/ComicView/index/id/531490/cid/1",
	"Accept-Encoding"	:"gzip, deflate, br",
	"Accept-Language":	"zh-CN,zh;q=0.9",
	"Cookie":	"__AC__=1; pgv_pvi=4245904384; RK=l56tyGEka2; ptcz=459690973b2f15c731f51fb394392939a3d616389d08b927527092f99696ab8c; pgv_pvid=2255082265; tvfe_boss_uuid=9883fdfecdb152a8; o_cookie=398812180; pac_uid=1_398812180; ts_refer=www.sogou.com/link; ts_uid=7339178226; theme=dark; readLastRecord=%5B%5D; ptui_loginuin=398812180; pgv_info=ssid=s6640252768; _qpsvr_localtk=0.12333970410871409; pgv_si=s779235328; ptisp=cm; roastState=0; readRecord=%5B%5B531490%2C%22%E4%B8%80%E4%BA%BA%E4%B9%8B%E4%B8%8B%22%2C1%2C%221.%E5%A7%90%E5%A7%901%22%2C1%5D%2C%5B531527%2C%22%E5%A4%A7%E7%8C%BF%E7%A5%9E%22%2C212%2C%22%E8%90%A5%E6%95%91%E4%B8%BD%E5%A5%88%22%2C191%5D%5D; ts_last=ac.qq.com/ComicView/index/id/531490/cid/1",
}
data={
	'pgv': '5',
	'eid': 'KlBPTUBHUFFWAgIfAQYHAwEJHEEy',
}
html=requests.get(url,headers=headers,verify=False,data=data).text
print(html)
# soup=BeautifulSoup(html,'html.parser')
# div=soup.find('div',attrs={'class':'main'})
# print(div)
# all_li=div.find_all('li')
# for li in all_li:
# 	print(li)
