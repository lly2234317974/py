# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YunqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class YunfirstItem(scrapy.Item):
    img_src=scrapy.Field()
    title=scrapy.Field()
    author=scrapy.Field()
    xs_type=scrapy.Field()
    xs_state=scrapy.Field()
    refresh_time=scrapy.Field()
    xs_num=scrapy.Field()
    xs_url=scrapy.Field()
    xs_id=scrapy.Field()

class DetailItem(scrapy.Item):
    click_num=scrapy.Field()
    total_rq=scrapy.Field()
    total_tj=scrapy.Field()
    month_click=scrapy.Field()
    month_rq=scrapy.Field()
    month_tj=scrapy.Field()
    week_click=scrapy.Field()
    week_rq=scrapy.Field()
    week_tj=scrapy.Field()
    tag=scrapy.Field()
    total_pl=scrapy.Field()
    xs_id=scrapy.Field()

