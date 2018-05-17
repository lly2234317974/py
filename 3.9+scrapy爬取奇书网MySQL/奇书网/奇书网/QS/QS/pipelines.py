# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import qishu
import MySQLdb
class QsPipeline(object):


    def __init__(self):
        self.connect =MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='qishu',
            use_unicode=True,
            charset='utf8'
        )
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):
        insert_sql='insert into qi_table(title,client_count,file,type,date,author,run_environment,online_reading) VALUES ("%s", %s, "%s", "%s", "%s", "%s", "%s", "%s")' % (item['title'],item['client_count'],item['file'],item['type'],item['date'],item['author'],item['run_environment'],item['online_reading'])

        self.cursor.execute(insert_sql)
        # commit()执行提交操作，将数据同步到数据表中。
        self.connect.commit()
        return item

    def __del__(self):
        # 当对象从内存中清空时，会执行该函数
        # 关闭数据库，关闭游标
        self.cursor.close()
        self.connect.close()




