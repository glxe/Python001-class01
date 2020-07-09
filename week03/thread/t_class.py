import threading
import os


class MyThread(threading.Thread):
    def __init__(self, n): 
        super().__init__() # 重构闰年函数必须要写
        self.n = n

    def run(self):
        print('current task:', self.n)
        print(f'pid: {os.getpid()}')

    
if __name__ == '__main__':
    t1 = MyThread('thread 1')
    t2 = MyThread('thread 2')
    print('t1: ', t1.is_alive())
    t1.start()
    print('t1: ', t1.is_alive())

    t2.start()
    print('t2: ', t2.is_alive())
    print('t2: ', t2.getName())
    


    # 将t1 和 t2 加入到主线程中
    t1.join()
    t2.join()
    print('t2: ', t2.is_alive())



# current task: thread 1
# pid: 86106
# current task: thread 2
# pid: 86106