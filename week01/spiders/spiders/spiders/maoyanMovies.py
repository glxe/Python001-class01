import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem

class MaoyanmoviesSpider(scrapy.Spider):
    name = 'maoyanMovies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):

        movies = Selector(response).xpath('//div[@class="movie-item-hover"]')
        i = 0
        for movie in movies:
            if (i > 9):
                break
            item = SpidersItem()
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