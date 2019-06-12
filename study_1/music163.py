from selenium import webdriver
import json

def page_all(all_urls):
	nums=0
	broswer=webdriver.Chrome()
	for url in all_urls:
		broswer.get(url)
		broswer.switch_to.frame('contentFrame')
		# for i in range(100):
		# 	broswer.execute_script('window.scrollTo(0,document.body.scrollHeight)')
		all_ul=broswer.find_element_by_class_name('m-cvrlst')
		all_li=all_ul.find_elements_by_css_selector('li')
		nums+=len(all_li)
		print("目前为止共计歌手:"+str(nums))
		for i in all_li:
			singer_href=i.find_element_by_class_name('nm').get_attribute('href')
			singer_name=i.find_element_by_class_name('nm').get_attribute('title')
			singer_name=singer_name.replace('的音乐',' ')
			complete_singer="{0:{2}<40}\t{1:{2}<10}".format(singer_href,singer_name,' ')
			print(complete_singer)
	broswer.close()
def main():
	all_urls=[]
	num1=0
	num2=0
	for j in range(1001,1004):
		num1=j
		for i in range(65,91):
			num2=i
			url='https://music.163.com/#/discover/artist/cat?id={}&initial={}'.format(num1,num2)
			all_urls.append(url)
	page_all(all_urls)


# def main2():
# 	url='https://music.163.com/#/discover/artist/'
# 	broswer=webdriver.Chrome()
# 	broswer.get(url)
# 	broswer.switch_to.frame('contentFrame')
# 	first_ul=broswer.find_element_by_class_name("m-cvrlst")
# 	second_ul=first_ul.find_elements_by_class_name('fafda')
# 	print(second_ul)
# main2()
# def main3():
# 	str1="{'Name': 'Zara', 'Age': 7, 'Class': 'First'}"
# 	user_dict=eval(str1)
# 	print(isinstance(user_dict,dict))

def ceshi():
	string1=''
	url='https://music.163.com/#/discover/artist/'
	broswer=webdriver.Chrome()
	broswer.get(url)
	string1=broswer.find_element_by_tag_name('em')
	print(string1.text)
def ceshi2():
	list2=[]
	if (len(list2)>0):
		print(1)
	else:
		print(2)
def ceshi3():
	url='https://www.manhuatai.com/douluodalu/528.html'
	broswer=webdriver.Chrome()
	broswer.get(url)
	options=broswer.find_elements_by_tag_name('option')
	print(options)
ceshi3()
