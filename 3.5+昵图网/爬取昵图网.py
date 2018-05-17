#conding:utf-8
import requests
import os
from lxml import etree
url='http://www.nipic.com/photo/lvyou/index.html'
response=requests.get(url)
root=etree.HTML(response.content)
a_list=root.xpath('//div[@class="sort-nav clearfix"]/a/strong')
for a in a_list:
    big_title=a.xpath("text()")[0]
    # print(big_title)
    big_url='http://www.nipic.com/photo/lvyou/index.html'
    big_response=requests.get(big_url)
    big_root=etree.HTML(big_response.content)
    b_list=big_root.xpath("//*[@id='designSort']/div/a")
    for b in b_list:
        small_title=b.xpath("text()")[0]
        small_url=b.xpath("@href")[0]
        small_url='http://www.nipic.com'+small_url
        # print(small_title,small_url)
        path="TP/"+big_title+"/"+small_title
        if not os.path.exists(path):
            os.makedirs(path)

        one=1
        old_small_url=small_url
        while True:
            small_response=requests.get(small_url)
            small_root=etree.HTML(small_response.content)
            small_list=small_root.xpath('//li[@class="works-box mb17 fl"]/a/span/img')
            for idx,c in enumerate(small_list):
                src=c.xpath('@src')[0]
                alt=c.xpath('@alt')[0]
                print(src,alt)
                name=alt+str(one)+"-"+str(idx)+".jpg"



                img_response=requests.get(src)
                f=open(path+"/"+name,"wb")
                f.write(img_response.content)
                f.close()
            one+=1
            if one==5:
                break
            small_url=old_small_url+'?page='+str(one)
















