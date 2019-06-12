import requests
import time

url='https://api.amemv.com/aweme/v1/aweme/stats/?os_api=24&device_platform=android&device_type=ZUK+Z2151&iid=65889539510&ssmix=a&manifest_version_code=530&dpi=480&uuid=861907030886406&version_code=530&app_name=aweme&version_name=5.3.0&openudid=10d1ece26f4de43&device_id=40324028687&resolution=1080*1920&os_version=7.0&language=zh&device_brand=ZUK&ac=wifi&update_version_code=5302&aid=1128&channel=lephone&_rticket=1552643624666&mcc_mnc=46000&ts=1552643625&js_sdk_version=1.12.50&as=a195a73839921c368b4799&cp=7322c45c91b58a63e1MyUg&mas=01da1020d8f0f7966db498994ebae795ba9c9cec2c461c6cccc68c'

json={
	"extra": {
		"now": '1552541474000'
	},
	"log_pb": {
		"impr_id": "20190314133114010019030067338102"
	},
	"status_code": '0'
}
cookie={
	'sid_guard': '69bf4323bbb201e5d0ce28d14383d07b%7C1552461916%7C5184000%7CSun%2C+12-May-2019+07%3A25%3A16+GMT',
	'uid_tt':	'790bd9db182c20122edbce1d74a56b81',
	'sid_tt':	'69bf4323bbb201e5d0ce28d14383d07b',
	'sessionid':	'69bf4323bbb201e5d0ce28d14383d07b',
	'odin_tt':	'05b269847029eafa587a1d32f6568a0235734ef71effa138e43aa39fee1aa741494eb93d6922c703f5d49de746e16e6d',
	'install_id':	'65889539510',
	'ttreq':	'1$e04a4330f5b4d23c908fa9d10b7388d94082e1e0',
	'qh[360]':	'1'
}
headers={
	'X-SS-STUB':	'290FB7D41B1808A9605D69D06D118AEB',
	'Accept-Encoding'	:'gzip',
	'sdk-version' : '1',
	'Cookie':	'qh[360]=1; sid_guard=69bf4323bbb201e5d0ce28d14383d07b%7C1552461916%7C5184000%7CSun%2C+12-May-2019+07%3A25%3A16+GMT; uid_tt=790bd9db182c20122edbce1d74a56b81; sid_tt=69bf4323bbb201e5d0ce28d14383d07b; sessionid=69bf4323bbb201e5d0ce28d14383d07b; odin_tt=05b269847029eafa587a1d32f6568a0235734ef71effa138e43aa39fee1aa741494eb93d6922c703f5d49de746e16e6d; install_id=65889539510; ttreq=1$e04a4330f5b4d23c908fa9d10b7388d94082e1e0',
	'x-tt-token':	'0069bf4323bbb201e5d0ce28d14383d07bea6b956cd5026180bb6dbad4812fe941cc8c13883ddb37c354130112dcffd3432a',
	'X-Gorgon':	'03742f2b00001e1f756f6e308297afc18719ff0577ea0069acc3',
	'X-Khronos':	'1552541477',
	'Content-Type'	: 'application/x-www-form-urlencoded; charset=UTF-8',
	'Content-Length':	'477',
	'Host':	'api.amemv.com',
	'Connection':	'Keep-Alive',
	'User-Agent': 'okhttp/3.10.0.1',
}
r=requests.get(url,cookies=cookie,headers=headers).json()
print(r)