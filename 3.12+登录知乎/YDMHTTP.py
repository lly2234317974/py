import http.client, mimetypes, urllib, json, time, requests
from http import cookiejar
######################################################################

class YDMHttp:
    # 配置用户信息\软件信息
    apiurl = 'http://api.yundama.com/api.php'
    username = 'jiaqianzhen'
    password = 'jia563344943'
    appid = '4600'
    appkey = 'e290551f95fecf15554d48736faf8851'

    def __init__(self):
        self.username = 'lly2234317974'
        self.password = '123456789'
        self.appid = '4600'
        self.appkey = 'e290551f95fecf15554d48736faf8851'

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response
    # 查询剩余题分
    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001
    # 登录
    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001
    # 上传识别图片
    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if (cid > 0):
            for i in range(0, timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def report(self, cid):
        data = {'method': 'report', 'username': self.username, 'password': self.password, 'appid': self.appid, 'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
        response = self.request(data)
        if (response):
            return response['ret']
        else:
            return -9001

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb');
        res = requests.post(url, files=files, data=fields)
        return res.text

######################################################################


if __name__ == '__main__':


    url = 'http://www.yundama.com/index/login?'

    captcha_url = 'http://www.yundama.com/index/captcha'

    session = requests.Session()
    session.cookies = cookiejar.LWPCookieJar(filename='ydm.txt')
    response = session.get(captcha_url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
    })
    with open('captcha.jpg','wb') as f:
        f.write(response.content)

    # 用户名
    username    = 'jiaqianzhen'

    # 密码
    password    = 'jia563344943'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid       = 4600

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey      = 'e290551f95fecf15554d48736faf8851'

    # 图片文件
    filename    = 'captcha.jpg'

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype    = 5000

    # 超时时间，秒
    timeout     = 60

    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp()

        # 登陆云打码
        uid = yundama.login();
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance();
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout);
        print('cid: %s, result: %s' % (cid, result))

        login_url = 'http://www.yundama.com/index/login?username=%s&password=%s&utype=1&vcode=%s'%(username,password,result)
        response = session.get(login_url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
        })
        session.cookies.save()

        response = session.get('http://www.yundama.com/user',headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
        })
        print(response.text)








######################################################################







