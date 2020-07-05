import scrapy
from ..items import MaoyanspiderItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']

    def start_requests(self):
        i = 0
        for i in range(0, 3):
            url =  f"http://maoyan.glxe.com/?showType=3&offset={i*30}"
            yield scrapy.Request(url = url, callback=self.parse)


    def parse(self, response):
        movies = response.xpath('//div[@class="movie-item-hover"]')
        i = 0
        for movie in movies:
            item = MaoyanspiderItem()
            title = movie.xpath('./a/div/div[1]/span[1]/text()').extract()[0].strip()
            t = movie.xpath('./a/div/div[2]//text()').extract()[2].strip()
            timet = movie.xpath('./a/div/div[4]//text()').extract()[2].strip()
            item = {
                'title': title,
                'type': t,
                'time': timet
            }
            i += 1
            yield item
