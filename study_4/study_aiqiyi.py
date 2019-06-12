from selenium import webdriver
import time
import json

def get_cookie():
	broswer=webdriver.Chrome()
	broswer.get('https://www.iqiyi.com/')
	time.sleep(30)
	cookie=broswer.get_cookies()
	str_cookie=json.dumps(cookie)
	with open('cookie_aiqiyi.txt','w') as f:
		f.write(str_cookie)
	
		
def cookie_login():
	broswer=webdriver.Chrome()
	broswer.get('https://www.iqiyi.com/')
	with open('cookie_aiqiyi.txt','r') as f:
		cookie=f.read()
	json_cookie=json.loads(cookie)
	for i in json_cookie:
		broswer.add_cookie(i)
	broswer.get('https://www.iqiyi.com')

if __name__ == '__main__':
	cookie_login()
