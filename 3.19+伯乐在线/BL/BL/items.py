# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class FBItem(scrapy.Item):
    src=scrapy.Field()
    title=scrapy.Field()
    release_time=scrapy.Field()
    DZ=scrapy.Field()
    collect=scrapy.Field()
    comment=scrapy.Field()

