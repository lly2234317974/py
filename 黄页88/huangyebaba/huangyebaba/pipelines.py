# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
class JobPipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlPipeline(object):
    def __init__(self, db_pool):
        # 赋值
        self.db_pool = db_pool
    #     query = self.db_pool.runInteraction(self.creat_table)
    #
    # def creat_table(self, cursor):
    #
    #     sql="create table if not exists gedaigongdai(company varchar(30),content varchar(200),address varchar(100),name varchar(30),phone varchar(60))"
    #     cursor.execute(sql)
    @classmethod
    def from_settings(cls, settings):
        # 准备数据库的链接参数,是一个字典
        db_params = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWD'],
            port=settings['MYSQL_PORT'],
            db=settings['MYSQL_DB'],
            charset=settings['MYSQL_CHARSET'],
            use_unicode=True,
            # 指定使用的游标类型
            cursorclass=cursors.DictCursor
        )
        # 创建连接池
        # 1.使用的操作数据库的包名称
        # 2.准备的数据库链接参数
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        # 返回创建好的对象
        return cls(db_pool)

    # 在初始化函数中,对db_pool进行赋值

    # 处理item的函数
    def process_item(self, item, spider):
        # 异步写入
        # 把执行sql的操作放入pool中
        # 1.执行的操作(功能函数) 函数对象 function类型
        # 2.item 对象 spider对象
        query = self.db_pool.runInteraction(self.insert_item, item)
        # 执行sql出现错误,会执行指定的回调函数
        query.addErrback(self.handle_error, item, spider)
        # 返回item
        return item

    # failure 错误原因
    def handle_error(self, failure, item, spider):
        # 输出错误原因
        print(failure)
    def insert_item(self,cursor,item):
        sql = "insert into gedaigongdai(company,content,address,name,phone) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (item['company'],item['content'],item['address'],item['name'],item['phone']))
