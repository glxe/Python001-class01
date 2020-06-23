import requests
from bs4 import BeautifulSoup as b4
from lxml import etree
import pandas as pd


def getCurrentPageByUrl(url):
    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    response = requests.get(url, headers = header)
    htmlStr = response.text
    htmlObj = etree.HTML(htmlStr)
    # //*[@id="content"]/div/div[1]/ol/li[1]/div/div
    movieNames = htmlObj.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div/a/span[1]/text()')
    movieDetailUrls = htmlObj.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href')
    
    print(movieNames)
    print(movieDetailUrls)
    details = [movieNames, movieDetailUrls]
    data = pd.DataFrame(data = details)
    data.to_csv('./movieOne.csv', encoding = 'utf8', index = False, header = False, mode='a') # 追加写入文件


from time import sleep

url = "https://movie.douban.com/top250"

#生成所有页面的urls元祖
urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))
print(urls)
# getCurrentPageByUrl(url)

for url in urls:
    getCurrentPageByUrl(url)
    sleep(5)