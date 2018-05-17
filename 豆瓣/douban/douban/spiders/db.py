# -*- coding: utf-8 -*-
import scrapy,re
from..items import DoubanItem
class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['db.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        '''
        1.排名
        2.电影名
        3.国家
        4.类型
        :param response:
        :return:
        '''
        content=response.xpath('//div[@class="item"]')
        for con in content:
            rank=con.xpath('div[1]/em/text()').extract_first('')
            name=con.xpath('div[1]/a/img/@alt').extract_first('')
            src=con.xpath('div[1]/a/img/@src').extract_first('')
            print(rank)
            print(name)
            print(src)
            director=con.xpath('div[2]/div[2]/p[1]/text()').extract_first('')#演员阵容
            director=re.sub('<br/>| |\n|\xa0','',director)
            score=con.xpath('div[2]/div[2]/div/span[2]/text()').extract_first('')#评分
            score_num=con.xpath('div[2]/div[2]/div/span[4]/text()').extract_first('').split('人评价')[0]#评价人数
            quote=con.xpath('div[2]/div[2]/p[2]/span/text()').extract_first('')#豆瓣评价
            print(director)
            print(score)
            print(score_num)
            print(quote)
            item=DoubanItem()
            item['rank']=rank
            item['name']=name
            item['director']=director
            item['score']=score
            item['score_num']=score_num
            item['quote']=quote
            item['src']=src
            yield item

        next_url_con=response.xpath('//a[contains(text(),"后页")]')
        if next_url_con:
            next_url=response.xpath('//a[contains(text(),"后页")]/@href').extract_first()
            next_url='https://movie.douban.com/top250'+next_url
            yield scrapy.Request(next_url,dont_filter=True)


