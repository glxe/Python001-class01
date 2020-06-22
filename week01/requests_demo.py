import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

respone = requests.get(myurl, headers=header,
                       auth=('15370383786', 'xxxx'))

print(respone.text)
print(f'返回码是：{respone.status_code}')
