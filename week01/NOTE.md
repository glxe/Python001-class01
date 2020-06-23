# 学习笔记（week one）

## 使用python库获取豆瓣影评

#### 1、用requests写一个最简单的爬虫  

开发程序的四个步骤：**提出需求、编码、代码run起来，修复和完善**  
本篇的需求是爬取豆瓣的top250的电影数据

使用 [requests](https://requests.readthedocs.io/zh_CN/latest/) 库，伪造user-agent，来获取网页的源代码。当然requests不仅仅获取网页源码，还携带cookie，身份认证，代理支持，文件分块上传，下载等等很多的事情。

#### 2、使用BeautifulSoup解析爬取到的网页  
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/) 是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间.

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
lxml是处理XML和HTML的python语言，解析的时候，自动处理各种编码问题。而且它天生支持 XPath 1.0、XSLT 1.0、定制元素类。
安装：
```
    pip install lxml
```

```
html 实例

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Study/title>
</head>
<body>

<h1>webpage</h1>
<p>source link</p>
<a href="http://www.runoob.com/html/html-tutorial.html" target="_blank">HTML</a> 
<a href="http://www.runoob.com/python/python-tutorial.html" target="_blank">Python</a>
<a href="http://www.runoob.com/cplusplus/cpp-tutorial.html" target="_blank">C++</a> 
<a href="http://www.runoob.com/java/java-tutorial.html" target="_blank">Java</a>
</body>
</html>


html（变量）， html.html（文件名）将被用于下面
```
用法：  
（1）HTML读取

```
#直接读取
html = "html内容";
from lxml import etree
html = etree.HTML(html)
```
（2）获取标签
获取所有a标签，这种html内容有多种写法，可以直接得到4个元素
```
# //a: 获取html下的所有a标签 
a_tags = html.xpath('//a')


# /html/body/a: 沿着节点顺序找a标签
a_tags = htmlObj.xpath('/html/body/a/text()')


# /descendant::a: 当前节点后代里面找a标签
a_tags = htmlObj.xpath('/descendant::a/text()')

```
xpath的选择器可以通过chrome浏览器的开发者工具里的 Elements选项卡在对应的html标签上右击选择copy XPath。  

Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。  
DataFrame：二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器。

使用lxml 和 pandas 库的例子：
```
import requests
import lxml.etree
url = "https://movie.douban.com/subject/1292052/"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"

# 声明为字典使用字典的语法赋值
header = {}
header['user-agent'] = userAgent
response = requests.get(url, headers = header)

# print(response.text)
# xml化处理
selector = lxml.etree.HTML(response.text)

#电影名称
movieName = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称：{movieName}')
#上映日期
date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{date}')
#评分
score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分：{score[0]}')

details = [movieName[0], date[0], score[0]]
# print(details)
import pandas as pd
movieOne = pd.DataFrame(data = details)
movieOne.to_csv('./movieOne.csv', encoding = 'utf8', index = False, header = False)
```

#### 4、实现爬虫的自动翻页功能  

小结：
```
import requests
from bs4 import BeautifulSoup as b4
from lxml import etree
import pandas as pd


def getCurrentPageByUrl(url):
    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    response = requests.get(url, headers = header)
    htmlStr = response.text
    htmlObj = etree.HTML(htmlStr)
    # //*[@id="content"]/div/div[1]/ol/li[1]/div/div
    movieNames = htmlObj.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div/a/span[1]/text()')
    movieDetailUrls = htmlObj.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/@href')
    
    print(movieNames)
    print(movieDetailUrls)
    details = [movieNames, movieDetailUrls]
    data = pd.DataFrame(data = details)
    data.to_csv('./movieOne.csv', encoding = 'utf8', index = False, header = False, mode='a') # 追加写入文件


from time import sleep

url = "https://movie.douban.com/top250"

#生成所有页面的urls元祖
urls = tuple(f'https://movie.douban.com/top250?start={page * 25}' for page in range(10))
print(urls)
# getCurrentPageByUrl(url)

for url in urls:
    getCurrentPageByUrl(url)
    sleep(5)
```

#### 5、Python基础语法的回顾  
#### 6、前端基础：HTML结构  
#### 7、前端基础：HTTP协议  
#### 8、Scrapy框架结构解析  
#### 9、Scrapy爬虫目录结构解析  
#### 10、将requests爬虫改写为Scrapy爬虫  
#### 11、通过Scrapy爬虫爬取电影详情页信息  
#### 12、XPath详解  
#### 13、Scrapy选择器  

