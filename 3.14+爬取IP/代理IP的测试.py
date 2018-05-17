#conding:utf-8

from urllib import request
# url='http://www.baidu.com'
# # 根据代理IP创建代理对象
# proxy_ip={'http':'221.224.49.237:3128'}
# proxy_handler=request.ProxyHandler(proxy_ip)
# opener=request.build_opener(proxy_handler)
# # request.install_opener(opener)
#
# response=opener.open(url)
# print(response.read().decode('utf-8'))

ip_list=[
    '112.95.56.203:8118',
    '222.76.187.42:8118',
    '122.114.31.177:808',
    '183.23.75.66: 	61234',
    '106.122.171.49:8118',
    '115.208.199.4:808',
    '61.135.217.7:80',
]
for ip in ip_list:
    try:
        proxy_han=request.ProxyHandler({'http':ip})
        opener=request.build_opener(proxy_han)
        request.install_opener(opener)
        #设置超时时间timeout
        resp=opener.open('http://www.baidu.com',timeout=0.6)
        print(len(resp.read().decode('utf-8')))
    except Exception as e:
        print(ip,'不可用')
        print('原因是：',e)
    else:
        print(ip,'可用 ')
        with open('ip.txt','wb') as f:
            #str转化为bytes类型
            ip=ip.encode(encoding='utf-8')
            f.write(ip)
        

















