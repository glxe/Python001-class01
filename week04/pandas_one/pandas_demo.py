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

