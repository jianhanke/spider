import requests
import json

def ceshi_response():
	response=requests.get('https://www.baidu.com')
	print(response.content.decode('utf-8'))

def ceshi_post():
	data={
		"name":"zhaofan",
		"age":22
	}
	res=requests.post('http://httpbin.org/post',params=data)
	print(res.text)
	print(res.url)
def ceshi_json():
	response = requests.get("http://httpbin.org/get")
	print(type(response.text))
	print(response.json())
	json_str=json.loads(response)
	print(json_str)

def ceshi_upload():
	files={"files":open("1.png","rb")}
	response=requests.post('http://httpbin.org/get')
	print(response.text)
def get_cookie():
	response=requests.get('https://www.baidu.com')
	print(response.cookies)
	for k,v in response.cookies.items():
		print(k+":"+v)
	print(response.cookies.items())
def ceshi_session():
	s = requests.Session()  #s 相当于一个request 做会话维持
	s.get("http://httpbin.org/cookies/set/number/123456")
	response = s.get("http://httpbin.org/cookies")
	print(response.text)
	# response2=s.get('https://www.baidu.com')   
	# print(response2.text)
	response3=requests.get("http://httpbin.org/cookies")
	print(response3.text)
def ceshi_proxies():

	proxies={
		'http':'112.85.130.61:9999',
		'https':'112.85.130.61:9999',
	}
	res=requests.get("http://httpbin.org/get",proxies=proxies)
	print(res.text)


ceshi_proxies()