# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Pipeline:管道，用于接收爬虫返回的item 数据
class JobspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ToCsvPipeline(object):
    def process_item(self, item, spider):
        with open("job.csv","a",encoding="gb18030") as f:

            job_name = item['job_name']
            fan_kui_lv = item['fan_kui_lv']
            job_company_name = item['job_company_name']
            job_salary = item['job_salary']
            job_place = item['job_place']

            job_time = item['job_time']
            job_type = item['job_type']
            job_info = [job_name,fan_kui_lv,job_company_name,job_salary,job_place,job_time,job_type,"\n"]
            f.write(",".join(job_info))
        #把item传递给下一个pipeline做处理
        return item

