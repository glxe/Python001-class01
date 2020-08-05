## 学习笔记
***
## week six 作业  

* [作业一]()
* [作业二]()

***

## 开发环境配置
***
[Django 官方文档](https://docs.djangoproject.com/zh-hans/3.0)  

MVC设计模式

MTV 框架模式

![MTV 框架模式](./67e9db068e2780d3b1fac968530981a.png)

***特点***
* 采用了MTV的框架  
* 强调快速开发和代码复用 DRY(Do Not Repeat Yourself)  
* 组件丰富：  
    - ORM(对象关系映射)映射类来构建数据模型  
    - URL 支持正则表达式  
    - 模板可继承  
    - 内置用户认证，提供用户认证和权限功能  
    - admin 管理系统  
    - 内置表单模型、Cache缓存系统、国际化系统等  

Django的安装：  
`pip install --upgrade django==2.2.13` 安装指定的版本  
检查是否安装成功 
```python
import django

print(django.get_version())
# 2.2.13
```
如果是输出对应的版本号，则表示安装成功

(LTS) 对当前的软件版本会长期支持

## 创建项目和目录结构
****
1、创建Django的项目  
2、创建应用程序  
3、启动程序  

创建项目：`django-admin startproject MyDjango`，创建好的目录结构：
```python

MyDjango/
    -manage.py # 命令行工具
    -MyDjango/
        -__init__.py
        -settings.py  # 项目的配置文件
        -urls.py
        -wsgi.py
```
创建应用程序：`python manage.py startapp index`，目录结构：
```python
index/
    -admin.py # 管理后台
    -apps.py # 当前app配置文件
    -migrations/ # 数据库迁移文件
        - __init__.py
    -models.py # 模型
    -tests.py # 自动化测试
    -views.py # 视图
```
使用 `python manage.py help` 命令查看该工具的具体功能。

使用 `python manage.py runserver` 命令启动程序，默认运行的是 `127.0.0.1:8000` ，`python manage.py runserve 0.0.0.0:80` 更改运行端口，使用 `CONTROL-C` 退出程序。

## 解析settings.py主要配置文件
***
配置文件包括：
* 项目路径  
* 密钥  
* 域名访问权限  
* App列表  
* 静态资源，包括CSS，JavaScript图片等  
* 模板文件  
* 数据库配置  
* 缓存  
* 中间件  

主要对 `INSTALLED_APPS` 配置添加自己的应用程序和 `DATABASES` 改成mysql
## urls调度器
***
定义程序的入口，主要用于接收用户的请求信息，附带一些django自己需要的信息，有django中间件。
***Django如何处理一个求情***  
当一个用户请求Django站点的一个页面：  
1. 如果传入 `HttpRequest` 对象拥有 `urlconf` 属性（通过中间件设置），它的值将被用来代替 `ROOT_URLCONF` 设置。  
2. Django 加载 `URLconf` 模块并寻找可用的 `urlpatterns`，Django一次匹配每个URL模式，在与请求的URL匹配的第一个模式停下来。  
3. 一旦有URL匹配成功，Django导入并调用相关的视图，视图会获得如下参数：
    - 一个 `HTTPRequest` 实例  
    - 一个或多个位置参数提供  
4. 如果没有 URL 匹配，或者匹配过程中出现了异常，Django 会调用一个适当的错误处理视图。  

urls.py 的基本配置
```python
from django.contrib import admin
from django.urls import path, ***include***

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
]
```

```python
# index/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
```
```python
# index/views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello Django!')
```

## 模块和包
***
* 模块：.py结尾的python程序  
* 包：存放多个模块的目录  
* `__init__.py`：包运行的初始化文件，可以是空文件  

常见以下几种导入方式：`import`, `from ... import ...`, `from ... import ... as ...`  

执行：
```python
if __name__ == '__main__':
    fun()
# 这个就是可执行，可模块导入
```
import 引用包的时候，会默认的去python的 site-packages 目录里找。
`from . import package` ，这个是在当前的目录里寻找模块。  
## 让URL支持变量
***
类似于node的路由表。  
* 带变量的URL，Django 支持对URL设置变量，URL变量类型包括：
    - str  
    - int  
    - slug(备注)  
    - uuid  
    - path    

`path('<int:year>', views.myyear)`，在函数里，函数的参数时 `year`  
在views文件的函数里，第一个参数必须是 `request`,  第二个才是业务参数，可以是可变长参数 `**kwargs`, 然后在函数里使用 `kwargs['name']` 来获取值。

```python
# path('<int:year>', views.myyear)
def myyear(request, year):
    print(dir(request))
    for r in request:
        print(r)
    return HttpResponse(year)


# path('<int:year>/<str:name>', views.name)
def name(request, **kwargs):
    return HttpResponse(f"year: {kwargs['year']}, name: {kwargs['name']}")
```

## URL正则和自定义过滤器
***
当URL的变量已经不支持你的业务需求了，则正则和自定义过滤器就派上用场了。  
`re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear')`, 正则需要使用 `re_path` 这个方法  

## view视图快捷方式
view视图：  
|响应类型|说明|
|-|-|
|HttpResponse('Hello World!')|HTTP状态码 200，请求已成功被服务器接收|
|HttpResponseRedirect('/admin/')|HTTP状态码 302，重定向Admin站点的URL|
|HttpResponsePremanentRedirect('/admin/')|HTTP状态码 301，永久重定向admin站点URL|
|HttpResponseBadRequest('BadRequest')|HTTP状态码 400，访问的页面不存在或者请去错误|
|HttpResponseNotFound('Not Found')|HTTP状态码 404，页面不存在或者网页的URL失效|
|HttpResponseForbidden('Forbidden')|HTTP状态码 403，没有访问权限|
|HttpResponseNotAllowed('Not Allowed Get')|HTTP状态码 405，不允许使用该请求方式|
|HttpResponseServerError('Server Error')|HTTP状态码 500，服务器内部错误|

Django 快捷函数  
`render()`  
将给定的模板与给定的上下文字典组合在一起，并以渲染的文本返回一个 `HttpResponse` 对象  
`redirect()`  
将一个 `HttpResponseRedirect` 返回到传递的参数的适当URL  
`get_object_or_404()`  
在给定的模型管理器(model manager)上调用get()，但它会引发 Http 404 而不是模型的DoesNoExist异常  

## 使用ORM创建数据表
***
模型与数据库  
* 每个模型都是一个 Python 的类，这些类继承 `django.db.models.Model`  
* 模型类的每个属性都对应数据库表的字段  
* 利用这些，Django提供一个自动生成访问数据的API  
```python
from django.db import models
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
# 对应下面的数据库表
```

```sql
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
);
```
这是由模型创建表
`python manage.py makemigrations`, `python manage.py migrate`
由表创建模型
`python manage.py inspectdb > app_name/models.py`
## ORM API
***     
## Django模板开发
***
* 变量：  
    - `My first name is {{ first_name }}. My last name is {{ last_name }}.` 
* 标签：
    - `{% if user.is_authenticated %}Hello, {{ user.username }}.{% endif %}`
## 展示数据库中的内容

## 豆瓣页面展示功能的需求分析

## urlconf与models 配置

## views视图的编写

## 结合bootstrap模板进行开发

## 如何阅读Django的源代码

## manage.py源码分析