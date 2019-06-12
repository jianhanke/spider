from bs4 import BeautifulSoup
import requests
import random
from fake_useragent import UserAgent

class GetIp():
  def get_ip_list(self,url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        httptype=str.lower(tds[5].text)#把类型换成小写
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list
  def get_random_ip(self,ip_list):
    ip=random.choice(ip_list)
    proxies={
      'http':ip,
      'https':ip,
    }
    return proxies

  def __init__(self):
    url = 'http://www.xicidaili.com/nn/'
    url2='http://httpbin.org/get'
    #url2='http://httpbin.org/get'
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    ip_list = self.get_ip_list(url, headers=headers) 
    for i in range(20):
        ua = UserAgent().random
        proxies=self.get_random_ip(ip_list)
        print(proxies)
        try:
            r=requests.get(url=url2,headers=ua,proxies=proxies,timeout=30)
            print(r.text)
        except:
            print('测试')

get=GetIp()
