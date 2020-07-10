import queue

# q = queue.Queue(5) # 队列的大小
# q.put(111) # 存队列
# q.put(222)
# q.put(333)
# print(q.get()) # 如果这里没有的话将会产生阻塞
# q.put(444)
# print(q.get())
# q.put(555)
# q.put(666)
# print(q.get())
# print(q.get())
# q.task_done() # 每次从queue中get一个数据后，当处理好相关问题，最后调用该方法
# # 以提示q.join() 是否停止阻塞，让线程继续执行或者退出
# print(q.qsize()) # 队列中元素的个数，队列的大侠
# print(q.empty()) # 队列是否为空
# print(q.full()) # 队列是否满了

##################
import threading
import random
import time 

lock = threading.Lock()

class Producer(threading.Thread):
    def __init__(self, q, con, name):
        super(Producer, self).__init__() # ?
        self.q = q
        self.con = con
        self.name = name
        print(f'Producer {self.name} started')

    def run(self):
        while True:
            global lock
            self.con.acquire()
            
            if self.q.full(): # 队列满了
                with lock:
                    print('Queue is full, producer wait.')
                self.con.wait()

            else:
                value = random.randint(0, 10)
                with lock:
                    print(f'{self.name} put value {self.name} {str(value)} in queue')
                self.q.put(f'{self.name} : {str(value)}') # 放入队列
                self.con.notify() # 通知消费者
                time.sleep(1)
        self.con.release()


class Customer(threading.Thread):
    def __init__(self, q, con, name):
        super(Customer, self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print(f'customer {self.name} started')

    def run(self):
        while True:
            global lock
            self.con.acquire()
            if self.q.empty(): # 队列空了
                with lock:
                    print(f'Queue is empty, customer wait.')
                self.con.wait() # 等待资源
            else:
                value = self.q.get()
                with lock:
                    print(f'{self.name} get value {str(value)} from queue')
                self.con.notify()   # 通知生产者
                time.sleep(1)

        self.con.release()


if __name__ == '__main__':
    q = queue.Queue(10)

    con = threading.Condition() # 条件变量锁
    p1 = Producer(q, con, 'p1')
    p2 = Producer(q, con, 'p2')

    p1.start()

    p2.start()

    c1 = Customer(q, con, 'c1')
    c1.start()

