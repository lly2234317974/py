#conding:utf-8
from scrapy import cmdline
# cmdline.execute(['scrapy', 'crawl', '51job', '-o', 'job.csv', '-s', 'FEED_EXPORT_ENCODING=gb18030'])
# cmdline.execute(['scrapy crawl zl'.split('')]  )
cmdline.execute('scrapy crawl 51job'.split(' '))
