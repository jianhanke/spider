from selenium import webdriver
import time
import json
import pymysql


def Sign_in():  #登录方法 用谷歌登录，返回谷歌 控制权
	broswer=webdriver.Chrome()
	broswer.get('http://weibo.com')
	with open('cookie.txt','r') as f:
		cookie=f.read()
	json_cookie=json.loads(cookie)
	for i in json_cookie:
		broswer.add_cookie(i)
	time.sleep(2)
	broswer.get('http://weibo.com')
	return broswer

def db_mange():   #管理数据库方法，返回 db,cursor
	db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='spiders')
	cursor=db.cursor()
	return db,cursor
	
def get_fan_info(broswer):   #获取某个用户的粉丝前五页信息
	broswer=Sign_in()
	all_urls=[]
	all_sql=[]
	for i in range(1,6):
		broswer.get('https://weibo.com/p/1005052244367010/follow?page={}#Pl_Official_HisRelation__59'.format(i))
	time.sleep(2)
	all_div=broswer.find_elements_by_class_name('info_name')
	for i in all_div:
		url=i.find_element_by_tag_name('a').get_attribute('href')
		all_urls.append(url)
	for j in all_urls:
		all_info=[]
		broswer.get(j)
		time.sleep(1)
		try:
			all_info=broswer.find_elements_by_tag_name('strong')
			user_name=broswer.find_element_by_class_name('username').text  #待测试
			user_name=" '{}'".format(user_name) 
		except:
			pass
		if (len(all_info)>0):
			follow_perple=all_info[0].text
			total_fans=all_info[1].text
			total_weibo=all_info[2].text
			sql='insert into weibo (name,follows,fans,weibo) values ({},{},{},{})'.format(user_name,follow_perple,total_weibo,total_weibo)
			all_sql.append(sql)
	return all_sql

def get_home_info(broswer):  #获取自己首页，发表动态的用户的粉丝信息
	all_sql=[]
	all_urls=[]
	all_info=[]
	broswer.get('http://weibo.com')
	time.sleep(5)
	for i in range(1):
		broswer.execute_script('window.scrollTo(0,document.body.scrollHeight)')
		time.sleep(1)
	all_div=broswer.find_elements_by_class_name('WB_info')
	for i in all_div:
		href=i.find_element_by_tag_name('a').get_attribute('href')
		all_urls.append(href)
	for j in all_urls:
		broswer.get(j)
		time.sleep(1)
		all_info=broswer.find_elements_by_tag_name('strong')
		user_name=broswer.find_element_by_class_name('username').text  #待测试
		user_name=" '{}'".format(user_name) 
		if (len(all_info)>0):
			follow_perple=all_info[0].text
			total_fans=all_info[1].text
			total_weibo=all_info[2].text
			sql='insert into weibo (name,follows,fans,weibo) values ({},{},{},{})'.format(user_name,follow_perple,total_weibo,total_weibo)
			all_sql.append(sql)
	return all_sql
def get_cookies():
	##
					
def main():   #运行方法，测试运行
	broswer=Sign_in()
	#info_list=get_info()
	db,cursor=db_mange()
	#all_sql=get_fan_info(broswer)
	all_sql=get_home_info(broswer)
	for sql in all_sql:
		cursor.execute(sql)
		db.commit()
main()



	