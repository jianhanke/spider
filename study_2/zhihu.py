import requests
from requests.packages import urllib3
import time
from selenium import webdriver
import tesserocr 
from PIL import Image

def Test_cookie():
	s=requests.Session()
	s.get('http://httpbin.org/cookies/set/number/123456789 ')
	r=s.get('http://httpbin.org/cookies') 
	print(r.text)
 
def Test_SSL():
	urllib3.disable_warnings()
	response=requests.get('https://www.12306.cn/index/',verify=False)
	print(response.status_code)

def Test_tab():
	browser = webdriver.Chrome()
	browser .get('https://www.baidu.com')
	browser .execute_script('window.open()') 
	print(browser.window_handles)
	browser.switch_to_window(browser.window_handles[1])
	browser.get('https://www.taobao.com')
	time.sleep(1)
	browser.switch_to_window(browser.window_handles[0])
	browser .get('https://python.org')
def Test2_tab():
	broswer=webdriver.Chrome()
	broswer.get('httP://www.baidu.com')
	broswer.execute_script('window.open()')
	print(broswer.window_handles)
	broswer.switch_to_window(broswer.window_handles[1])
	broswer.get('http://www.taobao.com')
	time.sleep(1)
	broswer.switch_to_window(broswer.window_handles[0])

def Test3():
	image = Image.open('code.jpg')
	result = tesserocr.image_to_text(image)
	print(result)
test3()