# -*- coding: utf-8 -*-
import scrapy
from ..items import KebiItem

class KbSpider(scrapy.Spider):
    name = 'kb'
    allowed_domains = ['http://jinrong.kebi.biz']
    # 贵金属------
    # 期货 'http://jinrong.kebi.biz/sell/list/23611.html'
    #
    start_urls = ['http://jinrong.kebi.biz/sell/list/23611_page_491.html']


    def parse(self, response):
        all_url=response.xpath('//table[@class="tablelist any"]/tr/td[1]/a/@href').extract()
        for carrie in all_url:
            yield scrapy.Request(carrie,self.detail,dont_filter=True)
        next_page = response.xpath("//a[contains(text(),'下一页')]/@href").extract_first()
        next_url = 'http://jinrong.kebi.biz/sell/list/' + next_page
        print(next_url)
        yield scrapy.Request(next_url, self.parse, dont_filter=True)

    def detail(self,response):
        total=response.xpath('//table[@class="f14"]')
        for item in total:
            company=item.xpath('tr[1]/td/a/text()').extract_first('')
            name=item.xpath("tr[2]/td[2]/text()").extract_first('')
            phone=item.xpath('tr[3]/td[2]/text()').extract_first('')
            number=item.xpath('tr[4]/td[2]/text()').extract_first('')
            address=item.xpath('tr[5]/td[2]/text()').extract_first('')
            item=KebiItem()
            item['company']=company
            item['name']=name
            item['phone']=phone
            item['number']=number
            item['address']=address
            yield item



