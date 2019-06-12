from bs4 import BeautifulSoup
import requests
import random

class GetProxy():

    def get_ip_list(self,url, headers):#得到该页面的所有IP
        web_data = requests.get(url, headers=headers)#得到网页响应web_data
        soup = BeautifulSoup(web_data.text, 'lxml')#解析网页
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            httptype=str.lower(tds[5].text)#把类型换成小写
            hou=(httptype+"://"+tds[1].text + ':' + tds[2].text)
            proxy2={}
            proxy2[httptype]=hou
            ip_list.append(proxy2)
        return ip_list
    #从众多的IP中随机选一个出来使用
    def get_random_ip(self,ip_list):

        proxy_ip = random.choice(ip_list)
        return proxy_ip

    def get_proxy(self):
        url = 'http://www.xicidaili.com/nn/'
        url2='https://2eeett.com/intr/d52c8d82b8edb231'
        #给请求指定一个请求头来模拟浏览器
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        ip_list = self.get_ip_list(url, headers=headers)#调用get_ip_list函数得到IP列表
        return ip_list
        # for i in range(10):
        # proxies = self.get_random_ip(ip_list)#调用函数get_random_ip从IP列表中随机取用
        # return proxies

            # print(proxies)
            # r=requests.get(url=url2,headers=headers,proxies=proxies,timeout=30)
            # print(r.status_code)



