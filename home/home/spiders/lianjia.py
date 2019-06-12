# -*- coding: utf-8 -*-
import scrapy
import pymysql
import math
from bs4 import BeautifulSoup
from home.items import HomeItem
import re
import sqlite3

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'

    # url='https://ty.fang.lianjia.com/loupan/pg1'
    # start_urls = []
    # start_urls.append(url)
    start_urls=['https://nj.fang.lianjia.com/']
    all_a=[]
    all_table=[]

    def parse(self,response):
        dd=response.css('dd')[7].css('a::attr(href)')
        for i in dd:
            href=i.extract()
            href=href+'loupan/pg1'
            yield scrapy.Request(url=href,callback=self.parse1)


    def parse1(self, response):
        useless=response.css('div[class=resblock-have-find]').css('span::text')[2].extract()
        table_name=re.findall(re.compile('个.+'),useless)[0].replace('个','').replace('新房','')
        db=pymysql.connect(host='localhost',user='root',password='zhao/980931',port=3306,db='spiders')
        cursor=db.cursor()
        tables1=cursor.execute('show tables;')
        tables2 = cursor.fetchall()
        for i in range(len(tables2)):
            one=str(tables2[i]).replace(',','').replace('(','').replace(')','').replace("'",'')
            self.all_table.append(one)
        if not (table_name in self.all_table):
            sql = """CREATE TABLE {} (
            `price` varchar(20) DEFAULT NULL,
            `name` varchar(20) DEFAULT NULL,
            `address` varchar(150) DEFAULT NULL,
            `url` varchar(100) DEFAULT NULL
            )""".format(table_name)
            cursor.execute(sql)
            num=response.css('span.value::text').extract()[0]
            page_num=math.ceil(int(num)/int(10))+1
            for num in range(1,page_num):
                current_page_num='pg'+str(num)
                url=response.url
                pg_num=re.findall(re.compile('pg\d+'),url)[0]
                url=url.replace(str(pg_num),current_page_num)
                yield scrapy.Request(url=url,callback=self.parse2)
        

    def parse2(self,response):
        useless=response.css('div[class=resblock-have-find]').css('span::text')[2].extract()
        table_name=re.findall(re.compile('个.+'),useless)[0].replace('个','').replace('新房','')
        all_div=response.css('div[class=resblock-desc-wrapper]')
        for div in all_div:
            all_li=div.css('div[class=resblock-name]')
            price=div.css('span[class=number]::text').extract()[0]
            price=" '{}' ".format(price)
            address=div.css('div[class=resblock-location]').css('a::text').extract()[0]
            address="'{}' ".format(address)
            for i in all_li:
                item=HomeItem()
                url=response.url
                unless=re.findall(re.compile('/loupan/pg\d'),url)[0]
                url=url.replace(unless,'')
                url2=url+i.css('a::attr(href)').extract()[0]
                url2="'{}' ".format(url2)
                name=i.css('a::text').extract()[0]
                name="'{}' ".format(name)
                sql="insert into {} (price,name,address,url) values ({},{},{},{})".format(table_name,price,name,address,url2)
                item['all_sql']=sql
                yield item


            

