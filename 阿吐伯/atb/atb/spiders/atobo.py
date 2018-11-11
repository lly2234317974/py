# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import AtbItem
class AtoboSpider(scrapy.Spider):
    name = 'atobo'
    allowed_domains = ['atobo.com']
    start_urls = ['https://www.atobo.com.cn/Companys/s-k582104/']
    def parse(self,response):
        all_city=response.xpath('//div[@id="ca_note"]/div/a/@href').extract()
        for zz in all_city:
            num=re.findall('\d+',zz)
            num=num[0]
            url='https://www.atobo.com.cn/Companys/s-s{}-k54794/'.format(num)
            yield scrapy.Request(url,self.city_page,dont_filter=True)
    def city_page(self, response):
        num_detail=response.xpath(".//*[@id='setcolor_area']/div[1]/div[1]/ul/li[3]/strong[1]/text()").extract_first('')
        if num_detail !='0':
            all_url=response.xpath('//a[@class="CompanyName"]/@href').extract()
            for carrie in all_url:
                a=carrie.split('//')[1]
                heder={
                    'Host': a,
                    'User - Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
                    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    'Accept - Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                    'Accept - Encoding': "gzip, deflate",
                    'Connection': "keep-alive",
                }
                yield scrapy.Request(carrie,self.detail,headers=heder,dont_filter=True)
            next_page=response.xpath('//a[contains(text(),"下一页")]/@href').extract_first('')
            next_page_url='https://www.atobo.com.cn'+next_page
            print(next_page_url)
            yield scrapy.Request(next_page_url,self.parse,dont_filter=True)
        else:
            pass
    def detail(self,response):
        company=response.xpath('//div[@class="cont-r"]/div[1]/h2/em/text()').extract_first('')
        all_content=response.xpath('//div[@class="card-context"]')
        for henry in all_content:
            main_business=henry.xpath('ul[1]/li[2]/text()').extract_first('')
            address=henry.xpath('ul[2]/li[2]/text()').extract_first('')
            name=henry.xpath('ul[3]/li[2]/text()').extract_first('')
            phone=henry.xpath('ul[4]/li[2]/text()').extract_first('')
            number=henry.xpath('ul[5]/li[2]/text()').extract_first('')
            item=AtbItem()
            item['company']=company
            item['main_business']=main_business
            item['address']=address
            item['name']=name
            item['phone']=phone
            item['number']=number
            yield item

