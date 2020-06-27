# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import csv

with open('./maoyan.html', 'r') as f:
    html = f.read()
    f.close()

# url = "https://maoyan.com/films?showType=3"

# print(html.encoding)
# header = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

# responese = requests.get(url=url, headers=header)

data = bs(html, 'html.parser')
# print(data)


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