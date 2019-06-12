from selenium import webdriver
import time
import json

def cookie_login():   #用cookie登录
	broswer=webdriver.Chrome()
	broswer.get('http://weibo.com')
	with open('cookie_weibo.txt','r') as f:
		cookie=f.read()
	json_cookie=json.loads(cookie)
	# cookie = [item["name"] + "=" + item["value"] for item in json_cookie]
	# cookiestr = '; '.join(item for item in cookie)
	# print(cookiestr)
	for i in json_cookie:
		broswer.add_cookie(i)
	broswer.get('http://weibo.com')

def login():             #正常登录,自己输入密码，然后调用写入cookie操作 
	broswer=webdriver.Chrome();
	broswer.get('http://weibo.com');
	time.sleep(10);
	loginname=broswer.find_element_by_id('loginname')
	password=broswer.find_element_by_name('password')
	login_button=broswer.find_element_by_class_name('W_btn_a')
	loginname.send_keys('15239910806')
	password.send_keys('zeya/980931')
	login_button.click()
	time.sleep(10);
	get_cookie(broswer)
	# cookie_login()


	# get_all_url(broswer)
def get_all_url(broswer):    #登陆后,获取信息
	all_urls=[]
	baic_url=''
	time.sleep(20)
	all_div=broswer.find_elements_by_class_name('WB_info');
	for i in all_div:
		url=i.find_element_by_tag_name('a').get_attribute('href')
		url=baic_url+url
		all_urls.append(url)
		print(url)
	get_url_info(broswer,all_urls)

def get_url_info(broswer,all_info):
	print('第三个')
	for i in all_info:
		broswer.get(i)
		time.sleep(1)
		name=broswer.find_element_by_class_name('username').text
		tag_table=broswer.find_element_by_class_name('WB_innerwrap')
		follow=tag_table.find_elements_by_class_name('S_line1')[0].find_element_by_tag_name('strong').text
		fan=tag_table.find_elements_by_class_name('S_line1')[1].find_element_by_tag_name('strong').text
		count=tag_table.find_elements_by_class_name('S_line1')[2].find_element_by_tag_name('strong').text
		info='{0:{4}<20} {1:{5}<15} {2:{5}<15}{3:{5}} '.format(name,follow,fan,count,chr(12288),'')
		print(info)
def get_cookie(broswer):
	cookies=broswer.get_cookies()
	str_cookie=json.dumps(cookies)
	with open('cookie_weibo.txt','w') as f:
		f.write(str_cookie)

if __name__ == '__main__':
	login()
