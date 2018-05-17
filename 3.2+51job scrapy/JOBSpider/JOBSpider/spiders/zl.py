# -*- coding: utf-8 -*-
import scrapy
from ..items import JOBspiderItem


class ZlSpider(scrapy.Spider):
    name = 'zl'
    allowed_domains = ['baidu.com']
    start_urls = [
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3%2B%E6%AD%A6%E6%B1%89&kw=python&sm=0&p=1',
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3%2B%E6%AD%A6%E6%B1%89&kw=php&sm=0&p=1',
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3%2B%E6%AD%A6%E6%B1%89&kw=java&sm=0&p=1']

    def parse(self, response):

        yield scrapy.Request(
            url=response.url,
            callback=self.parse_job_info,
            meta={},
            dont_filter=True,
        )

    def parse_next_page(self, response):
        next_page = response.xpath('//a[text()="下一页"]/@href').extract_first(' ')
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse_job_info,
                meta={},
                dont_filter=True,
            )


    def parse_job_info(self, response):
        zl_table_list = response.xpath('//div[@id="newlist_list_content_table"]/table[@class="newlist"]')
        for zl_table in zl_table_list[1:]:
            # 有足够td才可以使用，
            # zl_td_list=zl_table.xpath('tr[1]/td')
            # td1=zl_table_list[0]
            # td2=zl_table_list[1]
            # td3=zl_table_list[2]
            # td4=zl_table_list[3]
            # td5=zl_table_list[4]
            # 查找元素尽量使用xpath定位，少用索引，可能会发生索引越界
            # .extract()：把列表里的元素转换成文本，本身还是列表
            # extract_first(' '):把列表里元素转换成文本并取出第一个，如果取不到返回默认值
            td1 = zl_table.xpath('tr/td[@class="zwmc"]/div/a//text()').extract()
            # 去空格
            td1 = map(str.strip, td1)
            job_name = "".join(td1)
            fan_kui_lv = zl_table.xpath('tr/td[@class="fk_lv"]/span/text()').extract_first('没有反馈率').strip()
            job_company_name = zl_table.xpath('tr/td[@class="gsmc"]/a[1]/text()').extract_first('没有公司名称').strip()
            job_salary = zl_table.xpath('tr/td[@class="zwyx"]/text()').extract_first('面议').strip()
            job_place = zl_table.xpath('tr/td[@class="gzdd"]/text()').extract_first('没有地址').strip()
            job_time='不存在'
            job_type='智联招聘' if 'zhaopin.com' in response.url else '其他'

            print(job_name, fan_kui_lv, job_company_name, job_salary, job_place)
            item = JOBspiderItem()
            item['job_name'] = job_name
            item['job_company_name'] = job_company_name
            item['job_place'] = job_place
            item['job_salary'] = job_salary
            item['job_time'] = job_time
            item['job_type'] = job_type
            item['fan_kui_lv'] = '没有反馈率'
            yield item
        yield scrapy.Request(
            url=response.url,
            callback=self.parse_next_page,
            meta={},
            dont_filter=True,
        )
