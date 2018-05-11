# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
# import codecs,os,json
class YunqiPipeline(object):
    def process_item(self, item, spider):
        return item

class ExcelfirstPipeline(object):
    def __init__(self):
        self.workbook=xlwt.Workbook(encoding='utf-8')
        self.sheet=self.workbook.add_sheet('信息')
        self.sheet.write(0,0,'图片地址')
        self.sheet.write(0,1,'标题')
        self.sheet.write(0,2,'作者')
        self.sheet.write(0,3,'类型')
        self.sheet.write(0,4,'状态')
        self.sheet.write(0,5,'更新时间')
        self.sheet.write(0,6,'小说字数')
        self.sheet.write(0,7,'小说链接')
        self.sheet.write(0,8,'小说ID')
        self.count=1
    def process_item(self,item,spider):
        self.sheet.write(self.count,0,item['img_src'])
        self.sheet.write(self.count,1,item['title'])
        self.sheet.write(self.count,2,item['author'])
        self.sheet.write(self.count,3,item['xs_type'])
        self.sheet.write(self.count,4,item['xs_state'])
        self.sheet.write(self.count,5,item['refresh_time'])
        self.sheet.write(self.count,6,item['xs_num'])
        self.sheet.write(self.count,7,item['xs_url'])
        self.sheet.write(self.count,8,item['xs_id'])
        self.count+=1
        self.workbook.save('小说信息.xls')
        return item

class DetailPipeline(object):
    def __init__(self):
        self.workbook=xlwt.Workbook(encoding='utf-8')
        self.sheet=self.workbook.add_sheet('详细信息')
        self.sheet.write(0,0,'小说ID')
        self.sheet.write(0,1,'小说标签')
        self.sheet.write(0,2,'总点击数')
        self.sheet.write(0,3,'月点击数')
        self.sheet.write(0,4,'周点击数')
        self.sheet.write(0,5,'总人气')
        self.sheet.write(0,6,'月人气')
        self.sheet.write(0,7,'周人气')
        self.sheet.write(0,8,'总推荐')
        self.sheet.write(0,9,'月推荐')
        self.sheet.write(0,10,'周推荐')
        self.sheet.write(0,11,'评论数')
        self.count=1
    def process_item(self,item,spider):
        self.sheet.write(self.count,0,item['xs_id'])
        self.sheet.write(self.count,1,item['tag'])
        self.sheet.write(self.count,2,item['click_num'])
        self.sheet.write(self.count,3,item['month_click'])
        self.sheet.write(self.count,4,item['week_click'])
        self.sheet.write(self.count,5,item['total_rq'])
        self.sheet.write(self.count,6,item['month_rq'])
        self.sheet.write(self.count,7,item['week_rq'])
        self.sheet.write(self.count,8,item['total_tj'])
        self.sheet.write(self.count,9,item['month_tj'])
        self.sheet.write(self.count,10,item['week_tj'])
        self.sheet.write(self.count,11,item['total_pl'])
        self.count+=1
        self.workbook.save('小说详细信息.xls')
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
        sql = "INSERT INTO yq_table(xs_id,img_src,title,author,xs_type,xs_state,refresh_time,xs_num,xs_url)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # 执行sql
        cursor.execute(sql,(item['xs_id'],item['img_src'],item['title'],item['author'],item['xs_type'],item['xs_state'],item['refresh_time'],item['xs_num'],item['xs_url']))

class DetailMySQLTwistedPipeline(object):

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
        sql = "INSERT INTO detail_table(xs_id,tag,click_num,month_click,week_click,total_rq,month_rq,week_rq,total_tj,month_tj,week_tj,total_pl)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # 执行sql
        cursor.execute(sql,(item['xs_id'],item['tag'],item['click_num'],item['month_click'],item['week_click'],item['total_rq'],item['month_rq'],item['week_rq'],item['total_tj'],item['month_tj'],item['week_tj'],item['total_pl']))

class JsonfirstPipeline(object):
    def __init__(self):
        self.file = codecs.open('first.json', 'w+', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        # 判断是否为分类item
        # if item.get('img_src'):
        #     print('这是分类item,不需要保存数据')
        #     # 直接返回item
        #     return item
        # 博文item
        item = dict(item)
        json_str = json.dumps(item)
        self.file.write(json_str)
        self.file.write(',')
        return item

    def close_spider(self, spider):
        self.file.seek(-1, os.SEEK_END)
        self.file.truncate()
        self.file.write(']')
        self.file.close()