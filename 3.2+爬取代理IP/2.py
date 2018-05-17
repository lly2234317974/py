#conding:utf-8
import re
from bs4 import BeautifulSoup
from lxml import etree
from urllib import request,parse
from fake_useragent import UserAgent
'''
正则    最难     高
bs4     中等难度 中
xpath   最简单   低
json解析



'''

class QSWSpider(object):
    def __init__(self):
        self.ua= UserAgent()
        self.baseurl = 'https://www.qisuu.com/'
        self.headers={
            'User-Agent':self.ua.random,
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        self.html=''
    def get_html(self,url):

        self.headers['User-Agent']=self.ua.random
        req=request.Request(url,headers=self.headers)
        response=request.urlopen(req)
        self.html=response.read().decode('utf-8')
    def parse_categray(self):
        # pattern=re.compile('<div class="nav".*?<a.*?href="(.*?)"',re.S)
        # res=re.search(pattern,self.html)
        # # print(res)
        # if res:
        #     print(res.group(1))
        # else:
        #     print('没有找到分类')


        bs=BeautifulSoup(self.html,'lxml')
        # .nav a:nth-of-type伪类选择器，找到class为nav下的第二个a标签
        # res=bs.select('.nav a:nth-of-type(2)')
        res=bs.select('.nav a')[1]
        # print(res)
        # #提取href属性值
        #
        category_link=res['href']
        # print(category_link)


        # 3.xpath
        # doc=etree.HTML(self.html)
        # res=doc.xpath('')[0]
    def parse_detail(self):
        #1.正则
        pattern=re.compile('<div class="s".*?<a.*?href="(.*?)"')








    def start(self):
        self.get_html(self.baseurl)
        self.parse_categray()



if __name__=='__main__':
    a=QSWSpider()
    a.start()






















