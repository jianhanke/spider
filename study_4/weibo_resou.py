from selenium import webdriver
import time
import json

def cookie_login():
	broswer=webdriver.Chrome()
	broswer.get('http://weibo.com')
	with open('cookie_weibo.txt','r') as f:
		cookie=f.read()
	json_cookie=json.loads(cookie)
	for i in json_cookie:
		broswer.add_cookie(i)
	broswer.get('http://weibo.com')
	return broswer
def get_info(broswer):
	broswer.get('https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6')  #热搜网址
	all_infos=broswer.find_elements_by_class_name('td-02')
	for i in range(10):
		info=all_infos[i]
		info_text=info.find_element_by_tag_name('a').text
		print(info_text)

if __name__ == '__main__':
	broswer=cookie_login()
	get_info(broswer)