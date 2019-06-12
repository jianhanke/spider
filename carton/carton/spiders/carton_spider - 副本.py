import scrapy 
import re
import os
import requests
from carton.items import CartonItem

class CartonSpider(scrapy.Spider):
    name='carton'
    #start_urls=['http://comic.kukudm.com/comiclist/3/']
    start_urls=['http://comic.kukudm.com/comiclist/3']
    hide_url='http://n9.1whour.com/'
    now_url='http://comic.kukudm.com'
    all_url=[]
    all_name=[]
    page=1
    def parse(self,response):
        
        all_chapter=response.css('dd')
        for chapter in all_chapter:
            url=chapter.css('A::attr(href)').extract()[0]
            url=self.now_url+url
            self.all_url.append(url)
            name=chapter.css('A::text').extract()[0]
            self.all_name.append(name)
        for i in range(2,3):
            url=self.all_url[i]
            meta={'current_page':i}
            yield scrapy.Request(url=url,meta=meta,callback=self.parse2)

    def parse2(self,response):
        meta={'current_page':response.meta['current_page']}
        page_num =response.xpath('//td[@valign="top"]/text()').re(u'共(\d+)页')[0]
        page_num=int(page_num)+1
        url=response.url
        for i in range(1,page_num):
            ago_page=re.findall('\d+\.htm',url)[0]
            url=url.replace(ago_page,'{}.htm'.format(i))
            yield scrapy.Request(url=url,meta=meta,callback=self.parse3)


    def parse3(self,response):
        current_page=response.meta['current_page']
        current_chapter_name=self.all_name[current_page]
        root='G:\carton\火影忍者\ '+current_chapter_name+'\ '
        if not os.path.exists(root):
            os.mkdir(root)
        file_name=root+str(self.page)+'.jpg'
        src=response.css('script')[3]
        url=src.css('script::text').extract()[0]
        all2=re.findall(re.compile(r'\+"(.+)\'></a'),url)[0]
        all2=self.hide_url+all2
        #print(url)
        html=requests.get(all2,timeout=30).content
        with open(file_name,'wb') as f:
            f.write(html)
        self.page+=1






    #def parse(self,response):
        # all_script=response.css('script').extract()[3]

        # first_href=re.findall(r'SRC.+/.+/.+/.+/.+jpg\'></a>|SRC.+/.+/.+/.+/.+JPG\'></a>',all_script )[0]
        # second_href=re.findall(r'src.+/.+/.+/.+/.+jpg|src.+/.+/.+/.+/.+JPG',all_script )[0]

        # first_href=first_href.replace('SRC=\'"+m201304d+"','')
        # first_href=first_href.replace('\'></a>','')

        # second_href=second_href.replace('src=\'"+m201304d+"','')

        # print(self.hide_name+first_href)
        # print(self.hide_name+second_href)
        # for i in all_url:
        #     print(i)
       
        # for i in all_url:
        #     if not 'http' in i:
        #         print('http://comic.kukudm.com'+i)
        #     else:
        #         print(i)
        