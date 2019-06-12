from selenium import webdriver
import time


broswer=webdriver.Chrome()
broswer.get('http://weibo.com')
time.sleep(30)
for i in range(10):
	broswer.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(3)
all_div=broswer.find_elements_by_class_name('WB_info')
all_urls=[]
all_info=[]
for i in all_div:
	href=i.find_element_by_tag_name('a').get_attribute('href')
	all_urls.append(href)
for j in all_urls:
	broswer.get(j)
	time.sleep(1)
	all_info=broswer.find_elements_by_tag_name('strong')
	user_name=broswer.find_element_by_class_name('username').text  #待测试
	if (len(all_info)>0):
		follow_perple=all_info[0].text
		total_fans=all_info[1].text
		total_weibo=all_info[2].text
		one_person='{0:{4}<20}{1:{5}<15}{2:{5}<15}{3:{5}<15}'.format(user_name,follow_perple,total_fans,total_weibo,chr(12288),' ')
		print(one_person)