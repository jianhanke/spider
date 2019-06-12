from selenium import webdriver
import time
import json

all_urls=[]
broswer=webdriver.Chrome()
broswer.get('http://weibo.com')
with open('cookie.txt','r') as f:
	cookie=f.read()
json_cookie=json.loads(cookie)
for i in json_cookie:
	broswer.add_cookie(i)
time.sleep(2)
broswer.get('http://weibo.com')

for i in range(1,6):
	broswer.get('https://weibo.com/p/1005052244367010/follow?page={}#Pl_Official_HisRelation__59'.format(i))
	time.sleep(2)
	all_div=broswer.find_elements_by_class_name('info_name')
	for i in all_div:
		url=i.find_element_by_tag_name('a').get_attribute('href')
		all_urls.append(url)
for i in all_urls:
	print(i)
for j in all_urls:
	all_info=[]
	broswer.get(j)
	time.sleep(1)
	try:
		all_info=broswer.find_elements_by_tag_name('strong')
		user_name=broswer.find_element_by_class_name('username').text  #待测试
	except:
		pass
	if (len(all_info)>0):
		follow_perple=all_info[0].text
		total_fans=all_info[1].text
		total_weibo=all_info[2].text
		one_person='{0:{4}<20}{1:{5}<15}{2:{5}<15}{3:{5}<15}'.format(user_name,follow_perple,total_fans,total_weibo,chr(12288),' ')
		print(one_person)