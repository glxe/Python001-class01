import requests
# from fake_useragent import UserAgent
import time

# ua = UserAgent(verify_ssl=False)

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    'Referer': 'https://accounts.douban.com/passport/login?source=main'
}

# 会话对象：在同一个Session实例发出的所有请求之间保持cookie
# 期间使用urllib3的connection pooling功能
# 向同一主机发送多个请求，底层的TCP链接将会被重用，从而带来显著的性能提升
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    'ck': '',
    'name': '15888888888',
    'password': 'sfds',
    'remember': 'false',
    'ticket': ''
}


with requests.Session() as s:
    # post数据前获取cookie
    pre_login = 'https://accounts.douban.com/passport/login'
    pre_resp = s.get(pre_login, headers=header)
    res = s.post(url=login_url, data=form_data, headers=header, cookies=s.cookies)
    print(res.json())


print(res.json())

order_rul = "https://www.douban.com/mine/orders/"
res = s.get(order_rul, headers=header, cookies=s.cookies)

print(res.text)



