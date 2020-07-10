#信号量：内部实现一个计数器，占用信号量的线程数超过指定数值是阻塞 


import threading
import os
import time


def run(n):
    semaphore.acquire()
    print('run the thread: %s' % n)
    time.sleep(1)
    semaphore.release()




if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(5) # 最多允许5个线程同时运行
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        t.start()



# run the thread: 0
# run the thread: 1
# run the thread: 2
# run the thread: 3
# run the thread: 4
# run the thread: 6
# run the thread: 7
# run the thread: 9
# run the thread: 5
# run the thread: 8