import threading
import os
import time

num = 0
mutex = threading.Lock() # 普通锁

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if mutex.acquire(1): # 加锁
            num += 1
            print(f'{self.name}: num value is {num}')
        mutex.release() # 解锁

if __name__ == '__main__':
    for i in range(20):
        t = MyThread()
        t.start()


# Thread-2: num value is 1
# Thread-17: num value is 2
# Thread-8: num value is 3
# Thread-7: num value is 4
# Thread-12: num value is 5
# Thread-13: num value is 6
# Thread-16: num value is 7
# Thread-18: num value is 8
# Thread-1: num value is 9
# Thread-3: num value is 10
# Thread-15: num value is 11
# Thread-14: num value is 12
# Thread-19: num value is 13
# Thread-20: num value is 14
# Thread-6: num value is 15
# Thread-4: num value is 16
# Thread-5: num value is 17
# Thread-11: num value is 18
# Thread-9: num value is 19
# Thread-10: num value is 20