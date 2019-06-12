import pymysql
import time
import requests
from bs4 import BeautifulSoup

# db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306)
# cursor=db.cursor()
# cursor.execute('SELECT VERSION()')
# data=cursor.fetchone()
# print('Database version:',data)
# #cursor.execute('create database spiderss default character set utf8')
# data = cursor.fetchone()
# print(data)
# db.close()

# db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='spiders')
# cursor=db.cursor()
# sql='create table if not exists students(id varchar(255) not null,name varchar(255) not null,age int not null,primary key(id))'
# cursor.execute(sql)
# db.close()

# db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='spiders')
# cursor=db.cursor()
# id2='174804054'
# user='peisheng'
# age=20
# sql='insert into students(id,name,age) values(%s,%s,%s)'
# try:
# 	cursor.execute(sql,(id2,user,age))
# 	db.commit()
# except:
# 	db.rollback()
# db.close()

db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='spiders')
cursor=db.cursor()
sql = """CREATE TABLE {} (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )""".format('测试3')
cursor.execute(sql)


# str2='微博'
# str3=" '{}'".format(str2) 
# sql="insert into weibo (name,follows,fans,weibo) values ({},671,5433,5433);".format(str3)
# cursor.execute(sql)
# db.commit()
# # data={
# 	'id':'444244',
# 	'name':'Bob',
# 	'age':14,
# }
# table='students'
# keys=', '.join(data.keys())
# values=', '.join(['%s']*len(data))
# print(['$s']*len(data))
# print(keys)
# print(values)
# sql='insert into {table}({keys}) values({values})'.format(table=table,keys=keys,values=values)
# if cursor.execute(sql,tuple(data.values())):
# 	print('Successful')
# 	db.commit()


# db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='spiders')
# cursor=db.cursor()
# table='students'
# condition='age=20'
# sql='delete from {table} where {condition} '.format(table=table,condition=condition)
# cursor.execute(sql)
# db.commit()
# db.rollback()
# db.close()
# 

# time1=time.time()
# print(int (round(time1 * 1000)) )
# url='https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100206&refer_flag=0000015010_&from=feed&loc=avatar&is_all=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__28&id=1002065142723080&script_uri=/aynu1908&feed_type=0&page=1&pre_page=1&domain_op=100206&__rnd=1551583344123'
# heades={
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
# 	'X-Requested-With': 'XMLHttpRequest',
# 	'cookie':'SINAGLOBAL=3777574766988.6406.1532167660522; un=18337299830; wvr=6; UOR=hao.360.cn,weibo.com,www.baidu.com; SCF=AhZvAAq3SLZxNtwfS-9R_8m7xOI_dNXs7DQOBZ1UFQzeA8YIJ5TbzbwREsiudc8XWXtjAGCBl3hFT5OSuLzjMEo.; SUB=_2A25xf0TQDeRhGeVJ7lYX9inMyD-IHXVSDTEYrDV8PUNbmtAKLXLQkW9NT_Y8KlOM1sNsCBVapHPE5PnU1Db59RPg; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFav6PDx.POHbwqXgDejdoC5JpX5KMhUgL.FoeNSKBcSoM7e0e2dJLoIpjLxK-L1h.L1K2LxK-LB-qL1KzLxK-LB--LBKzt; SUHB=0RyqT9LwoeWkXI; ALF=1583114240; SSOLoginState=1551578240; Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; YF-V5-G0=2a21d421b35f7075ad5265885eabb1e4; wb_view_log_3754667033=1536*8641.25; YF-Page-G0=8ec35b246bb5b68c13549804abd380dc; _s_tentry=-; Apache=2248832963597.274.1551578290712; ULV=1551578290720:36:1:1:2248832963597.274.1551578290712:1551338755887; webim_unReadCount=%7B%22time%22%3A1551583340038%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D',

# }
# r=requests.get(url,headers=heades)
# if r.status_code==200:
# 	print(type(r))
# 	text=(r.json()['data'])
# 	text.find_all('')
# 	
