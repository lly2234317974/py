# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class BdPipeline(object):

    def __init__(self):
        self.connect=MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='bd',
            use_unicode=True,
            charset='utf8',
        )
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        insert_sql='insert into bd_table(title,author,level,content,client,date) values("%s","%s","%s","%s","%s","%s")'%(item['title'],item['author'],item['level'],item['content'],item['client'],item['date'])
        self.cursor.execute(insert_sql)

        self.connect.commit()

        return item

    def __del__(self):
        # 当对象从内存中清空时，会执行该函数
        # 关闭数据库，关闭游标
        self.cursor.close()
        self.connect.close()