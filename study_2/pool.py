import requests
from selenium import webdriver
def Test1():
	proxy='171.37.158.151'
	proxies={
		'http':'http://'+proxy,
		'https':'https://'+proxy,
	}
	try:
		response=requests.get('http://httpbin.org/get',proxies=proxies)
		print(response.text)
	except requests.exceptions.ConnectionError as e:
		print('Error',e.args)
def Test3():
	proxy='127.0.0.1:9743'
	chrome_options=webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server=http://'+proxy)
	broswer=webdriver.Chrome()
	broswer.get('http://httpbin.org/get')
def Test2():
	response=requests.get('http://httpbin.org/get')
	print(response.text)
Test2()