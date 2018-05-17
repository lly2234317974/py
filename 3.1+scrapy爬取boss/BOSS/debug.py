#conding:utf-8
from scrapy import cmdline
cmdline.execute(['sccrapy','crawl','boss','-o', 'img.csv', '-s', 'FEED_EXPORT_ENCODING="gb18030"'])