from selenium import webdriver
import time
import json
# js='window.open("https://weibo.com");'
# broswer.execute_script(js)
# windows=broswer.window_handles
# broswer.switch_to.window(windows[1])

broswer=webdriver.Chrome()
broswer.get('http://weibo.com')
# time.sleep(20)
# cookie=broswer.get_cookies()
# str_cookie=json.dumps(cookie)
# with open ('cookie.txt','w')as f:
# 	f.write(str_cookie)
# broswer.close()
with open('cookie.txt','r') as f:
	cookie=f.read()
json_cookie=json.loads(cookie)
for i in json_cookie:
	broswer.add_cookie(i)
time.sleep(2)
broswer.get('http://weibo.com')
#broswer.refresh()  #刷新方法，但是不管用

# js='window.open("https://weibo.com");'
# broswer.execute_script(js)
# windows=broswer.window_handles
# broswer.switch_to.window(windows[1])

# with open('cookie.txt','w') as f:
# 	f.write(json.dumps(cookies))

# print(type(cookies))


# broswer2=webdriver.Chrome()
# broswer2.get('http://weibo.com')
# for cookie in cookies:
# 	broswer2.add_cookie(cookie)
# time.sleep(10)
# broswer2.refresh()

# print(cookie)
# print(type(cookie))

# str_cookie=json.dumps(cookie)
# print(str_cookie)
# print(type(str_cookie))

# json_cookie=json.loads(str_cookie)
# print(type(json_cookie))
