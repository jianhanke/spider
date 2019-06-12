import requests
from bs4 import BeautifulSoup
import bs4
import os
import re

def getHTMLText(url,timeout=10):
    try:
        user_agent = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)"
        headers = {"User-Agent":user_agent}
        r=requests.get(url,headers,timeout=10)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('连接错误')
def main(url):
    html=getHTMLText(url)
    soup=BeautifulSoup(html,'html.parser')
    texts=soup.find('div',attrs={'id':'content'})
     #find_all 返回的是一个列表 ,因为只找到了一个 所以要用 texts[0]
     # text属性，提取文本内容，清楚 <br>标签 $nbsq不是标签
    str2=str(texts).replace('<br/>','\n')
    return str2


def all(url):
    info=[]
    hrefs=[]
    titles=[]
    nums=0
    shu={}
    html=getHTMLText(url)
    soup=BeautifulSoup(html,'html.parser')
    info=soup.find_all('a',attrs={'style':''})
    root='G:\study_first\小说\ '
    for i in info:
        href=i.get('href')
        href='https://www.biquku.co/343678/'+href
        hrefs.append(href)
        title=i.string
        titles.append(title)
        nums+=1
    for i in range(465,nums):
        try:
            print(str(i))
            path_name=root+titles[i]+'.txt'
            url=hrefs[i]
            information=main(url)
            with open(path_name,'w',encoding='utf-8') as f:
                f.write(information)
                f.close()
            time.sleep(10)
        except:
            pass
            continue
url='https://www.biquku.co/343678/'
all(url)
