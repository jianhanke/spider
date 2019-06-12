import requests
import json
import time
import urllib3


url='https://music.163.com/eapi/videotimeline/get'
headers={
		
	'User-Agent':	'NeteaseMusic/4.3.5.1517983086(114);Dalvik/2.1.0 (Linux; U; Android 7.0; ZUK Z2151 Build/NRD90M)',
	'Content-Type':	'application/x-www-form-urlencoded',
	'Content-Length':	'1255',
	'Host':	'music.163.com',
	'Connection':	'Keep-Alive',
	'Accept-Encoding':	'gzip',
	'Cookie':	'osver=7.0; deviceId=ODYxOTA3MDMwODg2NDA2CTAyOjAwOjAwOjAwOjAwOjAwCTEwZDFlY2UyNmY0ZGU0MwkxMGQwM2E5ZA%3D%3D; appver=4.3.5; MUSIC_U=c7a510f23b6ef6241aaedf4acd797df5f8b4a15726a69ad02af3920de65f42263b6f2083904f52beece3e5430ab868a4e26dfc7a025ba269619714cdb628f904d864a181eb83ad77de39c620ce8469a8; versioncode=114; mobilename=ZUKZ2151; buildver=1517983086; resolution=1920x1080; channel=netease; os=android',
}
data={
	'osver':	'7.0',
	'deviceId':	'ODYxOTA3MDMwODg2NDA2CTAyOjAwOjAwOjAwOjAwOjAwCTEwZDFlY2UyNmY0ZGU0MwkxMGQwM2E5ZA%3D%3D',
	'appver':	'4.3.5',
	'MUSIC_U':	'c7a510f23b6ef6241aaedf4acd797df5f8b4a15726a69ad02af3920de65f42263b6f2083904f52beece3e5430ab868a4e26dfc7a025ba269619714cdb628f904d864a181eb83ad77de39c620ce8469a8',
	'versioncode':	'114',
	'mobilename':	'ZUKZ2151',
	'buildver':	'1517983086',
	'resolution':	'1920x1080',
	'channel':	'netease',
	'os':	'android',
}	

r=requests.post(url=url,headers=headers,data=data,verify=False)
print(r)