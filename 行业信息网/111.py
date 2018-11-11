import requests
from lxml import etree
import pymysql
import socket,time
# 蘑菇代理的隧道订单
appKey = "TDg1UmlKVWRMQUpIZUt6MDo4aHExQWJERHN3MUQ0emY2"

# 蘑菇隧道代理服务器地址
ip_port = 'transfer.mogumiao.com:9001'

socket.setdefaulttimeout(3)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置

proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {"Proxy-Authorization": 'Basic '+ appKey}
def main(url):
    r = requests.get(url, headers=headers, proxies=proxy,verify=False,allow_redirects=False)
    print(r.status_code)
    r.encoding='utf-8'
    return r.text
    # if r.status_code == 302 or r.status_code == 301 :
    #     loc = r.headers['Location']
    #     url_f = "https://ip.cn" + loc
    #     print(loc)
    #     r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    #     print(r.status_code)
    #     print(r.text)
def second(html):
    selector=etree.HTML(html)
    next_page = selector.xpath('//ul/li/p[1]/a/@href')
    for x in next_page:
        next_page_url = x
        print(next_page_url)
        response= requests.get(next_page_url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
        response.encoding = 'utf-8'
        htmll=response.text
        selec = etree.HTML(htmll)
        phone = selec.xpath('//div[@class="dialog"]/div[2]/text()')
        phone=''.join(phone)
        print(phone)
        try:
            con = pymysql.connect(host='localhost', user='root', passwd='123456', db='kuaichedao', port=3306,
                                  charset='utf8')
            curr = con.cursor()
            sql = 'insert into phone(phone)VALUES (%s)'
            curr.execute(sql%(phone))
            con.commit()
            con.close()
        except Exception as e:
            pass

    for x in range(123, 585):
        next_url = 'http://so.cnlinfo.net/sonew/SearchCompanyNew.aspx?kw=%E6%8A%95%E8%B5%84={}'.format(x)
        res = requests.get(next_url, headers=headers, proxies=proxy, verify=False, allow_redirects=False,timeout=2)
        time.sleep(1)
        return second(res.text)
def third(phone):
    pass
if __name__ == '__main__':

    url="http://so.cnlinfo.net/sonew/SearchCompanyNew.aspx?kw=%E6%8A%95%E8%B5%84=122"
    html=main(url)
    htmll=second(html)
    # print(htmll)
    # third(ht//mll)
    # phone=1

