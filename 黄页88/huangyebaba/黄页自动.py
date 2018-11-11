from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql
import time
import re,random
browser = webdriver.Chrome()
# proxy_list=[{

# }]
# proxy=random.choice(proxy_list)

browser.get('http://so.cnlinfo.net/sonew/SearchCompanyNew.aspx?kw=%E6%8A%95%E8%B5%84&pagenum=1')
# browser.find_element_by_xpath('//*[@id="hs_3"]').click()#公司
# browser.find_element_by_xpath('//*[@id="search_btn"]/input').click()#第一页

# conn=pymysql.connect(host='localhost',user='root',passwd='123456',port=3306,db='kehuziliao')
# cur=conn.cursor()
# import random

num=0
while num<2394:
    kehu_name=browser.find_elements_by_xpath('//div[@class="content"]/ul/li/div/div//ul/li')

    for x in kehu_name:
        first=x.text
        phone=re.findall("1\d{10}", first)
        # phone=phone[0]
        if len(phone)!=0:
            print(phone[0])
            conn = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, db='kuaichedao',charset="utf8")
            cur = conn.cursor()
            sql='insert into touzi(phone)VALUES (%s)'
            cur.execute(sql,(phone[0]))
            cur.close()
            conn.commit()
            conn.close()
    a = random.uniform(4,9)
    time.sleep(a)
    num += 1

    if num==1:

        browser.find_element_by_xpath('.//*[@id="sTop"]/div[1]/div[2]/div/a/i').click()
    else:
        try:
            content=browser.find_element_by_xpath(".//*[@id='sTop']/div[1]/div[2]/div/a[2]").click()

        except Exception as e:
            print(e)
            # browser.find_element_by_xpath('//*[@id="sTop"]/div[1]/div[2]/div/a[1]/i').click()
            # browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            # browser.find_element_by_xpath('//div[@class="pages"]/a').click()
