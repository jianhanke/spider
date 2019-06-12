from selenium import webdriver
import json
import time

broswer=webdriver.Chrome()
broswer.get('https://www.weibo.com')
time.sleep(10)
user_id=broswer.find_elements_by_class_name('W_input ')[1]
user_pwd=broswer.find_elements_by_class_name('W_input ')[2]
user_button=broswer.find_elements_by_class_name('W_btn_a')[0]
user_id.send_keys('18337299830')
user_pwd.send_keys('zhao/980931')
user_button.click()
broswer.get('https://www.weibo.com')	
print(broswer.page_source)