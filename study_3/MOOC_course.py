import requests
from selenium  import webdriver
import time

broswer=webdriver.Chrome()
start_url='https://www.icourse163.org/category/computer'
broswer.get(start_url)
all_num=broswer.find_elements_by_class_name('ux-pager_itm')[-1].text

time.sleep(3)
for i in range(int(all_num)):
	all_course=broswer.find_elements_by_class_name('cnt')
	for i in all_course:
		course_name=i.find_element_by_class_name('u-course-name').text
		teacher_name=i.find_element_by_class_name('t2').find_elements_by_tag_name('a')[1].text
		course_introduce=i.find_element_by_class_name('p5').text
		course_info=course_name+','+teacher_name+','+course_introduce
	broswer.execute_script('window.scrollTo(0, document.body.scrollHeight)')
	last_button=broswer.find_elements_by_class_name('ux-pager_btn')[-1]
	last_button.click()
	time.sleep(2)
	# all_course=broswer.find_elements_by_class_name('u-course-name')
	# for j in all_course:
	# 	print(j.text)



# ul=broswer.find_element_by_class_name('ux-pager')
# time.sleep(1)
# all_url=ul.find_elements_by_class_name('ux-pager_itm')
# for i in all_url:
# 	time.sleep(1)
# 	i.click()

# for i in range(1,int(all_num)+1):
# 	all_course=broswer.find_elements_by_class_name('u-course-name')
# 	for j in all_course:
# 		print(j.text)
# 	last_button.click()
# 	time.sleep(1)


# ul=broswer.find_element_by_class_name('ux-pager')


# last_button.click()
# for i in range(1,int(all_num)+1):
# 	url='https://www.icourse163.org/category/computer#?type=30&orderBy=0&pageIndex={}'.format(i)
# 	print(url)
# 	broswer.get(url)
# 	time.sleep(4)
# 	all_course=broswer.find_elements_by_class_name('u-course-name')
# 	for j in all_course:
# 		print(j.text)







	