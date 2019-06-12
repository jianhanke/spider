# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class HomePipeline(object):
    
    def __init__(self):
        self.db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='spiders')
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        sql=item['all_sql']
        self.cursor.execute(sql)
        self.db.commit()
        return item
        
    
