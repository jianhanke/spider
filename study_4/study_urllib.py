import urllib.request

def ceshi_url():
	response =urllib.request.urlopen('https://www.baidu.com/')
	print(response.read().decode('utf-8'))

def ceshi_date():
	data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
	print(data)
	response = urllib.request.urlopen('https://www.baidu.com/', data=data)
	print(response.read())

if __name__ == '__main__':
	ceshi_date()