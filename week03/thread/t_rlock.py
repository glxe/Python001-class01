import threading
import os
import time
# 普通锁不可嵌套，RLock普通锁可嵌套
num = 0
mutex = threading.RLock() # 普通嵌套

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if mutex.acquire(1): # 加锁
            print(f'thread {self.name}, get mutex')
            mutex.acquire()
            num += 1
            print(f'{self.name}: num value is {num}')
            mutex.release()
        mutex.release() # 解锁

if __name__ == '__main__':
    for i in range(20):
        t = MyThread()
        t.start()

# thread Thread-1, get mutex
# Thread-1: num value is 1
# thread Thread-5, get mutex
# Thread-5: num value is 2
# thread Thread-4, get mutex
# Thread-4: num value is 3
# thread Thread-2, get mutex
# Thread-2: num value is 4
# thread Thread-3, get mutex
# Thread-3: num value is 5
# thread Thread-9, get mutex
# Thread-9: num value is 6
# thread Thread-7, get mutex
# Thread-7: num value is 7
# thread Thread-11, get mutex
# Thread-11: num value is 8
# thread Thread-13, get mutex
# Thread-13: num value is 9
# thread Thread-15, get mutex
# Thread-15: num value is 10
# thread Thread-16, get mutex
# Thread-16: num value is 11
# thread Thread-6, get mutex
# Thread-6: num value is 12
# thread Thread-10, get mutex
# Thread-10: num value is 13
# thread Thread-12, get mutex
# Thread-12: num value is 14
# thread Thread-18, get mutex
# Thread-18: num value is 15
# thread Thread-14, get mutex
# Thread-14: num value is 16
# thread Thread-17, get mutex
# Thread-17: num value is 17
# thread Thread-8, get mutex
# Thread-8: num value is 18
# thread Thread-19, get mutex
# Thread-19: num value is 19
# thread Thread-20, get mutex
# Thread-20: num value is 20