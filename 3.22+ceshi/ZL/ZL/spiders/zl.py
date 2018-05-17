# -*- coding: utf-8 -*-
import scrapy

from..items import ZlzpItem
class ZlSpider(scrapy.Spider):
    name = 'zl'
    allowed_domains = ['zl.com']
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7%2B%E5%8C%97%E4%BA%AC%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3%2B%E6%AD%A6%E6%B1%89&kw=python&p=1&isadv=0']

    def parse(self, response):

        #职位，反馈率 公司，薪水，地址，发布时间
        table_list=response.xpath('//table[@class="newlist"]')
        for table in table_list[1:]:
            job=table.xpath('tr/td/div/a//text()').extract()
            job_name = "".join(job)
            # job_name=job_name.replace('\xa0','')
            FYE=table.xpath('tr/td/span/text()').extract_first('无反馈率')
            company=table.xpath('tr/td/a/text()').extract_first('')
            salary=table.xpath('tr/td[@class="zwyx"]/text()').extract_first('面议')
            #try except
            if salary != '面议' and salary != '1000元以下':
                min_salary=salary.split('-')[0]
                max_salary=salary.split('-')[1]
            else:
                min_salary='面议'
                max_salary='面议'
            address=table.xpath('tr/td[@class="gzdd"]/text()').extract_first('无')
            time=table.xpath('tr/td[@class="gxsj"]/span/text()').extract_first('无')
            # print(job_name)
            item=ZlzpItem()
            item['job_name']=job_name
            item['FYE']=FYE
            item['company']=company
            item['salary']=salary
            item['min_salary']=min_salary
            item['max_salary']=max_salary
            item['address']=address
            yield item
            next_page=response.xpath('//a[contains(text(),"下一页")]/@href').extract_first('')
        yield scrapy.Request(url=next_page,callback=self.parse,dont_filter=True)
