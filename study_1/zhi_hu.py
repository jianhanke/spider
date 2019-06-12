from selenium import webdriver
import time

broswer=webdriver.Chrome()
broswer.get('http://www.zhihu.com')
login_div=broswer.find_element_by_class_name('SignContainer-switch')
login_button1=login_div.find_element_by_css_selector('span')
login_button1.click()
erweima=broswer.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[5]/span[1]/button')
erweima.click()
time.sleep(15)
all_div=broswer.find_elements_by_class_name('Feed')
for div in all_div:
	li=div.find_element_by_class_name('ContentItem')
	dic=li.get_attribute('data-zop')
	info=eval(dic)
	print(info['title'])

# user_name=broswer.find_element_by_name('username')
# user_name.send_keys('18337299830')
# user_password=broswer.find_element_by_name('password')
# user_password.send_keys('zhao/980931')
# login_button2=broswer.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button')
# login_button2.click()
