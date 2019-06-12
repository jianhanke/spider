import requests

url='http://jwglxt.aynu.edu.cn/xscj/Stu_MyScore_Drawimg.aspx?x=1&h=2&w=832&xnxq=20181&xn=2018&xq=1&rpt=0&rad=2&zfx=0'
headers={
		'cookie':'_gscu_996030535=51706420mkn7bt98; _gscbrs_996030535=1; ASP.NET_SessionId=qacxzeya124u0m55qowjia45',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
		'Host': 'jwglxt.aynu.edu.cn',
		'Referer': 'http://jwglxt.aynu.edu.cn/xscj/Stu_MyScore_rpt.aspx',
		'Origin':	'http://jwglxt.aynu.edu.cn',
		'Upgrade-Insecure-Requests': '1',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection' : 'keep-alive',
		'Content-Length':	'5747',
		'Cache-Control':	'max-age=0',
	}

r=requests.get(url=url,headers=headers).text
print(r)

