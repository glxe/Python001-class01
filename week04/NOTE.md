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

#### 多表拼接  

#### 输出和绘图  

#### 分词与提取关键词  

#### 情感倾向分析   