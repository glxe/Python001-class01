# multiprocessing.Process的run()方法

import os
import time
from multiprocessing import Process

class NewProcess(Process): # 继承Process类，创建一个新类
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self): # 重新Process类中的run方法
        while True:
            print(f'我是进程：{self.num}，我的pid：{os.getpid()}')
            time.sleep(1)


for i in range(16):
    p = NewProcess(i)
    p.start()

# 当不给NewProcess指定target时，会默认执行Process类里的run方法，这和指定target效果是一样的，只是将函数封装到类中之后便于理解和调用