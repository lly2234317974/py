# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item
class MySQLTwistedPipeline(object):

    # 1.链接mysql数据库
    # from_settings 激活pipeline之后,会自动调用该函数加载settings中的配置
    @classmethod
    def from_settings(cls, settings):
        # 准备数据库的链接参数,是一个字典
        db_params = dict(
            host = settings['MYSQL_HOST'],
            user = settings['MYSQL_USER'],
            password = settings['MYSQL_PASSWD'],
            port = settings['MYSQL_PORT'],
            db = settings['MYSQL_DBNAME'],
            charset = settings['MYSQL_CHARSET'],
            use_unicode = True,
            # 指定使用的游标类型
            cursorclass= cursors.DictCursor
        )
        # 创建连接池
        # 1.使用的操作数据库的包名称
        # 2.准备的数据库链接参数
        db_pool = adbapi.ConnectionPool('pymysql',**db_params)
        # 返回创建好的对象
        return cls(db_pool)
    # 在初始化函数中,对db_pool进行赋值
    def __init__(self,db_pool):
        # 赋值
        self.db_pool = db_pool
    # 处理item的函数
    def process_item(self,item,spider):
        # 异步写入
        # 把执行sql的操作放入pool中
        # 1.执行的操作(功能函数) 函数对象 function类型
        # 2.item 对象 spider对象
        query = self.db_pool.runInteraction(self.insert_item,item)
        # 执行sql出现错误,会执行指定的回调函数
        query.addErrback(self.handle_error,item,spider)
        # 返回item
        return item
    # failure 错误原因
    def handle_error(self,failure,item,spider):
        # 输出错误原因
        print(failure)
    # 执行的操作
    def insert_item(self,cursor,item):
        sql = "INSERT INTO dban(rank,name,director,score,score_num,quote)VALUES (%s,%s,%s,%s,%s,%s)"
        # 执行sql
        cursor.execute(sql,(item['rank'],item['name'],item['director'],item['score'],item['score_num'],item['quote']))