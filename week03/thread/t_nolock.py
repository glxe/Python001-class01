import threading
import os
import time

num = 0

def addone(i):
    global num
    num += 1
    time.sleep(1) # 必须休眠，否则观察不到脏数据
    print(f'num value is {num}')



for i in range(20):
    t = threading.Thread(target=addone, args=(i,))
    t.start()


# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20
# num value is 20 