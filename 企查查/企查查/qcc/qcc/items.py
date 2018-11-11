# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QccItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    name = scrapy.Field()
    mail = scrapy.Field()
    phone = scrapy.Field()
    gengduo = scrapy.Field()
