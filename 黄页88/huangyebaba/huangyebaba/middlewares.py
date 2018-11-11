# -*- coding: utf-8 -*-
# Define here the models for your spider middleware
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from scrapy import signals
from selenium import webdriver
# from fake_useragent import UserAgent
# from scrapy.downloadermiddlewares.retry import RetryMiddleware
# 代理服务器
proxyServer = "transfer.mogumiao.com:9001"
# appkey为你订单的key
proxyAuth = "Basic " + 'TDg1UmlKVWRMQUpIZUt6MDo4aHExQWJERHN3MUQ0emY2'
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer

        request.headers["Authorization"] = proxyAuth
    # def process_exception(self, request, response, spider):
    #     # self.logger.debug('Try Exception time')
    #     # self.logger.debug('Try second time')
    #     # self.logger.debug('proxyServer')
    #     request.meta["proxy"] = proxyServer
    #     request.headers["Authorization"] = proxyAuth
class UserAgentMiddleware(object):
    """This middleware allows spiders to override the user_agent"""

    def __init__(self, user_agent='Scrapy'):
        self.user_agent = UserAgent()

    @classmethod
    def from_crawler(cls, crawler):
        o = cls()
        # crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider):
        # self.user_agent = getattr(spider, 'user_agent', self.user_agent)
        pass

    def process_request(self, request, spider):
        if self.user_agent:
            request.headers.setdefault(b'User-Agent', self.user_agent.random)
