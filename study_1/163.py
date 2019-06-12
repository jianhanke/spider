
import requests

from bs4 import BeautifulSoup

import csv





# 构造函数获取歌手信息

def get_artists(url):

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html5lib')
    

    for artist in soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'}):

        artist_name = artist.string

        artist_id = artist['href'].replace('/artist?id=', '').strip()

        try:

            writer.writerow((artist_id, artist_name))

        except Exception as msg:

            print(msg)





ls1 = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]    # id的值

ls2 = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]    # initial的值
try:
  csvfile = open('music_163_artists(3).csv', 'a', encoding='gbk')    # 文件存储的位置
except:
  pass

writer = csv.writer(csvfile)
writer.writerow(('artist_id', 'artist_name'))

for i in ls1:

    for j in ls2:

        url = 'http://music.163.com/discover/artist/cat?id=' + str(i) + '&initial=' + str(j)
        print(url)
        get_artists(url)