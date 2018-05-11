# -*- coding: utf-8 -*-
import scrapy

from ..items import ZsItem
class ZsSpider(scrapy.Spider):
    name = 'zs'
    allowed_domains = ['zs.com']
    start_urls = ['http://sc.chinaz.com/jianli/free.html']
    #获取开发个人简历url
    def parse(self, response):
        kf_href=response.xpath('//div[@class="hot1"]/ul[5]/li[2]/a/@href').extract_first(' ')
        kf_url='http://sc.chinaz.com'+kf_href
        yield scrapy.Request(kf_url, self.parse_detail, dont_filter=True)
    #获个人开发取详细页和下一页
    def parse_detail(self,response):
        #详细url
        detail_url_list=response.xpath('//div[@class="box picblock col3"]/div/a')
        for detail_url in detail_url_list:
            detail_url=detail_url.xpath('@href').extract_first('')


            print(detail_url)
            yield scrapy.Request(detail_url, self.detail_page, dont_filter=True)
        next_page=response.xpath('//a[contains(text(),"下一页")]/@href').extract_first('')
        next_page='http://sc.chinaz.com/tag_jianli/'+next_page
        yield scrapy.Request(next_page, self.parse_detail, dont_filter=True)


    def detail_page(self,response):
        # down_url=response.xpath('//a[contains(text(),"福建电信下载")]/href').extract_first()
        down_url=response.xpath('//div[@class="dian"][2]/a[1]/@href').extract_first(' ')
        name=response.xpath('//div[@class="text_wrap"]/h2/a/text()').extract_first(' ')
        img_src=response.xpath('//div[@id="shareList"]/span[1]/img/@src').extract_first(' ')
        print('---------',down_url)
        if down_url !=' ':
            item=ZsItem()
            item['down_url']=[down_url]
            item['name']=name
            item['img_src']=[img_src]
            yield item






