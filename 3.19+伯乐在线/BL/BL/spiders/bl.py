# -*- coding: utf-8 -*-
import scrapy
import re
from..items import FBItem
class BlSpider(scrapy.Spider):
    name = 'bl'
    allowed_domains = ['bl.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']
    #获取详细页网址
    def parse(self, response):
        html=response.text
        pattern=re.compile('<div class="post floated-thumb">.*?<div class="clear"></div>',re.S)
        # html=str(html,encoding='utf-8')

        res=re.findall(pattern,html)
        for r in res:
            pa = re.compile('<div class="post-thumb">.*?href="(.*?)" title.*?<img src="(.*?)" alt=',re.S)
            res = re.search(pa,r)
            detail_page=res.group(1)
            src=res.group(2)

            yield scrapy.Request(url=detail_page,callback=self.detail_info,dont_filter=True,meta={'src':src})
        patt=re.compile('<div class="navigation margin-20">.*?<a class="next page-numbers" href="(.*?)">',re.S)
        next=re.findall(patt,html)
        next_page=next[0]
        print(next_page)
        yield scrapy.Request(next_page,self.parse,dont_filter=True)


    def detail_info(self,response):

        src =response.meta.get('src')#图片地址
        detail_html=str(response.body,encoding='utf-8')
        # 获取标题，发布时间
        pattern=re.compile('.*?<h1>(.*?)</h1>.*?<div.*?<p.*?>(.*?)<',re.S)
        res=re.search(pattern,detail_html)
        title=res.group(1) # 标题
        release_time=res.group(2).replace("\r\n\r\n",'').replace('&middot;','').strip(' ')# 发布时间
        release_time=release_time
        print(title,release_time)

        pattern_sec=re.compile('<span.*?>.*?<i.*?>.*?<h10.*?>(.*?)</h10>.*?<i.*?</i>(.*?)</span>.*?<i.*?</i>(.*?)</span>',re.S)
        res_sec=re.search(pattern_sec,detail_html)
        DZ=res_sec.group(1) # 点赞
        collect=res_sec.group(2) # 收藏
        comment=res_sec.group(3) # 评论
        print(comment)

        item=FBItem()
        item['src']=[src]
        item['title']=title
        item['release_time']=release_time
        item['DZ']=DZ
        item['collect']=collect
        item['comment']=comment
        yield item
