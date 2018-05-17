# -*- coding: utf-8 -*-
import scrapy

from..items import AxblogspiderItem
class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.com']
    start_urls = ['http://blog.csdn.net/column.html']

    def parse(self, response):
        next_url = response.xpath('//div[@class="column_wrap clearfix"]/div')
        for url in next_url:
            src = url.xpath('div/@style').extract_first('').split('(')[-1].strip(')')
            next_url = 'http://blog.csdn.net' + url.xpath('a/@href').extract_first('')
            first_name = url.xpath('a/div/p/text()').extract_first('')
            yield scrapy.Request(url=next_url, callback=self.detail_info, dont_filter=True,meta={'first_name': first_name, 'src': src})
        next_page = response.xpath('//a[contains(text(),"下一页")]/text()').extract_first('')
        next_page_url = response.xpath('//a[contains(text(),"下一页")]/@href').extract_first('')
        next_page_url = 'http://blog.csdn.net' + next_page_url
        if next_page == '下一页':
            yield scrapy.Request(next_page_url,self.parse,dont_filter=True)

    # 解析数据
    def detail_info(self, response):
        detail_list=response.xpath('//ul[@class="detail_list"]/li')
        for detail in detail_list:
            title = detail.xpath('h4/a/text()').extract_first('')
            date = detail.xpath('div/span/text()').extract_first('')
            click_num = detail.xpath('div/em/text()').extract_first('')
            first_name = response.meta.get('first_name')
            src = response.meta.get('src')
            print(title,date,click_num,first_name,src)
            item=AxblogspiderItem()
            item['title']=title
            item['date']=date
            item['click_num']=click_num
            item['first_name']=first_name
            item['src']=[src]
            yield item


        detail_next_page = response.xpath('//a[contains(text(),"下一页")]/text()').extract_first('')
        detail_next_url=response.xpath('//a[contains(text(),"下一页")]/@href').extract_first('')
        detail_next_url = 'http://blog.csdn.net' + detail_next_url
        if detail_next_page=='下一页':
            yield scrapy.Request(url=detail_next_url,callback=self.detail_info,dont_filter=True)
