# -*- coding: utf-8 -*-
import scrapy


class XlSpider(scrapy.Spider):
    name = 'xl'
    allowed_domains = ['xl.com']
    start_urls = ['http://blog.sina.com.cn/lm/pic/']

    def parse(self, response):
        pass
