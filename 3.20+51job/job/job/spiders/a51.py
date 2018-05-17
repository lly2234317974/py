# -*- coding: utf-8 -*-
import scrapy


class A51Spider(scrapy.Spider):
    name = '51'
    allowed_domains = ['51.com']
    start_urls = ['http://51.com/']

    def parse(self, response):
        divs=response.xpath('//div[@id="resultList"]/div[contains(@class,"el")]')

        for
