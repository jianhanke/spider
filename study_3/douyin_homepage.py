import requests

headers={
		'authority':  'api-eagle.amemv.com',
		'scheme':	'https',
		'path'	: '/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=-1&count=6&volume=0.4666666666666667&pull_type=2&need_relieve_aweme=0&filter_warn=0&req_from&is_cold_start=0&longitude=114.356568&latitude=36.084549&ts=1552644254&js_sdk_version=1.12.2&app_type=normal&os_api=24&device_platform=android&device_type=ZUK%20Z2151&iid=65889539510&ssmix=a&manifest_version_code=530&dpi=480&uuid=861907030886406&version_code=530&app_name=aweme&version_name=5.3.0&openudid=10d1ece26f4de43&device_id=40324028687&resolution=1080*1920&os_version=7.0&language=zh&device_brand=ZUK&ac=wifi&update_version_code=5302&aid=1128&channel=lephone&_rticket=1552644255479&mcc_mnc=46000&as=a135c7d84e39ec58db4633&cp=7d9dc953efbb8384e1IwQa&mas=0129b06e6b518bb34a55d09b8642a9dc55cccc6c2c46261cacc6a6',
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
		'x-ss-req-ticket':	'1552644255465',
		'user-agent':	'com.ss.android.ugc.aweme/530 (Linux; U; Android 7.0; zh_CN; ZUK Z2151; Build/NRD90M; Cronet/58.0.2991.0)',
		'x-gorgon':	'03006cc08000a6bc0bf8270baf89682005e69ce6a7f52394f391',
					#'03006cc0800011ff8598270baf89682005e69ce6a7f523ebcb80'
					#'03006cc0800073b0536f270baf89682005e69ce6a7f523ebebc4
					#'03006cc080005cdcebd0270baf89682005e69ce6a7f523eb57fb'
		'x-khronos':	'1552646698',
		
	}	
url='https://api-eagle.amemv.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=-1&count=6&volume=0.8&pull_type=2&need_relieve_aweme=0&filter_warn=0&req_from&is_cold_start=0&longitude=114.356568&latitude=36.084549&ts=1552646697&js_sdk_version=1.12.2&app_type=normal&os_api=24&device_platform=android&device_type=ZUK%20Z2151&iid=65889539510&ssmix=a&manifest_version_code=530&dpi=480&uuid=861907030886406&version_code=530&app_name=aweme&version_name=5.3.0&openudid=10d1ece26f4de43&device_id=40324028687&resolution=1080*1920&os_version=7.0&language=zh&device_brand=ZUK&ac=wifi&update_version_code=5302&aid=1128&channel=lephone&_rticket=1552646698384&mcc_mnc=46000&as=a1c5388859e26ca22b0699&cp=8a25c05c92b4852de1Ymaq&mas=0176297766afb2de824aaa1fd725e585d79c9c6c0c464c4c86c66c'
r=requests.get(url,headers=headers).json()

aweme_list=r['aweme_list']
video_urls=[]
for i in aweme_list:
	video_url=i['video']['play_addr']['url_list'][0]
	print(video_url)
	video_urls.append(video_url)