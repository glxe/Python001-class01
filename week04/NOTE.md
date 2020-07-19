## 学习笔记 

***
## week four 作业  

* [作业一](task.md)
* [作业二]()

***

## 数据清洗与预处理

#### pandas 简介  

* [pandas 中文文档](https://www.pypandas.cn/)  
* [安装参考文档](https://pypi.org/project/sklearn-pandas/1.5.0)  
* [Numpy 学习文档](https://numpy.org/doc/)  
* [matplotlib 学习文档](https://matplotlib.org/contents.html)  

**Pandas** 是 Python 的核心数据分析支持库，提供了快速、灵活、明确的数据结构，旨在简单、直观地处理关系型、标记型数据。Pandas 的目标是成为 Python 数据分析实践与实战的必备高级工具，其长远目标是成为**最强大、最灵活、可以支持任何语言的开源数据分析工具**。经过多年不懈的努力，Pandas 离这个目标已经越来越近了。  

**Pandas 适用于处理以下类型的数据：**

* 与 SQL 或 Excel 表类似的，含异构列的表格数据;  
* 有序和无序（非固定频率）的时间序列数据;  
* 带行列标签的矩阵数据，包括同构或异构型数据;  
* 任意其它形式的观测、统计数据集, 数据转入 Pandas 数据结构时不必事先标记。  

Pandas 的主要数据结构是 Series（一维数据）与 DataFrame（二维数据），这两种数据结构足以处理金融、统计、社会科学、工程等领域里的大多数典型用例。对于 R 用户，DataFrame 提供了比 R 语言 data.frame 更丰富的功能。Pandas 基于 NumPy 开发，可以与其它第三方科学计算支持库完美集成。

Pandas 就像一把万能瑞士军刀，下面仅列出了它的部分优势 ：

* 处理浮点与非浮点数据里的缺失数据，表示为 NaN；
* 大小可变：插入或删除 DataFrame 等多维对象的列；
* 自动、显式数据对齐：显式地将对象与一组标签对齐，也可以忽略标签，在 Series、DataFrame 计算时自动与数据对齐；
* 强大、灵活的分组（group by）功能：拆分-应用-组合数据集，聚合、转换数据；
* 把 Python 和 NumPy 数据结构里不规则、不同索引的数据轻松地转换为 DataFrame 对象；
* 基于智能标签，对大型数据集进行切片、花式索引、子集分解等操作；
* 直观地合并（merge）、**连接（join）**数据集；
* 灵活地重塑（reshape）、**透视（pivot）**数据集；
* 轴支持结构化标签：一个刻度支持多个标签；
* 成熟的 IO 工具：读取文本文件（CSV 等支持分隔符的文件）、Excel 文件、数据库等来源的数据，利用超快的 HDF5 格式保存 / 加载数据；
* 时间序列：支持日期范围生成、频率转换、移动窗口统计、移动窗口线性回归、日期位移等时间序列功能。
* 这些功能主要是为了解决其它编程语言、科研环境的痛点。处理数据一般分为几个阶段：数据整理与清洗、数据分析与建模、数据可视化与制表，Pandas 是处理数据的理想工具。


Pandas 的一些示例：
```python
import pandas as pd
import numpy as np
import matplotlib as plt
import os 


pwd = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(pwd, 'data.csv')
print(file)

df = pd.read_csv(file)

print(df)
# 筛选标题为 还行 这一列
print(df['还行'])

# 切片方式筛选
print(df[:3])

# 增加列名
df.columns = ['star', 'vote', 'shorts']

# 显示特定的行、列
df.loc[1:3, ['star']]

# 过滤数据
df['star'] == '力荐'


```

#### pandas 基本数据类型  
Pandas 两个数据类型
* Series （一维）
* DataFrame （二维）

Series示例：
```python
import pandas as pd
import numpy as np

# 从列表创建Series
pd.Series(['a', 'b', 'c'])
# 0    a
# 1    b
# 2    c
# dtype: object
# 自动创建索引

# 通过字典创建带索引的Series
s1 = pd.Series({'a':11, 'b':22, 'c':33})
# 通过关键字创建带索引的Series
s2 = pd.Series([11, 22, 33], index = ['a', 'b', 'c'])
s1
s2

# 获取全部索引
s1.index
# 获取全部值
s1.values

# 类型
type(s1.values)    # <class 'numpy.ndarray'>
type(np.array(['a', 'b']))

# 转换为列表
s1.values.tolist()

# 使用index会提升查询性能
#    如果index唯一，pandas会使用哈希表优化，查询性能为O(1)
#    如果index有序不唯一，pandas会使用二分查找算法，查询性能为O(logN)
#    如果index完全随机，每次查询都要扫全表，查询性能为O(N)

# 取出email
emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
import re
pattern ='[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
emails[mask]
```

DataFrame 示例：
```python
  
import pandas as pd


# 列表创建dataframe
df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
# 嵌套列表创建dataframe
df2 = pd.DataFrame([
                     ['a', 'b'], 
                     ['c', 'd']
                    ])
# 自定义列索引
df2.columns= ['one', 'two']
# 自定义行索引
df2.index = ['first', 'second']

df2
# 可以在创建时直接指定 DataFrame([...] , columns='...', index='...' )
# 查看索引
df2.columns, df2.index
type(df2.values)
```
#### 数据导入  

数据一般都是从execl，csv，或者数据等作为来源进行导入的。
当然Pandas 都是支持这些的，使用的read_*()的函数
示例：
```python
import pandas as pd
# pip install xlrd ,execl 文件需要这个库的支持
# 导入excel文件
excel1 = pd.read_excel(r'1.xlsx')
excel1
# 指定导入哪个Sheet
pd.read_excel(r'1.xlsx',sheet_name = 0)

# 支持其他常见类型
pd.read_csv(r'c:\file.csv',sep=' ', nrows=10, encoding='utf-8')

pd.read_table( r'file.txt' , sep = ' ')

import pymysql
sql  =  'SELECT *  FROM mytable'
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df = pd.read_sql(sql,conn)


# 熟悉数据
# 显示前几行
excel1.head(3)

# 行列数量
excel1.shape

# 详细信息
excel1.info()
excel1.describe()
```

#### 数据预处理  
在实际处理原始数据的时候，就像自己买菜做饭，你去菜场买的菜就是原始数据，当然原始数据的获取途径有多种，爬虫爬取，自己生产的等。
然后你需要把买回来的菜需要先第一步清理，把坏的菜叶，或者明显的缺胳膊少腿的给清理掉。原始数据也是，需要先把缺失的数据，重复的数据
该填充的填充，该删除的删除。这就是数据预处理

示例：
```python

import pandas as pd
import numpy as np

x = pd.Series([1, 2, 5, np.nan, 78, 5, np.nan])
print(x)
# 检验是否存在缺失值
print(x.hasnans)

# 将缺失值填充为平均值
ss = x.fillna(value = x.mean())
print(ss)



df = pd.DataFrame({
    "A": [1,2,3],
    "B": [89, np.nan, 43],
    "C": [np.nan, 56, 89],
    "D": [63, 4, 9]
})

print(df.isnull().sum()) # 查看缺失值汇总

print(df.ffill()) # 用上一行填充
print(df.ffill(axis=1)) # 用前一列填充

print(df)

print(df.info())
print(df.dropna())

print(df.fillna('无'))

print(df.drop_duplicates())
```
#### 数据调整  
```python

import numpy as np
import pandas as pd

# 行列调整
df = pd.DataFrame({
    "A": [5, 3, 4],
    "B": [2, None, 6],
    "C": [9, 2, None],
    "D": [4, 8, 3]
})

# 列的选择，多个列的要用列表
print(df[['A', 'C']])

# 某己列
print(df.iloc[:, [0, 3]])  # : 表示所有行，获取第一列和第四列
print('----------------------')
# 行选择
print(df.loc[[0, 2]])  # 选择第一行和第三行
print(df.loc[0:2])  # 选择第一行到第三行

# 比较
print(df[(df['A'] < 5) & (df['C'] < 4)])  # A列小于5 并且 C小于4, 括号的优先级大于&
print('----------------------')

# 数值替换
# 一对一替换
print(df['C'].replace(2, 3))


print(df.replace(np.nan, 0))

# 多对一替换
df.replace([4, 5, 8], 1000)
# 多对多替换
df.replace({4: 400, 5: 500, 8: 800})
# 排序
# 按照指定列降序排列
df.sort_values(by=['A'], ascending=False)
# 多列排序
df.sort_values(by=['A', 'C'], ascending=[True, False])
# 删除
# 删除列
df.drop('A', axis=1)
# 删除行
df.drop(3, axis=0)
# 删除特定行
df[df['A'] < 4]
# 行列互换
df.T
# 索引重塑
df4 = pd.DataFrame([
    ['a', 'b', 'c'],
    ['d', 'e', 'f']
],
    columns=['one', 'two', 'three'],
    index=['first', 'second']
)
df4.stack()
df4.unstack()
df4.stack().reset_index()
```

#### 基本操作  

示例：
```python
import pandas as pd
df = pd.DataFrame({"A":[5,3,None,4], 
                 "B":[None,2,4,3], 
                 "C":[4,3,8,5], 
                 "D":[5,4,2,None]}) 
# 算数运算
# 两列之间的加减乘除
df['A'] + df['C'] 

# 任意一列加/减一个常数值，这一列中的所有值都加/减这个常数值
df['A'] + 5

# 比较运算
df['A'] > df ['C']  

# count非空值计数
df.count()

# 非空值每列求和
df.sum()
df['A'].sum()

# mean求均值
# max求最大值
# min求最小值
# median求中位数  
# mode求众数
# var求方差
# std求标准差
```

#### 分组聚合  
```python
import pandas as pd
import numpy as np

# 聚合
sales = [{'account': 'Jones LLC','type':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co','type':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc','type':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]

df2 = pd.DataFrame(sales)
df2.groupby('type').groups

for a, b in df2.groupby('type'):
    print(a)
    print(b)

# 聚合后再计算
df2.groupby('type').count()
# df2.groupby('Jan').sum()


# 各类型产品的销售数量和销售总额
df2.groupby('type').aggregate( {'type':'count' , 'Feb':'sum' })


group=['x','y','z']
data=pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    "age":np.random.randint(15,50,10)
    })


data.groupby('group').agg('mean')
data.groupby('group').mean().to_dict()
data.groupby('group').transform('mean')

# 数据透视表
pd.pivot_table(data, 
               values='salary', 
               columns='group', 
               index='age', 
               aggfunc='count', 
               margins=True  
            ).reset_index()
```
#### 多表拼接  
```python
import pandas as pd
import numpy as np

group = ['x','y','z']
data1 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10)
    })

data2 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    })

data3 = pd.DataFrame({
    "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10),
    "salary":np.random.randint(5,50,10),
    })

# 一对一
pd.merge(data1, data2)

# 多对一
pd.merge(data3, data2, on='group')

# 多对多
pd.merge(data3, data2)

# 连接键类型，解决没有公共列问题
pd.merge(data3, data2, left_on= 'age', right_on='salary')

# 连接方式
# 内连接，不指明连接方式，默认都是内连接
pd.merge(data3, data2, on= 'group', how='inner')
# 左连接 left
# 右连接 right
# 外连接 outer

# 纵向拼接
pd.concat([data1, data2])
```
#### 输出和绘图  
输出到文件：
```python
# 导出为.xlsx文件
df.to_excel( excel_writer = r'file.xlsx')

# 设置Sheet名称
df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1')

# 设置索引,设置参数index=False就可以在导出时把这种索引去掉
df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1', index = False)

# 设置要导出的列
df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1', 
             index = False, columns = ['col1','col2'])

# 设置编码格式
enconding = 'utf-8'

# 缺失值处理
na_rep = 0 # 缺失值填充为0

# 无穷值处理
inf_rep = 0

# 导出为.csv文件
to_csv()

# 性能
df.to_pickle('xx.pkl') 

agg(sum) # 快
agg(lambda x: x.sum()) # 慢
```

绘图：
```python
import pandas as pd
import numpy as np

dates = pd.date_range('20200101', periods=12)
df = pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))
df

#                    A         B         C         D
# 2020-01-01  0.046485 -0.556209  1.062881 -1.174129
# 2020-01-02  1.066051 -0.343081  1.054913  1.601051
# 2020-01-03  0.191064 -0.386905  0.516403  0.259818
# 2020-01-04 -0.168462 -1.488041 -0.457658  0.913574
# 2020-01-05 -0.502614  1.235633 -0.578284 -0.362737
# 2020-01-06 -0.193310  0.652285 -0.346359  0.347364
# 2020-01-07  2.308562 -0.679108  0.856449  0.490840
# 2020-01-08  0.871489  0.338133 -0.163669  0.300147
# 2020-01-09 -1.245250  0.667357 -1.287782  1.494880
# 2020-01-10  0.387925 -1.058867 -0.397298  0.514921
# 2020-01-11 -0.440884  0.904307  1.338720  0.612919
# 2020-01-12 -0.864941 -0.358934 -0.203868 -1.191186

import matplotlib.pyplot as plt
plt.plot(df.index, df['A'], )
plt.show()

plt.plot(df.index, df['A'], 
        color='#FFAA00',    # 颜色
        linestyle='--',     # 线条样式
        linewidth=3,        # 线条宽度
        marker='D')         # 点标记

plt.show()

# seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使绘图更容易、更美观
import seaborn as sns
# 绘制散点图
plt.scatter(df.index, df['A'])
plt.show()

# 美化plt
sns.set_style('darkgrid')
plt.scatter(df.index, df['A'])
plt.show()
```
#### 分词与提取关键词  


[结巴文档](https://github.com/fxsjy/jieba)

模式：
```python
import jieba
strings = ['我来自极客大学', 'Python进阶训练营真好玩']

for string in strings:
    result = jieba.cut(string, cut_all=False) # 精确模式
    print('Default Mode: ' + '/'.join(list(result)))

for string in strings:
    result = jieba.cut(string, cut_all=True) # 全模式
    print('Full Mode: ' + '/'.join(list(result)))

result = jieba.cut('钟南山院士接受采访新冠不会二次暴发') # 默认是精确模式
print('/'.join(list(result)))
# "新冠" 没有在词典中，但是被Viterbi算法识别出来了

result = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造') # 搜索引擎模式
print('Search Mode: ' + '/'.join(list(result)))
```
关键字： 
```python
import jieba.analyse
text = '机器学习，需要一定的数学基础，需要掌握的数学基础知识特别多，如果从头到尾开始学，估计大部分人来不及，我建议先学习最基础的数学知识'
# 基于TF-IDF算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(text,
topK=5,                   # 权重最大的topK个关键词
withWeight=True)         # 返回每个关键字的权重值
# 基于TextRank算法进行关键词抽取
textrank = jieba.analyse.textrank(text,
topK=5,                   # 权重最大的topK个关键词
withWeight=False)         # 返回每个关键字的权重值

import pprint             # pprint 模块提供了打印出任何Python数据结构的类和方法
pprint.pprint(tfidf)
pprint.pprint(textrank)
```

```python
import jieba
import jieba.analyse
text = '机器学习，需要一定的数学基础，需要掌握的数学基础知识特别多，如果从头到尾开始学，估计大部分人来不及，我建议先学习最基础的数学知识'
stop_words=r'2jieba/extra_dict/stop_words.txt'
# stop_words 的文件格式是文本文件，每行一个词语
jieba.analyse.set_stop_words(stop_words)

textrank = jieba.analyse.textrank(text,
topK=5,                   
withWeight=False)         

import pprint             # pprint 模块提供了打印出任何Python数据结构的类和方法
pprint.pprint(textrank)
```

```phthon
import jieba
string = '极客大学Python进阶训练营真好玩'
user_dict=r'2jieba/extra_dict/user_dict.txt'

# 自定义词典
jieba.load_userdict(user_dict)

result = jieba.cut(string, cut_all=False)
print('自定义: ' + '/'.join(list(result)))

print('=' * 40 )

# 动态添加词典
jieba.add_word('极客大学')

# 动态删除词典
jieba.del_word('自定义词')

result = jieba.cut(string, cut_all=False)
print('动态添加: ' + '/'.join(list(result)))

print('=' * 40 )

string2 = '我们中出了一个叛徒'
result = jieba.cut(string2, cut_all=False)
print('错误分词: ' + '/'.join(list(result)))

print('=' * 40 )
# 关闭自动计算词频
result = jieba.cut(string2, HMM=False)
print('关闭词频: ' + '/'.join(list(result)))


print('=' * 40 )
# 调整分词，合并
jieba.suggest_freq('中出', True)

result = jieba.cut(string2, HMM=False)
print('分词合并: ' + '/'.join(list(result)))

print('=' * 40 )
# 调整词频，分开分词
string3 = '如果放到Post中将出错'
jieba.suggest_freq(('中','将'), True)
result = jieba.cut(string3, HMM=False)
print('分开分词: ' + '/'.join(list(result)))


# 词性表

# 1. 名词 (1个一类，7个二类，5个三类)
# 名词分为以下子类：
# n 名词
# nr 人名
# nr1 汉语姓氏
# nr2 汉语名字
# nrj 日语人名
# nrf 音译人名
# ns 地名
# nsf 音译地名
# nt 机构团体名
# nz 其它专名
# nl 名词性惯用语
# ng 名词性语素
# 2. 时间词(1个一类，1个二类)
# t 时间词
# tg 时间词性语素
# 3. 处所词(1个一类)
# s 处所词
# 4. 方位词(1个一类)
# f 方位词
# 5. 动词(1个一类，9个二类)
# v 动词
# vd 副动词
# vn 名动词
# vshi 动词“是”
# vyou 动词“有”
# vf 趋向动词
# vx 形式动词
# vi 不及物动词（内动词）
# vl 动词性惯用语
# vg 动词性语素
# 6. 形容词(1个一类，4个二类)
# a 形容词
# ad 副形词
# an 名形词
# ag 形容词性语素
# al 形容词性惯用语
# 7. 区别词(1个一类，2个二类)
# b 区别词
# bl 区别词性惯用语
# 8. 状态词(1个一类)
# z 状态词
# 9. 代词(1个一类，4个二类，6个三类)
# r 代词
# rr 人称代词
# rz 指示代词
# rzt 时间指示代词
# rzs 处所指示代词
# rzv 谓词性指示代词
# ry 疑问代词
# ryt 时间疑问代词
# rys 处所疑问代词
# ryv 谓词性疑问代词
# rg 代词性语素
# 10. 数词(1个一类，1个二类)
# m 数词
# mq 数量词
# 11. 量词(1个一类，2个二类)
# q 量词
# qv 动量词
# qt 时量词
# 12. 副词(1个一类)
# d 副词
# 13. 介词(1个一类，2个二类)
# p 介词
# pba 介词“把”
# pbei 介词“被”
# 14. 连词(1个一类，1个二类)
# c 连词
# cc 并列连词
# 15. 助词(1个一类，15个二类)
# u 助词
# uzhe 着
# ule 了 喽
# uguo 过
# ude1 的 底
# ude2 地
# ude3 得
# usuo 所
# udeng 等 等等 云云
# uyy 一样 一般 似的 般
# udh 的话
# uls 来讲 来说 而言 说来
# uzhi 之
# ulian 连 （“连小学生都会”）
# 16. 叹词(1个一类)
# e 叹词
# 17. 语气词(1个一类)
# y 语气词(delete yg)
# 18. 拟声词(1个一类)
# o 拟声词
# 19. 前缀(1个一类)
# h 前缀
# 20. 后缀(1个一类)
# k 后缀
# 21. 字符串(1个一类，2个二类)
# x 字符串
# xx 非语素字
# xu 网址URL
# 22. 标点符号(1个一类，16个二类)
# w 标点符号
# wkz 左括号，全角：（ 〔 ［ ｛ 《 【 〖 〈 半角：( [ { <
# wky 右括号，全角：） 〕 ］ ｝ 》 】 〗 〉 半角： ) ] { >
# wyz 左引号，全角：“ ‘ 『
# wyy 右引号，全角：” ’ 』
# wj 句号，全角：。
# ww 问号，全角：？ 半角：?
# wt 叹号，全角：！ 半角：!
# wd 逗号，全角：， 半角：,
# wf 分号，全角：； 半角： ;
# wn 顿号，全角：、
# wm 冒号，全角：： 半角： :
# ws 省略号，全角：…… …
# wp 破折号，全角：—— －－ ——－ 半角：--- ----
# wb 百分号千分号，全角：％ ‰ 半角：%
# wh 单位符号，全角：￥ ＄ ￡ ° ℃ 半角：$
```
#### 情感倾向分析   
```python
from snownlp import SnowNLP
text = '其实故事本来真的只值三星当初的中篇就足够了但是啊看到最后我又一次被东野叔的反战思想打动了所以就加多一星吧'
s = SnowNLP(text)

# 1 中文分词
s.words

# 2 词性标注 (隐马尔可夫模型)
list(s.tags)

# 3 情感分析（朴素贝叶斯分类器）
s.sentiments
text2 = '这本书烂透了'
s2 = SnowNLP(text2)
s2.sentiments

# 4 拼音（Trie树）
s.pinyin

# 5 繁体转简体
text3 = '後面這些是繁體字'
s3 = SnowNLP(text3)
s3.han

# 6 提取关键字
s.keywords(limit=5)

# 7 信息衡量
s.tf # 词频越大越重要
s.idf # 包含此条的文档越少，n越小，idf越大，说明词条t越重要

# 8 训练
from snownlp import seg
seg.train('data.txt')
seg.save('seg.marshal')
# 修改snownlp/seg/__init__.py的 data_path 指向新的模型即可
```

```python

import pandas as pd
from snownlp import SnowNLP

# 加载爬虫的原始评论数据
df = pd.read_csv('book_utf8.csv')
# 调整格式
df.columns = ['star', 'vote', 'shorts']
star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}
df['new_star'] = df['star'].map(star_to_number)
# 用第一个评论做测试
first_line = df[df['new_star'] == 3].iloc[0]
text = first_line['shorts']
s = SnowNLP(text)
print(f'情感倾向: {s.sentiments} , 文本内容: {text}')

# 封装一个情感分析的函数
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

df["sentiment"] = df.shorts.apply(_sentiment)
# 查看结果
df.head()
# 分析平均值
df.sentiment.mean() 


# 训练模型
# from snownlp import sentiment
# sentiment.train('neg.txt','pos.txt')
# sentiment.save('sentiment.marshal')

del df['star']
del df['vote']
order = ['new_star', 'shorts', 'sentiment']
df = df[order]
df.rename(columns={'new_star':'n_star','shorts':'short'},inplace=True) 
df.to_csv('result.csv', index=None)
```

```python
import numpy as np

# 标量
a = 1
print(a)

# 向量
v1 = np.array([1, 3])
print(v1)
print(v1.shape)

# 矩阵
m1 = np.array([[1, 0], [0, 1]])
print(m1)
print(m1.shape)

# 向量减法
v1 = np.array([1, 0])
v2 = np.array([0, 1])
print(v1 + v2)
v3 = np.array([1, 1])
print(v3 - v1)

# 曼哈顿距离
v1 = np.array([1, 1])
v2 = np.array([2, 2])
from numpy import linalg
print(linalg.norm(v2 - v1, 1))

# 欧几里得距离
print(linalg.norm(v2 - v1, 2))

# 矩阵
m1 = np.array([[1, 2], [2, 3]])
print(m1)
print(m1.shape)

# 矩阵与标量运算
print(m1 + 1)

# 向量的维度(2维)
print(v2.shape)

# 向量的维度(3维)
v3 = np.array([1, 1, 1])
print(v3.shape)

# 矩阵相加
m1 = np.array([[1, 0], [0, 1]])
m2 = np.array([[1, 1], [1, 1]])
print(m1.shape, m2.shape)
print(m1 + m2)

# 矩阵形状不一致会报错
m3 = np.array([[1,], [0,]])
m4 = np.array([[1,], [1,], [2,]])
print(m3.shape, m4.shape)
print(m3 + m4)
```
```python
import torch
import torchtext
from torchtext import vocab
# 预先训练好的词向量
gv = torchtext.vocab.GloVe(name='6B', dim=50)
# 40万个词，50个维度
len(gv.vectors), gv.vectors.shape
# 获得单词的在Glove词向量中的索引(坐标)
gv.stoi['tokyo']
# 查看tokyo的词向量
gv.vectors[1363]
# 可以把坐标映射回单词
gv.itos[1363]

# 把tokyo转换成词向量
def get_wv(word):
    return gv.vectors[gv.stoi[word]]
get_wv('tokyo')

# 找到距离最近的10个单词
def sim_10(word, n=10):
    all_dists = [(gv.itos[i], torch.dist(word, w)) for i, w in enumerate(gv.vectors)]
    return sorted(all_dists, key=lambda t: t[1])[:n]
sim_10(get_wv('tokyo'))

def analogy(w1, w2, w3, n=5, filter_given=True):
    print(f'[ {w1} : {w2} :: {w3} : ? ]')
    
    # w2 - w1 + w3 = w4
    closest_words = sim_10(get_wv(w2) - get_wv(w1) + get_wv(w3))

    # 过滤防止输入参数出现在结果中
    if filter_given:
        closest_words = [t for t in closest_words if t[0] not in [w1, w2, w3]]
    print(closest_words[:2])

analogy('beijing', 'china', 'tokyo')
# [ beijing : china :: tokyo : ? ]
# [('japan', tensor(2.7869)), ('japanese', tensor(3.6377))]
```