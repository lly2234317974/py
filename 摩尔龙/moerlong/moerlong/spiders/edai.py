# -*- coding: utf-8 -*-
import scrapy

from..items import MoerlongItem
class EdaiSpider(scrapy.Spider):
    name = 'edai'
    allowed_domains = ['edai.com']
    start_urls = ['http://sh.edai.com/chanpin/?page=1']
    def start_requests(self):
        for x in range(2, 1448):
            url = 'http://sh.edai.com/chanpin/?page={}'.format(x)
            yield scrapy.Request(url)
    def parse(self, response):
        content=response.xpath('//ul/li/div[2]/h3')
        for carrie in content:
            url=carrie.xpath('a/@href').extract_first('')
            yield scrapy.Request(url,self.detail_information,dont_filter=False)
        # next_page=response.xpath('//a[contains(text(),"下一页")]/text()').extract_first('')
        # if '下一页' in next_page:
    def detail_information(self,response):
        company=response.xpath('//p[7]/text()').extract_first('')
        if '所属公司： ' in company:
            company=company.split('所属公司： ')[1]
            item=MoerlongItem()
            item['company']=company
            yield item

