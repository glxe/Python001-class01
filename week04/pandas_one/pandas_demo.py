# import pandas as pd
# import numpy as np
# import matplotlib as plt
# import os 


# pwd = os.path.dirname(os.path.realpath(__file__))

# file = os.path.join(pwd, 'data.csv')
# print(file)

# df = pd.read_csv(file)

# print(df)
# # 筛选标题为 还行 这一列
# print(df['还行'])

# import pandas as pd
# import numpy as np

# x = pd.Series([1, 2, 5, np.nan, 78, 5, np.nan])
# print(x)
# # 检验是否存在缺失值
# print(x.hasnans)

# # 将缺失值填充为平均值
# ss = x.fillna(value = x.mean())
# print(ss)



# df = pd.DataFrame({
#     "A": [1,2,3],
#     "B": [89, np.nan, 43],
#     "C": [np.nan, 56, 89],
#     "D": [63, 4, 9]
# })

# print(df.isnull().sum()) # 查看缺失值汇总

# print(df.ffill()) # 用上一行填充
# print(df.ffill(axis=1)) # 用前一列填充

# print(df)

# print(df.info())
# print(df.dropna())

# print(df.fillna('无'))

# print(df.drop_duplicates())

import pandas as pd

# 行列调整
df = pd.DataFrame({
    "A": [5, 3, 4],
    "B": [2, None, 6],
    "C": [9, 2, None],
    "D": [4, 8, 3]
})

# 列的选择，多个列的要用列表
print(df[ ['A', 'C'] ])

# 某己列
print(df.iloc[:, [0, 3]]) # : 表示所有行，获取第一列和第四列
print('----------------------')
# 行选择
print(df.loc[[0, 2]]) # 选择第一行和第三行
print(df.loc[0:2]) # 选择第一行到第三行

# 比较
print(df[(df['A'] < 5) & (df['C'] < 4)]) # A列小于5 并且 C小于4, 括号的优先级大于&
print('----------------------')

# 数值替换
# 一对一替换
print(df['C'].replace(2, 3))

import numpy as np
print(df.replace(np.nan, 0))


