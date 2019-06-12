import requests
import os

url="https://www.xlxy.edu.cn/ewebeditor/uploadfile/2017/0000/20170410.mp4"
root="D://picture//"
path=root+'xinlian.mp4'
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r=requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
			pritn("文件已存在")
except:
	print("爬取失败")
	print(r.raise_for_status)