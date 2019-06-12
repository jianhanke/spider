import requests
from selenium import webdriver
import time
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from lxml import etree

url="https://d.weibo.com/231650?cfs=920&Pl_Discover_Pt6Rank__4_filter=&Pl_Discover_Pt6Rank__4_page=1"
headers={
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Cookie':'SINAGLOBAL=6739368062615.665.1558278581473; wb_view_log_6465114819=1536*8641.25; UOR=,,login.sina.com.cn; un=15239910806; wvr=6; wb_view_log_3754667033=1536*8641.25; ALF=1591622972; SSOLoginState=1560086972; SCF=Av3cpggR2bnuhvYuvll2gPoq9T-2TOV2C_4S__BGIQmQYCcRQmrPPFykpE6lyBjGRDgrM0QwSBoV4hBf6qee_NA.; SUB=_2A25x-XnuDeRhGeVJ7lYX9inMyD-IHXVSj-wmrDV8PUNbmtANLRCgkW9NT_Y8KnKkUrRGlrg8O68lmPGKOPxUSyWp; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFav6PDx.POHbwqXgDejdoC5JpX5KzhUgL.FoeNSKBcSoM7e0e2dJLoIpjLxK-L1h.L1K2LxK-LB-qL1KzLxK-LB--LBKzt; SUHB=0u5RT4EvfYV_yU; _s_tentry=-; Apache=6681973952081.039.1560086978272; ULV=1560086978293:39:20:7:6681973952081.039.1560086978272:1560085599818; YF-Page-G0=aedd5f0bc89f36e476d1ce3081879a4e|1560087179|1560087177; webim_unReadCount=%7B%22time%22%3A1560087189839%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',
	'Host': 'd.weibo.com',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Referer': 'https://weibo.com/u/3754667033/home',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}
html=requests.get(url,headers=headers).text
html = etree.HTML(html)
info=html.xpath('//*[@id="Pl_Discover_Pt6Rank__4"]/div/div/div[1]/div/ul/li[1]/div/div[2]/div[1]/div[1]/a[1]')
print(info)

# soup=BeautifulSoup(html,'html.parser')

# big_div=soup.find_all('script')[17]
# print(big_div)
# infos=big_div.find_all('div')
# print(infos)



