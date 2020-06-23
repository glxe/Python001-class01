import requests
import lxml.etree

url = "https://movie.douban.com/subject/1292052/"

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"

# 声明为字典使用字典的语法赋值
header = {}
header['user-agent'] = userAgent
response = requests.get(url, headers = header)

# print(response.text)
# xml化处理
selector = lxml.etree.HTML(response.text)

#电影名称
movieName = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称：{movieName}')
#上映日期
date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{date}')
#评分
score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分：{score[0]}')

details = [movieName[0], date[0], score[0]]

# print(details)
import pandas as pd

movieOne = pd.DataFrame(data = details)

movieOne.to_csv('./movieOne.csv', encoding = 'utf8', index = False, header = False)