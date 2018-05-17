# -*- coding: utf-8 -*-
import scrapy
from..items import QishuItem

class QiSpider(scrapy.Spider):
    name = 'qi'
    allowed_domains = ['qishu.com']
    start_urls = ['https://www.qisuu.com/']
    base_url='https://www.qisuu.com'

    def parse(self, response):
        res=response.xpath('//div[@class="nav"]/a')

        for index,a in enumerate(res):
            if index==0:
                continue
            cate=a.xpath('text()').extract_first('')
            href=a.xpath('@href').extract_first('')
            print(cate,href)
            #
            cg_url=self.base_url+href
            #创建请求对象，并使用yield交给引擎处理

            yield scrapy.Request(
                url=cg_url,
                callback=self.parse_categray,
                meta={'cate':cate},
                dont_filter=True

            )
    #解析分类页面
    def parse_categray(self,response):
        # cate=response.meta.get('cate')
        # print(cate)

        lis=response.xpath('//div[@class="listBox"]/ul/li')
        for i in lis:
            star=i.xpath('div/em/@class').extract_first()
            href=i.xpath('a/@href').extract_first()
            detail_url=self.base_url+href
            response.meta['star']= star
            response.meta['detail_url']=detail_url

            yield scrapy.Request(
                url=detail_url,
                callback=self.parse_detail,
                meta=response.meta,
            dont_filter=True)

        next_href=response.xpath('//a[contains(text(),"下一页")]/href').extract_first('')
        if next_href:
            yield scrapy.Request(
            url=self.base_url+next_href,
            callback=self.parse_categray,
            meta=response.meta,
            )


    def parse_detail(self,response):
        #分类，等级，地址

        cate=response.meta.get('cate')
        star=response.meta.get('star')
        star=star[-1]
        detail_url=response.meta.get('detail_url')
        src=response.xpath('//div[@class="detail_pic"]/img/@src').extract_first('')
        src=self.base_url+src

        #小说名字
        name=response.xpath('//div[@class="detail_right"]/hl/text()').extract_first('')

        infos=response.xpath('//div[@class="detail_right"]/ul/li/text()').extract()
        #点击数
        click_num=infos[0].split('：')[-1]
        file_size=infos[1].split('：')[-1]
        book_type=infos[2].split('：')[-1]
        update_time=infos[3].split('：')[-1]
        status=infos[4].split('：')[-1]
        author=infos[5].split('：')[-1]
        run_type=infos[6].split('：')[-1]
        print(star,cate,author,file_size)

        item=QishuItem()
        item['cate']=cate
        item['star']=star
        item['detail_url']=[detail_url]
        item['src']=[src]
        item['name']=name
        item['click_num']=click_num
        item['file_size']=file_size
        item['book_type']=book_type
        item['update_time']=update_time
        item['status']=status
        item['author']=author
        item['run_type']=run_type

        yield item







































