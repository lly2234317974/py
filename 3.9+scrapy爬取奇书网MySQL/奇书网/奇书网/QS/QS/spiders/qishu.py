# -*- coding: utf-8 -*-
import scrapy
from ..items import QSItem

class QishuSpider(scrapy.Spider):
    name = 'qishu'
    allowed_domains = ['qishu.com']
    start_urls = ['https://www.qisuu.com/']

    def parse(self, response):
        # 获取第二页url
        next_url = response.xpath('//div[@class="nav"]/a[2]/@href').extract_first('')
        next_url = 'https://www.qisuu.com' + next_url
        yield scrapy.Request(
            url=next_url,
            callback=self.detail_next,
            dont_filter=True
        )
    # 获取详细页第二页
    def detail_next(self,response):
        #获取详细页面url
        detail_url=response.xpath('//div[@class="listBox"]/ul/li/a')
        for info in detail_url:
            next_url='https://www.qisuu.com'+info.xpath('@href').extract_first('')
            yield scrapy.Request(
                url=next_url,
                callback=self.detail_information,
                dont_filter=True

            )
        next_page=response.xpath('//div[@class="tspage"]/a/@href').extract()
        next_page=next_page[-2]
        print(next_page)
        # all_page_url=response.xpath('//select[@name="select"]/option/@value').extract()
        # for next_page in all_page_url:
        #     print(next_page)
        next_page='https://www.qisuu.com'+next_page
        yield scrapy.Request(
                url=next_page,
                callback=self.detail_next,
                dont_filter=True,
            )

    # 第三页
    def detail_information(self,response):

        title=response.xpath('//div[@class="showBox"]/div/div/div/h1/text()').extract_first('')#书名
        client_count=response.xpath('//div[@class="showBox"]/div/div/div/ul/li[1]/text()').extract_first('').split(u'：')[-1]#点击次数
        file=response.xpath('//div[@class="showBox"]/div/div/div/ul/li[2]/text()').extract_first('').split(u'：')[-1]#文件大小
        type=response.xpath('//div[@class="showBox"]/div/div/div/ul/li[3]/text()').extract_first('').split(u'：')[-1]#书籍类型
        date=response.xpath('//div[@class="showBox"]/div/div/div/ul/li[4]/text()').extract_first('').split(u'：')[-1]#更新日期
        author=response.xpath('//div[@class="showBox"]/div/div/div/ul/li[6]/text()').extract_first('').split(u'：')[-1]#作者
        run_environment=response.xpath('//div[@class="showBox"]/div/div/div/ul/li[7]/text()').extract_first('').split(u'：')[-1]#运行环境
        online_reading=response.xpath('//div[@class="showBox mt20"]/div/ul/li[1]/a/@href').extract_first('')#在线阅读地址
        online_reading='https://www.qisuu.com'+online_reading
        print(title,client_count,file,type,date,author,run_environment,online_reading)
        item=QSItem()
        item['title']=title
        item['client_count']=client_count
        item['file']=file
        item['type']=type
        item['date']=date
        item['author']=author
        item['run_environment']=run_environment
        item['online_reading']=online_reading
        yield item










