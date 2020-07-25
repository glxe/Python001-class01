import pandas as pd
import numpy as np
import matplotlib as plt
import os
import csv
import time
# import pymysql
# conn = mysql.connector.connect(
# user='root',
# password='dqueqqsv',
# host='118.24.249.42',
# port='3306',
# database='test'
# )
import pymysql



db = pymysql.connect(
    '118.24.249.42',
    'root',
    'dqueqqsv',
    'test'
)

cursor = db.cursor()

pwd = os.path.dirname(os.path.realpath(__file__))

file = os.path.join(pwd, 'data.csv')


localtime = time.strftime("%Y-%m-%d %H:%M:%S" ,  time.localtime() )

with open(file, 'r') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i += 1
        if row:
            group_id = i / 5

            sql = "INSERT INTO `documents` (`group_id`, `date_added`, `title`, `content`) VALUES (%s, %s, %s, %s)"

            try:
                # 执行sql语句
                cursor.execute(sql, (group_id, localtime, row[2], row[2]))
            except Exception as e:
                print(e)
            # print(row[2])

# print(df)
db.commit()

db.close()