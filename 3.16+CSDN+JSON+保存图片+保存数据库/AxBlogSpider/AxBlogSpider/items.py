# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AxblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    first_name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    click_num = scrapy.Field()
    src = scrapy.Field()



