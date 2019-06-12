import pymongo
from flask import Flask,g


client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
#db=client['test']  两种连接数据库方法

collection=db.ceshi2
#collection=db['ceshi']			两种连接表的方法

student={
	'id':'20170101',
	'name':'Jordan',
	'age':'20',
	'gender':'male'
}
student2={
	'id':'20170202',
	'name':'Mike',
	'age':21,
	'gender':'male'
}
resulst=collection.insert_many([student,student2])

result=collection.find_one({'name':'Mike'})
print(type(result))
print(result)
