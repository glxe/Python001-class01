# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from proxyspider.items import ProxyspiderItem
#export http_proxy = "http://52.179.231.206:80"
# setting 增加scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过 Request.meta['proxy'] 读取 http_proxy 环境变量加载代理

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['maoyan.com']

    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        movies = Selector(response).xpath('//div[@class="movie-item-hover"]')
        i = 0
        for movie in movies:
            if (i > 9):
                break
            item = ProxyspiderItem()
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