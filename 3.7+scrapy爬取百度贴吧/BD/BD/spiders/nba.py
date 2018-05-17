# -*- coding: utf-8 -*-
from urllib import request

import scrapy,re
from..items import BdItem

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['nba.cm']
    start_urls = ['https://tieba.baidu.com/f?kw=%E7%81%AB%E7%AE%AD&ie=utf-8&tab=good&cid=0&pn=']

    def parse(self,response):
        yield scrapy.Request(
            url=response.url,
            callback=self.detail_data,
            dont_filter=True,
            meta={},

        )
    # 首页信息
    def detail_data(self, response):
        detail_list=response.xpath('//div [@class="t_con cleafix"]')
        for detail in detail_list:
            content=detail.xpath('div/div/div/a/text()').extract_first(' ')# 标题
            next_url=detail.xpath('div/div/div/a/@href').extract_first(' ')# 详细url
            next_url='https://tieba.baidu.com'+next_url

            print(content)

            yield scrapy.Request(url=next_url,callback=self.next_detail_data,meta={'content':content},dont_filter=True,)
        # 获取本页的下一页
        detail_data_content = response.xpath('//div[@class="pagination-default clearfix"]/a/text()').extract()
        detail_data_content = str(detail_data_content[-2])
        detail_page = response.xpath('//div[@class="pagination-default clearfix"]/a/@href').extract()
        detail_page=detail_page[-2]
        detail_page= 'https:' + detail_page
        print(detail_page)
        if '下一页' in detail_data_content:
            yield scrapy.Request(url=detail_page,callback=self.detail_data,dont_filter=True)

    # 详细页信息
    def next_detail_data(self, response):
        title = response.meta.get('content')#标题
        author=response.xpath('//li[@class="d_name"]/a/text()').extract_first('作者')
        level=response.xpath('//div[@class="p_badge"]/a/div/text()').extract_first('')#等级
        content=response.xpath('//cc/div[@class="d_post_content j_d_post_content "]//text()').extract_first().strip('   ')#回复内容
        client = response.xpath('//div[@class="post-tail-wrap"]/span[@class="tail-info"]/a/text()').extract_first('来自web客户端')
        date=response.xpath('//div[@class="post-tail-wrap"]/span[@class="tail-info"]//text()').extract()#发布日期
        date=date[-1]

        print(title,author,level,content,client,date)

        item=BdItem()
        item['title']=title
        item['author']=author
        item['level']=level
        item['content']=content
        item['client']=client
        item['date']=date
        yield item
        #获取下一页信息
        detail_content=response.xpath('//ul[@class="l_posts_num"]/li/a/text()').extract()
        if detail_content:
            detail_content=str(detail_content[-2])
            print(detail_content)
        detail_url=response.xpath('//ul[@class="l_posts_num"]/li/a/@href').extract()

        detail_url='https://tieba.baidu.com'+detail_url[-2]
        if '下一页' in detail_content:

            yield scrapy.Request(url=detail_url,callback=self.next_detail_data,dont_filter=True)













