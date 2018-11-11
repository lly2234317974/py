# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi
class MysqlPipeline(object):
    def __init__(self,db_pool):
        self.db_pool=db_pool
    #     query=self.db_pool.runInteraction(self.creat_table)
    # def creat_table(self,cursor):
    #     sql="create table if not exists qihuo(company varchar(40),main_business varchar(250),address varchar(50),name varchar(20),phone varchar(50),number varchar(30))"
    #     cursor.execute(sql)
    @classmethod
    def from_settings(cls,settings):
        db_params=dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            port=settings['MYSQL_PORT'],
            db=settings['MYSQL_DB'],
            charset=settings['MYSQL_CHARSET'],
            use_unicode= True,
            cursorclass=cursors.DictCursor

        )
        db_pool=adbapi.ConnectionPool('pymysql',**db_params)
        return cls(db_pool)

    def process_item(self,item,spider):
        query=self.db_pool.runInteraction(self.insert_item,item)
        query.addErrback(self.handle_error,item,spider)
        return item
    def handle_error(self,failure,item,spider):
        print(failure)
    def insert_item(self,cursor,item):
        sql='insert into qihuo(company,main_business,address,name,phone,number)VALUES (%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql,(item['company'],item['main_business'],item['address'],item['name'],item['phone'],item['number']))
