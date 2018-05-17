#conding:utf-8
import pymysql
import requests
from fake_useragent import UserAgent
from scrapy.selector import Selector
ua=UserAgent()
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='ip_list', charset='utf8')
cursor=conn.cursor()
def crawl_ip(url):
    # url='https://www.kuaidaili.com/free/inha/'
    headers={
        'User-Agent':ua.random,
        'Host':'www.kuaidaili.com',
    }
    response=requests.get(url=url,headers=headers)
    selector=Selector(text=response.text)
    list=selector.xpath('//tr')
    print(list)
    for li in list[1:]:

        ip=li.xpath('td[1]/text()').extract_first('')
        port=li.xpath('td[2]/text()').extract_first('')
        ip_type=li.xpath('td[4]/text()').extract_first('')
        # print(ip)
        mysql(ip,port,ip_type)
def mysql(ip,port,ip_type):
    query='select * from ip_table WHERE ip="%s"'%ip
    res=cursor.execute(query)
    if res!=0:
        print('该IP已存在')
        return

    insert='insert into ip_table(ip,port,ip_type)VALUES ("%s","%s","%s")'%(ip,port,ip_type)
    cursor.execute(insert)
    conn.commit()

def ul():
    for x in range(1,10):
        print('正在爬去第{}页'.format(x))
        url='https://www.kuaidaili.com/free/inha/%s/'%x
        crawl_ip(url)
if __name__=='__main__':
    ul()