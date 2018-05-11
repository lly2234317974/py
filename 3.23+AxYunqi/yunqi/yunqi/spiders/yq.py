# -*- coding: utf-8 -*-
import scrapy

from..items import YunfirstItem
from..items import DetailItem

class YqSpider(scrapy.Spider):
    name = 'yq'
    allowed_domains = ['yq.com']
    start_urls = ['http://yunqi.qq.com/bk/gdyq/so2/n30p1']

    def parse(self, response):
        list=response.xpath('//div[@class="book"]')
        for tr in list:
            img_src=tr.xpath('a/img/@src').extract_first('')
            title=tr.xpath('div/h3/a/text()').extract_first('')
            author=tr.xpath('div/dl[1]/dd[1]/a/text()').extract_first('')
            xs_type=tr.xpath('div/dl[1]/dd[2]/a/text()').extract_first('')
            xs_state=tr.xpath('div/dl[1]/dd[3]/text()').extract_first('')
            refresh_time=tr.xpath('div/dl[2]/dd[1]/text()').extract_first('')
            xs_num=tr.xpath('div/dl[2]/dd[2]/text()').extract_first('')
            xs_url=tr.xpath('a/@href').extract_first('')
            xs_id=tr.xpath('div/h3/a/@id').extract_first('')
            item=YunfirstItem()
            item['img_src']=img_src
            item['title']=title
            item['author']=author
            item['xs_type']=xs_type
            item['xs_state']=xs_state
            item['refresh_time']=refresh_time
            item['xs_num']=xs_num
            item['xs_url']=xs_url
            item['xs_id']=xs_id
            yield item

            yield scrapy.Request(url=xs_url,callback=self.detail_info,dont_filter=True,meta={'xs_id':xs_id})
        for x in range(1,100):
            next_page='http://yunqi.qq.com/bk/gdyq/so2/n30p%s'%x
            print(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse,dont_filter=True)


    def detail_info(self,response):
        xs_id=response.meta['xs_id']
        tag=response.xpath('//div[@class="left"]/div[6]/text()').extract_first('').split('：')[-1]
        tag=tag.strip('\r\n')
        list_ar=response.xpath('//div[@class="swishlist"]/table')
        for ar in list_ar:
            click_num=ar.xpath('tr[2]/td[1]/text()').extract_first('').split('：')[-1]
            total_rq=ar.xpath('tr[2]/td[2]/text()').extract_first('').split('：')[-1]
            total_tj=ar.xpath('tr[2]/td[3]/text()').extract_first('').split('：')[-1]
            month_click=ar.xpath('tr[3]/td[1]/text()').extract_first('').split('：')[-1]
            month_rq=ar.xpath('tr[3]/td[2]/text()').extract_first('').split('：')[-1]
            month_tj=ar.xpath('tr[3]/td[3]/text()').extract_first('').split('：')[-1]
            week_click=ar.xpath('tr[4]/td[1]/text()').extract_first('').split('：')[-1]
            week_rq=ar.xpath('tr[4]/td[2]/text()').extract_first('').split('：')[-1]
            week_tj=ar.xpath('tr[4]/td[3]/text()').extract_first('').split('：')[-1]
            total_pl=ar.xpath('tr[5]/td[2]/span/text()').extract_first('')
            print(click_num)
            # item=DetailItem()
            # item['xs_id'] = xs_id
            # item['click_num']=click_num
            # item['total_rq']=total_rq
            # item['total_tj']=total_tj
            # item['month_click']=month_click
            # item['month_rq']=month_rq
            # item['month_tj']=month_tj
            # item['week_click']=week_click
            # item['week_rq']=week_rq
            # item['week_tj']=week_tj
            # item['tag']=tag
            # item['total_pl']=total_pl
            #
            # yield item
