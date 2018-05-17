# -*- coding: utf-8 -*-
import scrapy


class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jiandan.com']
    start_urls = ['http://jandan.net/ooxx']

    def parse(self, response):


        yield scrapy.Request(
            url=response.url,
            meta={},
            dont_filter=True,
            callback=self.detail_tp,
        )
    def detail_tp(self,response):

        tp=response.xpath('//div[@class="text"]/p/img/@src')
        print(tp)