# -*- coding: utf-8 -*-
import scrapy
import requests,xlwt

from ..items import JobItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['boss.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&scity=101020100&industry=&position=']

    def parse(self, response):

        yield scrapy.Request(
            url=response.url,
            callback=self.big_parse,
            dont_filter=True

        )


    def big_parse(self, response):
        '''
        获取职位、薪资、发布时间
        :return:
        '''
        big_a_list=response.xpath('//div[@class="job-primary"]')
        for big_a in big_a_list:
            big_href=big_a.xpath('div/h3/a/@href').extract_first("没有地址")

            big_ka=big_a.xpath('div/h3/a/@ka').extract_first("没有地址")
            # print(big_href,big_ka)
            big_href='https://www.zhipin.com'+big_href+big_ka
            job=big_a.xpath('div/h3/a/div[@class="job-title"]/text()').extract_first("没有标题")
            print(job)
            salary=big_a.xpath('div/h3/a/span[@class="red"]/text()').extract_first("没有标题")
            time=big_a.xpath('div[@class="info-publis"]/p/text()').extract_first("没有标题")
            yield scrapy.Request(
                url=big_href,
                callback=self.small_parse,
                meta={
                    'job':job,
                    'salary':salary,
                    'time':time
                },
                dont_filter=True

            )

    def small_parse(self,response):

        '''
        获取职位要求
        :return:
        '''

        job=response.meta.get('job')
        salary=response.meta.get('salary')
        time=response.meta.get('time')
        job_require = response.xpath('//div[@class="job-sec"]/div[@class="text"]/text()').extract_first("没有标题")
        print(job_require)

        item=JobItem()
        item['job']=job
        item['salary']=salary
        item['time']=time
        item['job_require']=job_require

        yield item
        # wb=xlwt.Workbook(encoding='ascii')
        # time3=time.strftime("%Y-%m-%d",time.localtime())
        # ws=wb.add_sheet(time3+'BOSS')
        # ws.write(0,0,'工作名称')
        # ws.write(0,1,'薪资')
        # ws.write(0,2,'发布时间')
        # ws.write(0,3,'工作要求')
        # wb.save('职位.xls')
















