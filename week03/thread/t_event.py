# 事件：定义一个flag，set设置flag为True，clear设置flag为False

import threading
import os
import time


def func(e, i):
    print(i)
    e.wait() # 检测当前event是什么状态，如果是红灯则阻塞，如果是绿灯则继续往下执行，默认是红灯
    print(i+100)

event = threading.Event()

for i in range(10):
    t = threading.Thread(target=func, args=(event, i))
    t.start()


event.clear() # 主动将flag设置为红灯
inp = input('>>>')

if inp == '1':
    event.set() # 主动将flag设置为绿灯


# 使用redis实现分布式锁？


# 定时器：指定n秒后执行
from threading import Timer

def hello():
    print('hello world')

t = Timer(1, hello) # 应该跟JavaScript里的settimeout一样的
t.start()