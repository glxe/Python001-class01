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

### 反爬虫：验证码识别  

### 爬虫中间件和系统代理IP  

### 自定义中间件和随机代理IP  

### 分布式爬虫  



### 