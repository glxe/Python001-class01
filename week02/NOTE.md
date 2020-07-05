# 学习笔记（week two）  
***
## week two 作业  

* [作业一]()
* [作业二]()

***

## 掌握Scrapy爬虫框架  

### 异常捕获与处理  
所有内置的非系统退出的异常都派生子Exception类  
StopIteration 异常示例：
```python
gen = (i for i in range(0, 2))
print(next(gen))
print(next(gen))
try:
    print(next(gen))
except: StopIteration:
    print('最后一个元素')
```
通过Traceback函数去追踪错误。  
**异常处理机制的原理**  
* 异常也是一个类  
* 异常捕获过程  
    1. 异常类把错误信息打包到一个对象  
    2. 然后对该对象自动查找到调用栈  
    3. 知道运行系统找到明确声明如何处理这些异常的位置  
* 所有异常继承自BaseException  
* Traceback显示出错了的位置，显示的顺序和异常信息对象传播的方向是相反的  

- 异常信息在Traceback信息的最后一行，有不同的类型  
- 捕获异常可以使用try...except语法   
- try...except支持多重异样处理  

常见的异常类型主要有：  
1. LookupError下的IndexError 和 KeyError  
2. IOError  
3. NameError  
4. TypeError  
5. AttributeError  
6. ZeroDivisionError

异常的例子：
```python
def f1():
    1/0

def f2():
    list1 = []
    # 这里会出现异常 list index out of range 被捕获输出，
    list1[1]
    #这里将不会运行
    f1()

def f3():
    f2()

try:
    f3()
except (ZeroDivisionError, Exception) as e:
    print(e)  
```

自定义异常类：
```python

class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    # 魔术函数
    def __str__(self):
        return self.errorinfo

userInput = 'a';

try:
    if (not userInput.isdigit()):
        raise UserInputError('用户输入错误') # 主动抛出错误
except UserInputError as ue:
    print(ue)
finally:
    del userInput
```

读取文件处理：
```python
# 传统的打开文件写法
file1 = open('a.txt', encoding='utf8')
try:
    data = file1.read()
finally:
    file1.close()

# with
with open('a.txt', encoding='utf8') as file1: #自动close文件流
    data = file1.read()
```

customer with exemple:
```python

class Open:
    def __init__(self):
        pass
    
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, type, value, trace):
        print('eixt')
        return self

    def __call__(self, a):
        print('call')
        print(a)
        pass

with Open() as f: # 这里的 f 其实是Open类中__enter__返回的值，
    f('a')
    pass
```

错误示例：
```python
class Open:
    def __enter__(self):
        print('enter')

    def __exit__(self, type, value, trace):
        print('eixt')

    def __call__(self, a):
        print('call')
        print(a)
        pass

with Open() as f:
    f('a')
    pass

#上面的这个代码运行会报下面的错误

# error.py 49 <module>
# f('a')

# TypeError:
# 'NoneType' object is not callable
# 因为f的值是__enter__的返回值，而上面这段代码是没有返回值的，即None，则运行的代码是None('a')，所以这是错误的
```
* [美化错误类库：pretty_errors](https://pypi.org/project/pretty-errors/)  
* [try 语句官方文档](https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-try-statement)  
* [with 语句官方文档](https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-with-statement)  
* [with 语句上下文管理器官方文档](https://docs.python.org/zh-cn/3.7/reference/datamodel.html#with-statement-context-managers)  


### 使用PyMySQL进行数据库操作  

```
# 安装python mysql客户端
pip install PyMySQL
```

pymysql操作示例：
```python


# 开始-创建connection-获取cursor-CURD（增删查改）-关闭cursor-关闭connection-结束

import pymysql

dbInfo = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'test'
}

sqls = ['select 1', 'select VERSION()']

result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls ):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 实际应用中要进行复用，可以节省服务资源

        # 游標建立的時候就開啟了一個隱形的事務
        cur = conn.cursor()
        print(cur)
        try:
            for command in sqls:
                cur.execute(command)
                result.append(cur.fetchone())
                
            #關閉游標
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()
# 主程序的入口 如果是被当做模块文件引入，则不会执行此段代码，只有单独运行才会执行
if __name__ == "__main__":
    db = ConnDB(dbInfo=dbInfo, sqls=sqls)
    db.run()
    print(result);
```
**Type Hint（类型提示）** Python3开始引入的。但这只是一种注解，并不能在运行的时候去检查对与错。  详细的使用可以参考[博文](https://juejin.im/post/5b478b396fb9a04fe25ebf45)  
```python
#函数定义返回值
def add(x:int,y:int)->int:
    return x+y

print(add(10,12))
print(add('hello','world')) # 无法做到检查


# 变量的定义
x:int = 10
y:str = 'hello'
c:list = []
```
```python
import pymysql

conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'rootroot',
                       database = 'test',
                       charset = 'utf8mb4'
                        )

# 获得cursor游标对象
con1 = conn.cursor()

# 操作的行数
count = con1.execute('select * from tb1;')
print(f'查询到 {count} 条记录')


# 获得一条查询结果
result = con1.fetchone()
print(result)

# 获得所有查询结果
print(con1.fetchall())

con1.close()
conn.close()

# 执行批量插入
# values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
# cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)
```
* [MySQL 官方文档手册](https://dev.mysql.com/doc/)  
* [MySQL 官方下载连接](https://www.mysql.com/downloads/)  
* [PyMySQL 官方文档](https://pypi.org/project/PyMySQL/)  

### 反爬虫：模拟浏览器头部的信息  
* [User-Agent 参考文档](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/User-Agent)

怎么识别爬虫：
* 根据基本的请求
    1.带http头信息：如user-agent、referer  
    2.带cookies（包含加密的用户名、密码验证信息）
* 根据浏览行为  

```
模拟user-agent库
pip install fake_useragent
```
```python
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)

ua.chrome

```
### 反爬虫：cookies验证  
**[A simple HTTP Request & Response Service.](https://httpbin.org/)**  
```python
import requests

#GET 请求

r = requests.get('https://www.baidu.com')
r.status_code
r.text
print(r.json)

# POST 请求

r = requests.post('https://httpbin.org/post')

print(r.json())



# 在同一个Session实例发出的所有请求之间保持cookie
s = requests.session()

s.get('https://httpbin.org/cookies/set/aaa/4444')

r = s.get('https://httpbin.org/cookies')

print(r.json())
# https://httpbin.org/cookies/set/aaa/4444

# 也可以使用上下文管理器
with requests.session() as s:
    a = s.get('https://httpbin.org/cookies/set/aaa/4444')
    print(a.json())
```

模拟douban登录：
```python
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
    'name': '15899998888',
    'password': 'aaaaa',
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
```
### 反爬虫：使用WebDriver模拟浏览器行为  
* [Selenium-自动化测试工具](http://www.selenium.org.cn/)，*Selenium测试直接运行在浏览器中，就像真正的用户在操作一样*  

web自动化测试工具集，包括IDE、Grid、RC（selenium 1.0）、WebDriver（selenium 2.0）等。  
* [WebDriver 文档1](https://www.selenium.dev/selenium/docs/api/py/)  
* [WebDriver 文档2](https://www.w3.org/TR/webdriver/)  

webdriver 和 浏览器之间还需要一个驱动，[ChromeDriver 下载地址](https://chromedriver.storage.googleapis.com/index.html)，当然在下载的时候需要注意，ChromeDriver的版本号要和Chrome版本号对应。然后选择自己操作系统对应的安装包。windows直接是个执行文件，可以直接丢掉python的bin目录里，也可以单独放在一个目录，但一定要住，需要把这个目录放到环境变量中。  

豆瓣和石墨的登录示例：
```python
from selenium import webdriver
import time


# 豆瓣登录
try:
    browser = webdriver.Chrome()

    browser.get('https://douban.com')
    time.sleep(1)

    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('15888888888')
    browser.find_element_by_xpath('//*[@id="password"]').send_keys('sdfss')
    time.sleep(1)
    loginBtn = browser.find_element_by_xpath('//a[@class="btn btn-account btn-active"]')
    loginBtn.click()

    cookies = browser.get_cookies()
    print(cookies)
    
    # ///html/body/div[1]/div[2]/div[1]/div[5]/a
except Exception as e:
    pass
finally:
    print('end')

# 石墨登录

try:
    browser = webdriver.Chrome()

    browser.get('https://shimo.im/welcome')
    time.sleep(2)
    browser.find_element_by_xpath('//button[@class="login-button btn_hover_style_8"]').click()
    time.sleep(3)
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('15888888888')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('sdfs')
    time.sleep(2)
    loginBtn = browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]')
    loginBtn.click()

    cookies = browser.get_cookies()
    print(cookies)
    
except Exception as e:
    pass
finally:
    print('end')
    browser.close()

```

下载图片示例：
```python
#file download
imageRrl = 'https://img1.doubanio.com/view/photo/l/public/p624842928.webp'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
r = requests.get(imageRrl, headers = headers) # 一开始没加headers 然后http status code 是418()。加了headers就正常了
print(r.content)
with open('p624842928.webp', 'wb') as f:
    f.write(r.content)
```
[HTTP status code 418的梗](https://www.zhihu.com/question/41318710/answer/90500171)

下载文件实例：
```python
###  大文件下载
#  如果文件比较大的话，那么下载下来先放在内存中，内存还是有很大的压力的
# 所以为了防止内存被消耗完，我们需要想办法把下载的文件分块写到磁盘中

fileUrl = "https://v3-tt.ixigua.com/24e0d689616c1bb6a2a330a3004425e3/5efb6afd/video/tos/cn/tos-cn-vd-0026/8c2711bab29540b5a11b2d48303b7029/media-video-avc1/?a=1768&br=5856&bt=1952&cr=0&cs=0&dr=0&ds=3&er=0&l=202006302335560100140440810439D94E&lr=default&mime_type=video_mp4&qs=2&rc=Mzc2cjlrcG08dDMzZzczM0ApZTQ4ZmY6NDxnN2ZlPDtlZWcxLWteYy5zZWdfLS0xLS9zc2A2MC82NWIxYS8yNmBjXjA6Yw%3D%3D&vl=&vr="
fileName = "8c2711bab29540b5a11b2d48303b7029.mp4";
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
r = requests.get(fileUrl, headers = headers, stream = True) # 一开始没加headers 然后http status code 是418([418的梗](https://www.zhihu.com/question/41318710/answer/90500171))。加了headers就正常了
# print(r.content)

with open(fileName, 'wb') as f:
    for chunk in r.iter_content(chunk_size = 1024):
        if chunk:
            f.write(chunk)
```
### 反爬虫：验证码识别  
识别验证码示例：
```python
# 需要先安装图片依赖库 libpng，jpeg，libtiff，leptonica
# mac系统使用brew install libpng jpeg libtiff leptonica
# 安装图片文字处理工具 Tesseract
# // 安装tesseract的同时安装训练工具

# brew install --with-training-tools tesseract

# // 安装tesseract的同时安装所有语言，语言包比较大，如果安装的话时间较长，建议不安装，按需选择

# brew install --all-languages tesseract

# // 安装tesseract，并安装训练工具和语言

# brew install --all-languages --with-training-tools tesseract

# // 只安装tesseract，不安装训练工具

# brew install tesseract

# 然后还需要安装支持python的库，pip3 install Pillow pytesseract

import requests
import os
import pytesseract
from PIL import Image

codeUrl = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2282030598,1303150352&fm=26&gp=0.jpg'
header = {
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
r = requests.get(codeUrl, headers = header)

with open('code.jpeg', 'wb') as f:
    f.write(r.content)


# 打开文件
im = Image.open('code.jpeg')
# im.show()

# 灰度处理
gray = im.convert('L')
gray.save('code_gray.jpeg')
im.close()

# 二值化
th = 120
table = []
for i in range(256):
    if i < th:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table, '1')
out.save('code_th.jpeg')

th = Image.open('code_th.jpeg')

codeStr = pytesseract.image_to_string(th, lang = 'eng')
th.close()
print(codeStr)
```
* [基于Tesseract的OCR识别](https://www.jianshu.com/p/f0f05ff2dc2e)
* [各种语言识别库](https://github.com/tesseract-ocr/tessdata)
### 爬虫中间件和系统代理IP  
***中间件***主要对Spider蜘蛛以及Downloader下载器来做增强，或定制化开发，从而开发出可以适应不同情况的爬虫。当然中间件可以有多个。优先级。根据权重值，来使多个中间件的先后运行顺序
* [Scrapy详解之中间件（Middleware）](https://zhuanlan.zhihu.com/p/42498126)

[问题1](#wenti1)
```python

# -*- coding: utf-8 -*-
import scrapy

# windows中执行不成功

#export http_proxy = "http://52.179.231.206:80"
# setting 增加scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过 Request.meta['proxy'] 读取 http_proxy 环境变量加载代理

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text)

```
```
scrapy crawl httpbin --nolog # 不打印debug日志
```
### 自定义中间件和随机代理IP  
如何编写一个下载中间件？一般需要重写下面四个主要方法：
* ***process_request(request, spider)*** Request 对象经过下载中间件时会被调用，优先级高的先调用  
* ***process_response(request, response, spider)*** Response 对象经过下载中间件时会被调用，优先级高的后调用  
* ***process_exception(request, exception, spider)*** 当 process_exception() 和 process_request() 抛出异常是会被调用  
* ***from_crawler(cls, crawler)*** 使用crawler 来创建中间件对象，并（必须）返回一个中间件对象   
### 分布式爬虫  

Scrapy 原生不支持分布式，多机之间需要实现redis队列和管道共享，而scrapy-redis很好的实现了Scrapy和redis的集成
使用scrapy-redis之后Scrapy主要的变化：
1.使用RedisSpider类替代了Spider类
2.Scheduler的queue由Redis实现
3.item pipeline 由redis实现

安装并开启 ```pip install scrapy-redis```


开启redis并以守护进程方式：在redis.conf中加入 ```daemonize yes``` 后即可以守护进程方式运行


```python
# setting 
#redis info
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

#scheduler queue
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'

#remove duplicate
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

#requests default queue priority
#Requests的默认优先级队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'

# 将Requests队列持久化到Redis，可支持暂停或重启爬虫
SCHEDULER_PERSIST = True

# 将爬取到的内容 保存到redis
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
```

```python
# 保存百度首页
import scrapy
from redemospider.items import RedemospiderItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
       print(response.text)
       text = response.text
       item = RedemospiderItem()
       item['text'] = text
       yield item

```

## <a id="wenti1">问题1</a>
在 设置环境变量时，linux和winsows是不同，linux中 ```export http_proxy="http://52.179.231.206:80"``` ，windows是 ```set http_proxy="http://52.179.231.206:80"``` ,然后linux能执行成功。windows却不行？