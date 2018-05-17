#conding:utf-8
import re,requests
import http.cookiejar as cookiejar
url=''

headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
    'Referer':'https://www.zhihu.com/signup?next=%2F',
'Host':"www.zhihu.com"
}
filename='num'+'.txt'
session=requests.Session()
session.cookies=cookiejar.LWPCookieJar(filename=filename,)

