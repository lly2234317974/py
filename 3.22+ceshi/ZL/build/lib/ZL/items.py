# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZlzpItem(scrapy.Item):
    job_name=scrapy.Field()
    FYE=scrapy.Field()
    company=scrapy.Field()
    salary=scrapy.Field()
    min_salary=scrapy.Field()
    max_salary=scrapy.Field()
    address=scrapy.Field()