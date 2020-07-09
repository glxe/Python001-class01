# join dead lock 死锁

from multiprocessing import Process, Queue
import time
import os


def f(x):
    return x*x

if __name__ == '__main__':
   queue = Queue()

   p = Process(target=f, args=(queue,))
   p.start()
   p.join()   # this deadlocks
   obj = queue.get()

# 交换最后两行可以修复这个问题，（或者直接删掉 p.join(), 这样程序就能自己执行完成自动结束掉）