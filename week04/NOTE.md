## 学习笔记 

***
## week four 作业  

* [作业一]()
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



#### 数据导入  



#### 数据预处理  


#### 数据调整  



#### 基本操作  



#### 分组聚合  


#### 多表拼接  


#### 输出和绘图  



#### 分词与提取关键词  


#### 情感倾向分析   