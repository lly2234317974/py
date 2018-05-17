# -*- coding: utf-8 -*-
import scrapy,json

from..items import NhdzItem
class NhSpider(scrapy.Spider):
    name = 'nh'
    allowed_domains = ['nh.com']
    start_urls = ['http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=152124']

    def parse(self, response):
        rs=json.loads(response.text)
        data_first=rs.get('data')
        print(data_first)

        max_time=data_first.get('max_time')
        data_list=data_first.get('data')
        for data in data_list:
            content=data.get('group').get('content')
            author=data.get('group').get('user').get('name')

            with open('nhdz.txt','a',encoding='utf-8') as f:
                f.write(author)
                f.write('\n')
                f.write(content)
                f.write('\n')
                f.write('\n')

            print(content)

            item=NhdzItem()


            item['content']=content
            item['author']=author
            yield item


        next_url='http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time='+str(max_time)
        print(next_url)
        yield scrapy.Request(next_url,dont_filter=True)


























