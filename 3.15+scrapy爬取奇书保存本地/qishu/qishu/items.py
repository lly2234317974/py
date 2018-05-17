# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QishuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    cate = scrapy.Field()
    star = scrapy.Field()
    detail_url = scrapy.Field()
    src = scrapy.Field()
    name = scrapy.Field()
    click_num = scrapy.Field()
    file_size = scrapy.Field()
    book_type = scrapy.Field()
    update_time = scrapy.Field()
    status = scrapy.Field()
    author = scrapy.Field()
    run_type = scrapy.Field()