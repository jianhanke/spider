import urllib.request
import http.cookiejar
import requests
import http.cookiejar




cookie = http.cookiejar.MozillaCookieJar()
cookie.load('zhihu.txt', ignore_discard=True, ignore_expires=True)
url='https://www.zhihu.com/'
r = requests.get(url, cookies=cookie)
print(r.text)

