import scrapy
from redemospider.items import RedemospiderItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
       print(response.text)
       text = response.text
       item = RedemospiderItem()
       item['text'] = text
       yield item

