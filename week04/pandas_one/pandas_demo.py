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


