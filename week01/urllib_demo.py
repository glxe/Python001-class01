from urllib import request


myurl = 'https://movie.douban.com/top250'

resp = request.urlopen('https://movie.douban.com/')
print(resp.read().decode())