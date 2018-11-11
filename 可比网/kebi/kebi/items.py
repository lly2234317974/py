# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KebiItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    name = scrapy.Field()
    # pass

    phone= scrapy.Field()
    number= scrapy.Field()
    address= scrapy.Field()