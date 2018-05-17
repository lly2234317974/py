# -*- coding: utf-8 -*-
import scrapy


class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jiandan.com']
    start_urls = ['http://jiandan.com/']

    def parse(self, response):
        pass
