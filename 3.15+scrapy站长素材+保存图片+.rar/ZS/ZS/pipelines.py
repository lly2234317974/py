# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
class ZsPipeline(object):
    def process_item(self, item, spider):

        return item

class CustomFilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        # result = []
        # for src in item['down_url']:
        #     if src=0:
        #         req = Request(
        #             url=src,
        #             meta={'item': item}
        #         )
        #         result.append(req)
        # return result

        return [Request(x,meta={'item':item}) for x in item['down_url']]
    def file_path(self, request, response=None, info=None):
        name=request.meta['item']['name']
        return 'data/'+name+'/'+name+'.rar'

class CustomImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        result = []
        for src in item['img_src']:
            req = Request(
                url=src,
                meta={'item': item}
            )
            result.append(req)
        return result
    def file_path(self, request, response=None, info=None):
        name=request.meta['item']['name']
        path='data/'+name+'/'+name+'.jpg'
        return path
















