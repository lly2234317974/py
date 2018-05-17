# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class QSItem(scrapy.Item):
    title=scrapy.Field()
    client_count=scrapy.Field()
    file=scrapy.Field()
    type=scrapy.Field()
    date=scrapy.Field()
    author=scrapy.Field()
    run_environment=scrapy.Field()
    online_reading=scrapy.Field()
