from selenium import webdriver
import time

browser = webdriver.Chrome()
url = 'https://www.kaishiba.com/project/more.html'
browser.get(url)
for i in range(10):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight) ')
    time.sleep(2)
all_li=browser.find_elements_by_class_name('programCard')
for i in all_li:
    li_name=i.find_element_by_class_name('cardBox').find_element_by_css_selector('a').text
    li_href=i.find_element_by_class_name('cardBox').find_element_by_css_selector('a').get_attribute('href')
    complete_li='名字:'+li_name+'\t' +'链接:'+li_href+'\n'
    print(complete_li)
browser.close()