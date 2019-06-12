import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import re
import urllib
import time

def analysis(url,broswer):
	broswer.get(url)
	select   =broswer.find_element_by_class_name('mh_select')
	option    =select.find_elements_by_tag_name('option')
	div=broswer.find_element_by_class_name('mh_headpager')
	title=broswer.find_element_by_tag_name('h1').find_element_by_tag_name('strong').text
	total_page=len(option)
	img_url=broswer.find_element_by_class_name('mh_comicpic').find_element_by_tag_name('img').get_attribute('src').replace('webp','jpg')

	root_name=broswer.find_element_by_class_name('mh_wrap').find_elements_by_tag_name('a')[3].get_attribute('title')
	root='G://{}/'.format(root_name)
	print(root)
	if not os.path.exists(root):
		os.mkdir(root)
	title=title.replace(root_name,'')		
	root2=root+title+'/'
	if not os.path.exists(root2):
		os.mkdir(root2)

	for i in range(1,total_page):
		new_jpg=str(i)+'.jpg'
		num_jpg=re.findall(r'\d+.jpg',img_url)[0]
		img_url=img_url.replace(num_jpg,new_jpg)
		img=requests.get(img_url)
		path=root2+new_jpg
		print(title)
		print(path)
		with open(path,'wb') as f:
			f.write(img.content)
			f.close()

def main():
	all_urls=[]
	broswer=webdriver.Chrome()
	url='https://www.manhuatai.com/dazhuzai/'
	broswer.get(url)
	ul=broswer.find_element_by_id('topic1')
	li_url=ul.find_elements_by_tag_name('a')
	li_url.reverse()
	for i in li_url:
		li_url=i.get_attribute('href')
		all_urls.append(li_url)
	for i in all_urls:	
		analysis(i,broswer)
main()
