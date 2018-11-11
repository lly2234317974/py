# -*- coding: utf-8 -*-
import scrapy

from ..items import XinxiItem
class CnlinfoSpider(scrapy.Spider):
    name = 'cnlinfo'
    allowed_domains = ['cnlinfo.net']
    start_urls = ['http://so.cnlinfo.net/sonew/SearchCompanyNew.aspx?kw=%E5%95%86%E5%8A%A1%E5%92%A8%E8%AF%A2']

    def parse(self, response):
        next_page=response.xpath('//ul/li[@class="list_1_c"]')
        for y in next_page:
            next_page_url=y.xpath('p[1]/a/@href').extract_first()
            hangye = y.xpath('p[2]//text()').extract()
            hangye = ''.join(hangye)
            address = y.xpath('p[3]//text()').extract_first('')
            yield scrapy.Request(url=next_page_url,callback=self.informa,meta={'hangye':hangye,'address':address})
        for x in range(2,1461):
            next_url='http://so.cnlinfo.net/sonew/SearchCompanyNew.aspx?kw=%E5%95%86%E5%8A%A1%E5%92%A8%E8%AF%A2&pagenum={}'.format(x)
            yield scrapy.Request(next_url, self.parse,dont_filter=False)
    def informa(self,response):
        hangye=response.meta['hangye']
        address=response.meta['address']
        print(hangye)
        phone=response.xpath('//div[@class="dialog"]/div[2]/text()').extract_first()
        print(phone)
        item=XinxiItem()
        item['phone']=phone
        item['hangye']=hangye
        item['address']=address
        yield item
