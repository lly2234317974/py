#conding:utf-8
import requests
import random
import re
import urllib.request
url='https://www.qiushibaike.com/'
User_Agentlist=[
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
    "Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
]
ip_list=[
    '122.114.31.177":808',
    '58.216.202.149:8118',
    '120.77.254.116:3128',
    '60.205.125.201:8888'
]
def QSBK(page):
    abs_url=url+'8hr/page/'+str(page)+'/'
    headers={
        'User-Agent':random.choice(User_Agentlist)
    }
    request=urllib.request.Request(abs_url,headers=headers)
    response=urllib.request.urlopen(request)
    #获取网页源代码
    html=response.read()


    pattern=re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>',re.S)
    content_list=re.findall(pattern,html.decode('utf-8'))
    for content in content_list:
        print('用户昵称：',content[0].strip('\n'))
        print('内容是：',content[1].strip('\n').replace('<br/>',''))
        author=content[0].strip('\n')
        content_con=content[1].strip('\n').replace('<br/>','')
        with open('QSBK.txt','a',encoding='utf-8') as f:
            f.write(author)
            f.write('\n')
            f.write(content_con)
            f.write('\n')
            f.write('\n')




QSBK(1)