from bs4 import BeautifulSoup
import requests
import random

def get_ip_list(url, headers):#得到该页面的所有IP

    web_data = requests.get(url, headers=headers)#得到网页响应web_data
    soup = BeautifulSoup(web_data.text, 'lxml')#解析网页
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        httptype=str.lower(tds[5].text)#把类型换成小写
        hou=(tds[1].text + ':' + tds[2].text)
        proxy={}
        proxy[httptype]=hou
        ip_list.append(proxy)
    return ip_list
    
#从众多的IP中随机选一个出来使用
def get_random_ip(ip_list):
    proxy_ip = random.choice(ip_list)
    return proxy_ip

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    #给请求指定一个请求头来模拟浏览器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    ip_list = get_ip_list(url, headers=headers)#调用get_ip_list函数得到IP列表
    proxies = get_random_ip(ip_list)#调用函数get_random_ip从IP列表中随机取用
    print(proxies)


