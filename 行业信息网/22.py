import requests
proxy_a = requests.get(
    'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=0&city=0&yys=0&port=1&pack=23443&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=130000').text
print(proxy_a)