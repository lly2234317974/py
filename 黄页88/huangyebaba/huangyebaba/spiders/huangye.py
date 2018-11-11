# -*- coding: utf-8 -*-
import scrapy,time
import re,random
from..items import HuangyebabaItem
from..settings import ua
class HuangyeSpider(scrapy.Spider):
    name = 'huangye'
    allowed_domains = ['huangye88.com']
    # start_urls = ['http://www.huangye88.com/search.html?kw=%E4%B8%AA%E4%BB%A3%E5%85%AC%E4%BB%A3%E6%95%A3%E6%88%B7%E6%8A%95%E8%B5%84&type=company&page=2/']
    def start_requests(self):
        # 96 292 313 354 381 409 415 现货
        # 35 69 83 142 147 158 161 254 257 388 403 484
        # url='http://www.huangye88.com/search.html?kw=散户投资&type=company&page=556/'
        # 大宗商品现货 51 91 156 179 255 270 278 391 406 433
        # 6 223
        # 现货贵金属---556完结
        # 个代公代 406
        # 现货贵金属,现货原油
        url='http://www.huangye88.com/search.html?kw=%E7%8E%B0%E8%B4%A7%E8%B4%B5%E9%87%91%E5%B1%9E%2C%E7%8E%B0%E8%B4%A7%E5%8E%9F%E6%B2%B9&type=company&page=198/'
        yield scrapy.Request(url,self.parse,meta={'now_num':5})
    def parse(self, response):
        now_num_page=response.meta['now_num']
        if response.status in ['504','404','502','403']:
            retry_url='http://www.huangye88.com/search.html?kw=%E7%8E%B0%E8%B4%A7%E8%B4%B5%E9%87%91%E5%B1%9E%2C%E7%8E%B0%E8%B4%A7%E5%8E%9F%E6%B2%B9&type=company&page={}/'.format(now_num_page)
            scrapy.Request(retry_url,self.parse,meta={'now_num':now_num_page})
        else:
            total=response.xpath('//div[@class="pro-left"]')
            for x in total:
                company=x.xpath('div/p/a/text()').extract_first('')
                content=x.xpath('div/ul/li[@class="com"][1]//text()').extract()
                content=''.join(content)
                content=re.sub('主营产品','',content)
                address=x.xpath('div/ul/li[2]/text()').extract_first('')
                name=x.xpath('div/ul/li[@class="fen"][1]/text()').extract_first('')
                phone=x.xpath('div/ul/li[@class="com"][last()]//text()').extract()
                phone=''.join(phone)
                phone=re.sub('电话号码','',phone)
                item = HuangyebabaItem()
                item['company'] = company
                item['content'] = content
                item['address'] = address
                item['name'] = name
                item['phone'] = phone
                yield item
            next_url = response.xpath('//a[contains(text(),"下一页")]/@href').extract_first('')
            next_url='http://www.huangye88.com'+next_url
            try:
                b=next_url.split('company')[1]
                num = re.findall('.*?page=(.*?)/', b)
            except Exception as e:
                print('error')
                num=['1']

            num=num[0]
            if '5' in num:
                time.sleep(50)
            now_page=num
            num=int(num)
            a=num-1
            print(next_url)

            if next_url=='http://www.huangye88.com':
                num_num=int(now_num_page)
                num_num-=1
                now_url='http://www.huangye88.com/search.html?kw=%E7%8E%B0%E8%B4%A7%E8%B4%B5%E9%87%91%E5%B1%9E%2C%E7%8E%B0%E8%B4%A7%E5%8E%9F%E6%B2%B9&type=company&page={}/'.format(now_num_page)
                yield scrapy.Request(now_url,callback=self.parse,dont_filter=True,meta={'now_num':now_page})
            else:
                yield scrapy.Request(next_url,callback=self.parse,dont_filter=True,meta={'now_num':now_page})


