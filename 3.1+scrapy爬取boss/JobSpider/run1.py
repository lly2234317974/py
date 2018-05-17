#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy import cmdline
# cmdline.execute('scrapy crawl job'.split(' '))
cmdline.execute('scrapy crawl zl'.split(' '))
"""
显著提升爬虫效率的方式:
    1.换个性能更好的机器
    2.网络使用光纤
    3.多线程
    4.多进程
    5.分布式
    6.提升数据的写入速度
反爬虫的应对措施:
    1.随机修改User-Agent
    2.禁用Cookie追踪
    3.放慢爬虫速度
    4.使用代理,动态更换ip(电脑ip不变,动态IP指的是代理的IP)
    5.分布式(一般用不同区域的电脑,不能在一个局域网)
"""
