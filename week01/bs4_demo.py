import requests
from bs4 import BeautifulSoup as b4


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
header = {'user-agent': user_agent}
myurl = 'https://movie.douban.com/top250'
respone = requests.get(myurl, headers=header,
                       auth=('15370383786', 'xxxx'))


bs_info = b4(respone.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a', ):
        print(atag.get('href')) #获取所有连接
        print(atag.find('span',).text) #获取电影名称
