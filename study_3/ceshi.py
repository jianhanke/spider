import re


url='https://tj.fang.lianjia.com/loupan/pg1'

for num in range(1,10):
    current_page_num='pg'+str(num)
    print(current_page_num)
    pg_num=re.findall(re.compile('pg\d+'),url)[0]
    print(pg_num)
    url=url.replace(str(pg_num),current_page_num)
    print(url)

url2='https://ty.fang.lianjia.com/loupan/pg1'

ceshi=re.findall(re.compile('/loupan/pg\d'),url2)[0]
print(ceshi)


