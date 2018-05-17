# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QsbkSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_src=scrapy.Field()
    alt=scrapy.Field()
    author=scrapy.Field()
    path=scrapy.Field()
