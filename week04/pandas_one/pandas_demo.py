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
