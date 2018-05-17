# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import xlwt
class NhdzPipeline(object):
    def process_item(self, item, spider):
        return item


class SQPipeline(object):
    def __init__(self):
        self.connect=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456',db='nhdz',use_unicode=True,charset='utf8')
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):
        insert_sql='insert into nh_table(author,content) VALUES ("%s","%s")'% (item['author'],item['content'])
        self.cursor.execute(insert_sql)
        self.connect.commit()
        return item
    def __del__(self):
        self.cursor.close()
        self.connect.close()


class ExcelPipeline(object):
    def __init__(self):
        self.workbook=xlwt.Workbook(encoding='utf-8')
        self.sheet=self.workbook.add_sheet('内涵',cell_overwrite_ok=True)
        self.sheet.write(0,0,'author')
        self.sheet.write(0,1,'content')
        self.count=1
    def process_item(self,item,spider):
        self.sheet.write(self.count,0,item['author'])
        self.sheet.write(self.count,1,item['content'])
        self.count+=1
        self.workbook.save('内涵段子.xls')
        return item
    # def close_spider(self,spider):
    #     self.workbook.save('内涵段子.xls')
