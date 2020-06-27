import scrapy
from bs4 import BeautifulSoup
from spiders.items import SpidersItem

class DoubanMoviesSpider(scrapy.Spider):
    name = 'douban_movies'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(0, 10):
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url = url, callback=self.parse)

    # 解析函数
    def parse(self, response):
        items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'hd'})
        for title in title_list:
            item = SpidersItem()
            item['title'] = title.find('a').find('span',).text
            item['link'] = title.find('a').get('href')
            items.append(item)
            yield scrapy.Request(url=item['link'], meta = {'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item
