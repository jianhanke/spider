from bs4 import BeautifulSoup
import requests
import re

r=requests.get("http://python123.io/ws/demo.html")
r.encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
#previous_sblings 只能用在for循环内
print(soup.find_all(string=''))