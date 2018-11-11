# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AtbItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    main_business =  scrapy.Field()
    address =  scrapy.Field()
    name =  scrapy.Field()
    phone = scrapy.Field()
    number =  scrapy.Field()

# pass
