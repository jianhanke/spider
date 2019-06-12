import requests

url="http://m.ip138.com/ip.asp?ip="
r=requests.get(url+'202.204.80.112')
r.encoding=r.apparent_encoding
print(r.status_code)
print(r.text)
