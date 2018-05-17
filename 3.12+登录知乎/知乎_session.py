#conding:utf-8
from fake_useragent import UserAgent
import requests
import http.cookiejar as cookiejar
import re,time,codecs
class ZhuHu(object):
    def __init__(self,phone_num,password):
        self.url='https://www.zhihu.com/signin'############
        self.headers={
            'Referer':'https://www.zhihu.com/signup?next=%2F',
            'Host':"www.zhihu.com",
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        }
        self.phone_num=phone_num
        self.password=password
        self.ua=UserAgent()
        self.filename=phone_num+'.txt'
        self.session=requests.Session()
        # LWPCookieJar是python中管理cookie的工具，可以将cookie保存到文件，或者在文件中读取cookie数据到程序
        self.session.cookies=cookiejar.LWPCookieJar(filename=self.filename)
    def get_cookies(self):

        response=self.session.get(self.url, headers=self.headers)
        res=response.headers['Set-Cookie']
        xsrf=re.search(re.compile(r'_xsrf(.*?);'),res)
        xsrf=xsrf.group(1)
        self.login(xsrf)
    def login(self,xsrf):
        url='https://www.zhihu.com/login/phone_num'##############
        data={
            '_xsrf':xsrf,
            'phone_num':self.phone_num,
            'password':self.password
        }
        response=self.session.post(url,data=data,headers=self.headers)
        self.session.cookies.save()

    def get_index_page(self):
        response = self.session.get("https://www.zhihu.com", headers=self.headers)
        # 'wb'：让写入的数据以二进制格式进行写入，通常用在写入图片，音频，视频等资源时。
        with open('index.html', 'wb') as file_test:
            file_test.write(response.content)
        print('写入成功！')
        # res=response.json()
        # if res.get('r')==0:
        #     self.session.cookies.save()
        # else:
        #     print(response.json().get('msg'))
        #     print('正在尝试重新登录')
        #     time.sleep(1)
        #     self.login(xsrf)
if __name__=='__main__':
    # a=ZhuHu('15736959834','199666lly')
    # a.get_cookies()
    user_info = [
        # {'phone_num':'18337152380','password':'shutun0315'},
        {'phone_num': '1573659834', 'password': '199666lly'},
    ]
    for user in user_info:
        zh = ZhuHu(user['phone_num'], user['password'])
        zh.get_cookies()
    # import random
    # # 随机获取一个cookie,用来发送请求
    # user = random.choice(user_info)
    #
    # with requests.Session() as session:
    #     # 随机加载本地的cookie文件
    #     session.cookies =cookieJar.LWPCookieJar()
    #     session.cookies.load(filename=user['phone_num']+'.txt')
    #     # 发请求
    #     response = session.get('http://www.zhihu.com',headers={
    #         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    #         "Referer": "https://www.zhihu.com/signup?next=%2F",
    #         "Host": "www.zhihu.com"
    #     })
    #     # 保存
    #     with codecs.open('zhihu.html','w',encoding='utf-8') as f:
    #         f.write(response.text)
