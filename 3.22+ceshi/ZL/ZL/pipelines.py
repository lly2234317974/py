# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt
import pymysql
class ZlPipeline(object):
    def process_item(self, item, spider):
        return item

class ExcelPipeline(object):
    def __init__(self):
        self.workbook=xlwt.Workbook(encoding='utf-8')
        self.sheet=self.workbook.add_sheet('zhilian')
        self.sheet.write(0, 0, '职位')
        self.sheet.write(0, 1, '反馈率')
        self.sheet.write(0, 2, '公司名称')
        self.sheet.write(0, 3, '薪资')
        self.sheet.write(0, 4, '最低薪资')
        self.sheet.write(0, 5,'最高薪资')
        self.sheet.write(0, 6, '工作地点')
        self.count=1
    def process_item(self, item, spider):
        self.sheet.write(self.count,0,item['job_name'])
        self.sheet.write(self.count,1,item['FYE'])
        self.sheet.write(self.count,2,item['company'])
        self.sheet.write(self.count,3,item['salary'])
        self.sheet.write(self.count,4,item['min_salary'])
        self.sheet.write(self.count,5,item['max_salary'])
        self.sheet.write(self.count,6,item['address'])
        self.count+=1

        self.workbook.save('智联招聘.xls')
        return item

class MySQLPipelinea(object):
    def __init__(self):
        self.connect=pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='zl',charset='utf8')
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):
        insert_sql='insert into zl_table(job_name,FYE,company,salary,min_salary,max_salary,address) VALUES ("%s","%s","%s","%s","%s","%s","%s")' % (item['job_name'],item['FYE'],item['company'],item['salary'],item['min_salary'],item['max_salary'],item['address'])
        self.cursor.execute(insert_sql)
        self.connect.commit()
        return item
    def __del__(self):
        self.cursor.close()
        self.connect.close()
