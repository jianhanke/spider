import requests

def get_video_url():
	video_urls=[]
	headers={
		'authority':  'api.amemv.com',
		'scheme':	'https',
		'path'	: '/aweme/v1/aweme/post/?max_cursor=1550826067000&user_id=101899808690&count=10&retry_type=no_retry&mcc_mnc=46000&iid=65889539510&device_id=40324028687&ac=wifi&channel=lephone&aid=1128&app_name=aweme&version_code=530&version_name=5.3.0&device_platform=android&ssmix=a&device_type=ZUK+Z2151&device_brand=ZUK&language=zh&os_api=24&os_version=7.0&uuid=861907030886406&openudid=10d1ece26f4de43&manifest_version_code=530&resolution=1080*1920&dpi=480&update_version_code=5302&_rticket=1552618812618&ts=1552618812&js_sdk_version=1.12.2&as=a1e5e1b83c93dcf53b2933&cp=153dc85ec8b78b53e1KsSa&mas=0198253e9f556a74bd7600ff79156bccbecccc9c4c46ccac66c626',
		'cookie':	'sid_guard=69bf4323bbb201e5d0ce28d14383d07b%7C1552461916%7C5184000%7CSun%2C+12-May-2019+07%3A25%3A16+GMT',
		'cookie':	'uid_tt=790bd9db182c20122edbce1d74a56b81',
		'cookie':	'sid_tt=69bf4323bbb201e5d0ce28d14383d07b',
		'cookie':	'sessionid=69bf4323bbb201e5d0ce28d14383d07b',
		'cookie': 	'odin_tt=05b269847029eafa587a1d32f6568a0235734ef71effa138e43aa39fee1aa741494eb93d6922c703f5d49de746e16e6d',
		'cookie':	'qh[360]=1',
		'cookie':	'install_id=65889539510',
		'cookie':	'ttreq=1$e04a4330f5b4d23c908fa9d10b7388d94082e1e0',
		'accept-encoding':'gzip',
		'x-tt-token':	'0069bf4323bbb201e5d0ce28d14383d07bea6b956cd5026180bb6dbad4812fe941cc8c13883ddb37c354130112dcffd3432a',
		'sdk-version':	'1',
		'user-agent':	'com.ss.android.ugc.aweme/530 (Linux; U; Android 7.0; zh_CN; ZUK Z2151; Build/NRD90M; Cronet/58.0.2991.0)',
		'x-gorgon':	'03006cc000002b002d29a76ab99879dc87a383e78d9ae93b4b04',
		'x-khronos':	'1552622755',
	}														   
	url='https://api.amemv.com/aweme/v1/aweme/post/?max_cursor=1544353254000&user_id=6556303280&count=10&retry_type=no_retry&mcc_mnc=46000&iid=65889539510&device_id=40324028687&ac=wifi&channel=lephone&aid=1128&app_name=aweme&version_code=530&version_name=5.3.0&device_platform=android&ssmix=a&device_type=ZUK+Z2151&device_brand=ZUK&language=zh&os_api=24&os_version=7.0&uuid=861907030886406&openudid=10d1ece26f4de43&manifest_version_code=530&resolution=1080*1920&dpi=480&update_version_code=5302&_rticket=1552622755770&ts=1552622755&js_sdk_version=1.12.2&as=a1159218c36a2c246b2955&cp=21abc8523fb68044e1MsUa&mas=01d6973a386f5c013e30bf3ae3b598997facac9c4c466c2c4cc64c'
	r=requests.get(url=url,headers=headers).json()
	aweme_list=r['aweme_list']
	for i in aweme_list:
		video_url=i['video']['play_addr']['url_list'][0]
		video_urls.append(video_url)
	return video_urls
def get_video_info():
	num=1
	video_urls=get_video_url()
	for url in video_urls:
		video=requests.get(url).content
		path='抖音/{}.mp4'.format(num)
		num+=1
		with open(path,'wb') as f:
			f.write(video)
			f.close()

get_video_info()
