# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import xlwt
from scrapy import Request
class BlPipeline(object):
    def process_item(self, item, spider):
        return item


class ExcelPipeline(object):
    def __init__(self):
        self.workbook=xlwt.Workbook()
        self.sheet=self.workbook.add_sheet('伯乐')
        self.sheet.write(0,0,'标题')
        self.sheet.write(0,1,'发布时间')
        self.sheet.write(0,2,'点赞数')
        self.sheet.write(0,3,'收藏数')
        self.sheet.write(0,4,'评论数')
        self.sheet.write(0,5,'图片地址')
        self.count=1
    def process_item(self,item, spider):
        self.sheet.write(self.count,0,item['title'])
        self.sheet.write(self.count,1,item['release_time'])
        self.sheet.write(self.count,2,item['DZ'])
        self.sheet.write(self.count,3,item['collect'])
        self.sheet.write(self.count,4,item['comment'])
        self.sheet.write(self.count,5,item['src'])
        self.count += 1
        self.workbook.save('伯乐在新.xls')

class TPImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        result=[]
        for r in item['src']:
            req=Request(url=r,meta={'item':item})
            result.append(req)
        return result
    def file_path(self, request, response=None, info=None):
        title=request.meta['item']['title']
        path='images/'+title+'/'+title+'.jpg'
        return path

