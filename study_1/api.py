import requests
import json

type_tele_url='http://api.avatardata.cn/TVTime/Query?key=96f738688904441596e1e9cb21bc41c9'
actual_url='http://api.avatardata.cn/TVTime/LookUp?key=96f738688904441596e1e9cb21bc41c9&pId=1'
list_url='http://api.avatardata.cn/TVTime/TVlist?key=96f738688904441596e1e9cb21bc41c9&code=cctv1&date='

def actual():
    r=requests.get(actual_url)
    response_dict=r.json()['result']
    b=json.dumps(response_dict)
    d=json.loads(b)
    for c in d:
        actual_name=c['channelName']
        actual_id=c['pId']
        actual_name2=c['rel']
        actual_url2=c['url']
        str3='{0:{4}<10}{1:{4}<10}{2:{4}<20}{3:{4}<20}'.format(actual_name,actual_id,actual_name2,actual_url2,' ',chr(12288))
        print(str3)
def list():
    r=requests.get(list_url)
    response_dict=r.json()['result']
    b=json.dumps(response_dict)
    c=json.loads(b)
    for i in c:
        time=i['time']
        pname=i['pName']
        str1='{0:{2}<20}\t{1:{3}<20}'.format(time,pname,' ',chr(12288))
        print(str1)
def type():
    r=requests.get(type_tele_url)
    response_dict=r.json()['result']
    b=json.dumps(response_dict)
    c=json.loads(b)
    for i in c:
        tele_id=i['id']
        tele_name=i['name']
        str2='{0:{2}<10}\t{1:{3}<10}'.format(tele_id,tele_name,' ',chr(12288))
        print(str2)
actual()