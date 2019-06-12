import requests

kv={'wd':'Python'}
r=requests.get("http://so.com/s",params=kv)
print(r.raise_for_status)
print(r.request.url)
print(len(r.text))