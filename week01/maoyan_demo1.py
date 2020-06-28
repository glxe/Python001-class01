# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import csv

# with open('./maoyan.html', 'r') as f:
#     html = f.read()
#     f.close()

url = "https://maoyan.com/films?showType=3"

USER_AGENT = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

header = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"}

responese = requests.get(url=url, headers=header)

data = bs(responese.text, 'html.parser')
print(data)


# # data.find_all(class="class")
movies = []
movieName = data.find_all('div', attrs={'class': 'movie-item-title'})
movieType = data.select('.movie-hover-info > div:nth-child(2)')
movieTime = data.select('.movie-hover-info > div:nth-child(4)')
# print(movieTime)
itemsName = []
itemsType = []
itemsTime = []
i = 0
for name in movieName:
    if (i > 9):
        break
    # item['title'] = (name.get('title')
    item = {'title': name.get('title')}
    itemsName.append(item)
    i+=1

j = 0
for t in movieType:
    if (j > 9):
        break
    # item['title'] = (name.get('title')
    item = {'type': t.get_text().strip().replace("\n", "").replace(' ', '')}
    itemsType.append(item)
    j+=1

k = 0
for t in movieTime:
    if (k > 9):
        break
    # item['title'] = (name.get('title')
    item = t.get_text().strip().replace("\n", "").replace(' ', '')
    title = itemsName[k]['title']
    typetype = itemsType[k]['type']
    mItem = {'title': title, 'type': typetype, 'time': item}
    movies.append(mItem);
    k+=1

import pandas as pd
handle = pd.DataFrame(data = movies)
handle.to_csv('./week01/maoyan_demo1.csv', encoding='utf-8', index = False, header = False)









print(movies)