#conding:utf-8
import requests
from lxml import etree
from urllib import request
import MySQLdb
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='ip',charset='utf8')
cursor=conn.cursor()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
for i in range(1,4):
    url='http://www.xicidaili.com/nn/{0}'.format(i)
    req=request.Request(url,headers=headers)
    response=request.urlopen(req)
    html=response.read().decode('utf-8')
    doc=etree.HTML(html)
    ip_list=doc.xpath('//table/tr/td[2]/text()')
    port_list=doc.xpath('//table/tr/td[3]/text()')
    for x in range(len(ip_list)):
        ip=ip_list[x]
        port=port_list[x]
        cursor.execute("insert into ip_list(ip,port) VALUES ('{0}','{1}')".format(ip,port))
        conn.commit()




        print(ip)