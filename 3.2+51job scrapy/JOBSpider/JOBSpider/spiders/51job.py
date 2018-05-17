# -*- coding: utf-8 -*-
import scrapy,requests
from ..items import JOBspiderItem

'''
提高爬虫效率：
1.网络使用光纤
2.多线程
3.多进程
4.分布式
5.使用性能更好的机器
6.提升数据的写入速度

'''
class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.com']
    start_urls = [ 'http://search.51job.com/list/020000%252C080200%252C180200%252C040000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=','http://search.51job.com/list/020000%252C080200%252C180200%252C040000,000000,0000,00,9,99,java,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=','http://search.51job.com/list/020000%252C080200%252C180200%252C040000,000000,0000,00,9,99,php,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']

    def parse(self, response):
        '''

        :param response:
        :return:
        '''
        yield scrapy.Request(
            url=response.url,
            callback=self.parse_job_info,
            meta={},
            dont_filter=True,

        )
        # yield scrapy.Request(
        #     # url=response.url,
        #     callback=self.parse_job_info,
        #     meta={},
        #     dont_filter=True,
        # )

    def parse_next_page(self,response):

        '''
        解析下一页
        :param response:
        :return:
        '''
        # .extract_first('')取出列表转化为字符串
        next_page=response.xpath('//li[@class="bk"][2]/a/@href').extract_first(' ')
        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse_job_info,
                meta={},
                dont_filter=True,
            )

            '''
            递归：一个函数内部自己调用自己
            '''
    def parse_job_info(self,response):
        '''

        :param response:
        :return:
        '''
        job_div_list=response.xpath('//div[@id="resultList"]/div[@class="el"]')
        for job_div in job_div_list:
            job_name=job_div.xpath('p/span/a/@title').extract_first('无工作').strip()
            job_company_name=job_div.xpath('span[@class="t2"]/a/@title').extract_first('无公司信息').strip()
            job_place=job_div.xpath('span[@class="t3"]/text()').extract_first('无工作地点').strip()
            job_salary=job_div.xpath('span[@class="t4"]/text()').extract_first('无名称').strip()
            job_time=job_div.xpath('span[@class="t5"]/text()').extract_first('无时间信息').strip()
            job_type='51job' if '51job.com' in response.url else '其他'
            print(job_type,job_name,job_company_name, job_place,job_salary,job_time)
            '''
            数据清洗：清除数据两端的空行特殊字符
            常用：strip
            '''
            item=JOBspiderItem()
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



