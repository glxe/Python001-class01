# 学习笔记（week one）

## 使用python库获取豆瓣影评

#### 1、用requests写一个最简单的爬虫  

开发程序的四个步骤：**提出需求、编码、代码run起来，修复和完善**  
使用requests库，伪造user-agent，来获取网页的源代码。当然requests不仅仅获取网页源码，还携带cookie，身份认证，代理支持，文件分块上传，下载等等很多的事情。

#### 2、使用BeautifulSoup解析爬取到的网页  

安装第三方库需要使用 **pip**，具体使用方法：
```
pip install other
```

或者使用此命令来迁移代码，如下命令：
```
pip install -r requirements.txt
// requirements.txt 为约定俗成的文件名
```
这样，就能不同的机器或不同的环境下统一第三方包的版本了。

引入第三方库的方式：
```
方式1
import package
方式2
from libray import package [as alias]
```

使用beautifulSoup库的例子：
```
import requests
from bs4 import BeautifulSoup as b4


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
header = {'user-agent': user_agent}
myurl = 'https://movie.douban.com/top250'
respone = requests.get(myurl, headers=header,
                       auth=('15370383786', 'xxxx'))


bs_info = b4(respone.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a', ):
        print(atag.get('href')) #获取所有连接
        print(atag.find('span',).text) #获取电影名称
```


#### 3、使用XPath解析网页  
#### 4、实现爬虫的自动翻页功能  
#### 5、Python基础语法的回顾  
#### 6、前端基础：HTML结构  
#### 7、前端基础：HTTP协议  
#### 8、Scrapy框架结构解析  
#### 9、Scrapy爬虫目录结构解析  
#### 10、将requests爬虫改写为Scrapy爬虫  
#### 11、通过Scrapy爬虫爬取电影详情页信息  
#### 12、XPath详解  
#### 13、Scrapy选择器  

