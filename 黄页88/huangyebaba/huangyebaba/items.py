# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuangyebabaItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    content = scrapy.Field()
    address = scrapy.Field()
    name = scrapy.Field()
    phone = scrapy.Field()
    # pass
