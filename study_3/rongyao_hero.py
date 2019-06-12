import requests
import os

def Get_Hero():
	url='http://gamehelper.gm825.com/wzry/hero/list?channel_id=90033a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.7&version_code=1207&cuid=A48A257A54B2C2A68280A5AFC391C2A8&ovr=7.0&device=ZUK_ZUK+Z2151&net_type=1&client_id=Nnxv07YO1GMwOtYOJtPXMQ%3D%3D&info_ms=a1GWx2Q8jsK3MX4PsKZz4A%3D%3D&info_ma=yF7qVwYRkRk38q1Oyn7%2B8dVwn4nz5EssrEF0uM4MPIs%3D&mno=0&info_la=A70eRaD82AqG%2FQr%2BhadLYg%3D%3D&info_ci=A70eRaD82AqG%2FQr%2BhadLYg%3D%3D&mcc=0&clientversion=&bssid=vuhoq1I9eJw1%2F04Qx%2FGZyJ%2B4Zk0yBacOoyB7jay42WI%3D&os_level=24&os_id=10d1ece26f4de43&resolution=1080_1920&dpi=480&client_ip=192.168.1.112&pdunid=10d03a9d'
	r=requests.get(url).json()
	Get_Hero_Info(r)

def Get_Hero_Info(r):
	all_hero=r['list']
	print(type(all_hero))
	for i in all_hero:
		print('测试')
		print(i)
		hero_name=i['title']
		hero_url=i['cover']
		Get_Image(hero_name,hero_url)
		
def Get_Image(hero_name,hero_url):
	file_postfix=os.path.splitext(hero_url)[-1] 
	hero_image=requests.get(hero_url).content
	path='王者荣耀/'+hero_name	+file_postfix
	with open(path,'wb') as f:
		f.write(hero_image)
		f.close()

def Get_Hero_2(): #英雄装备
	url='http://gamehelper.gm825.com/wzry/equip/list?channel_id=90033a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.7&version_code=1207&cuid=A48A257A54B2C2A68280A5AFC391C2A8&ovr=7.0&device=ZUK_ZUK+Z2151&net_type=1&client_id=Nnxv07YO1GMwOtYOJtPXMQ%3D%3D&info_ms=a1GWx2Q8jsK3MX4PsKZz4A%3D%3D&info_ma=yF7qVwYRkRk38q1Oyn7%2B8dVwn4nz5EssrEF0uM4MPIs%3D&mno=0&info_la=A70eRaD82AqG%2FQr%2BhadLYg%3D%3D&info_ci=A70eRaD82AqG%2FQr%2BhadLYg%3D%3D&mcc=0&clientversion=&bssid=vuhoq1I9eJw1%2F04Qx%2FGZyJ%2B4Zk0yBacOoyB7jay42WI%3D&os_level=24&os_id=10d1ece26f4de43&resolution=1080_1920&dpi=480&client_ip=192.168.1.112&pdunid=10d03a9d'
	r=requests.get(url).json()
	print(r)
	Get_Hero_Info(r)
def Get_Hero_3():
	url='http://gamehelper.gm825.com/wzry/inscription/list?channel_id=90033a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.7&version_code=1207&cuid=A48A257A54B2C2A68280A5AFC391C2A8&ovr=7.0&device=ZUK_ZUK+Z2151&net_type=1&client_id=Nnxv07YO1GMwOtYOJtPXMQ%3D%3D&info_ms=a1GWx2Q8jsK3MX4PsKZz4A%3D%3D&info_ma=yF7qVwYRkRk38q1Oyn7%2B8dVwn4nz5EssrEF0uM4MPIs%3D&mno=0&info_la=A70eRaD82AqG%2FQr%2BhadLYg%3D%3D&info_ci=A70eRaD82AqG%2FQr%2BhadLYg%3D%3D&mcc=0&clientversion=&bssid=vuhoq1I9eJw1%2F04Qx%2FGZyJ%2B4Zk0yBacOoyB7jay42WI%3D&os_level=24&os_id=10d1ece26f4de43&resolution=1080_1920&dpi=480&client_ip=192.168.1.112&pdunid=10d03a9d'
	r=requests.get(url).json()
	print(r)
def Get_Runes():
	url='http://gamehelper.gm825.com/wzry/inscription/list?channel_id=90033a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.7&version_code=1207&cuid=A48A257A54B2C2A68280A5AFC391C2A8&ovr=7.0&device=ZUK_ZUK+Z2151&net_type=1&client_id=Nnxv07YO1GMwOtYOJtPXMQ%3D%3D&info_ms=a1GWx2Q8jsK3MX4PsKZz4A%3D%3D&info_ma=yF7qVwYRkRk38q1Oyn7%2B8dVwn4nz5EssrEF0uM4MPIs%3D&mno=0&info_la=A70eRaD82AqG%2FQr%2BhadLYg%3D%3D&info_ci=A70eRaD82AqG%2FQr%2BhadLYg%3D%3D&mcc=0&clientversion=&bssid=vuhoq1I9eJw1%2F04Qx%2FGZyJ%2B4Zk0yBacOoyB7jay42WI%3D&os_level=24&os_id=10d1ece26f4de43&resolution=1080_1920&dpi=480&client_ip=192.168.1.112&pdunid=10d03a9d'
	r=requests.get(url).json()
	all_runes=r['list']
	Get_Runes_Info(all_runes)
	
def Get_Runes_Info(all_runes):
	for i in all_runes:
		name=i['name']
		level=i['level']
		url=i['icon']
		total_name=name+level
		Get_Runes_Image(total_name,url)
def Get_Runes_Image(total_name,url):
	image=requests.get(url).content
	postfix=os.path.splitext(url)[-1]
	path='符文/'+total_name+postfix
	with open(path,'wb') as f:
		f.write(image)

Get_Runes()