# -*- coding: utf-8 -*-
import scrapy,os
from..items import QsbkSpiderItem
from urllib import request

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qsbk.com']
    start_urls = ['https://www.qiushibaike.com/pic/']

    def parse(self, response):
        '''
        :param response:
        :return:
        '''
        yield scrapy.Request(
            url=response.url,
            meta={},
            dont_filter=True,
            callback=self.detail_TP,
        )
    def next_page(self,response):
        '''
        下一页
        :param response:
        :return:
        '''
        next_url=response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract_first()
        next_url='https://www.qiushibaike.com'+str(next_url)
        # print(next_url)

        yield scrapy.Request(
            url=next_url,
            callback=self.detail_TP,
            meta={},
            dont_filter=True,
        )
    def detail_TP(self,response):
        '''
        获取图片，名字，
        :param response:
        :return:
        '''
        detail_list=response.xpath('//div[@class="article block untagged mb15"]')
        # print(detail_list)
        for detail in detail_list:
            img_src=detail.xpath('div[@class="thumb"]/a/img/@src').extract_first('没有图片地址')
            alt=detail.xpath('div[@class="thumb"]/a/img/@alt').extract_first('没有图片名字')
            author=detail.xpath('div[@class="author clearfix"]/a/h2/text()').extract_first('没有作者')

            img_src='http:'+img_src
            img_src=img_src

            print(img_src)
            path='TP/'+'1'
            if not os.path.exists(path):
                os.makedirs(path)
            item=QsbkSpiderItem()
            item['img_src']=img_src
            item['alt']=alt
            item['author']=author
            item['path']=path
            yield item
            # request.urlretrieve(img_src, path+alt)
            with open(path+'/'+img_src.split('/')[-1],"wb")as f:
                img_response=requests.get(img_src)
                f.write(img_response.content)


        yield scrapy.Request(
                url=response.url,
                callback=self.next_page,
                meta={},
                dont_filter=True,
        )

