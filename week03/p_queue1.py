
import time
import os
from multiprocessing import Process, Queue


def write(w):
    print(f'write process start... pid: {os.getpid()}')
    for m in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
        w.put(m) # 写入队列
        time.sleep(1)
    print('write process end.')


def read1(r):
    print(f'read process-1 start... pid: {os.getpid()}')
    while True: # 阻塞 等待获取write值
        value = r.get(True)
        print(f'i am 1 value = {value}')

    print('read process-1 end.') # 不会执行，直接被干掉了。
    
def read2(r):
    print(f'read process-2 start... pid: {os.getpid()}')
    while True:
        value = r.get(True)
        print(f'i am 2 value = {value}')


if __name__ == '__main__':
    # 父进程创建队列，并传递给子进程
    print(f'parent process start... pid: {os.getpid()}')
    q = Queue()
    w = Process(target=write, args=(q,))
    r1 = Process(target=read1, args=(q,))
    r2 = Process(target=read2, args=(q,))
    w.start()
    r1.start()
    r2.start()

    w.join()
    # r1 和 r2 进程是一个死循环，无法等待其结束，只能强行结束， 写进程结束了，所有读进程也可以结束
    r1.terminate()
    r2.terminate()

    print('parent process end.')


#     parent process start... pid: 79562
# write process start... pid: 79563
# read process-1 start... pid: 79564
# i am 1 value = A
# read process-2 start... pid: 79565
# i am 1 value = B
# i am 2 value = C
# i am 1 value = D
# i am 2 value = E
# i am 1 value = F
# i am 2 value = G
# i am 1 value = H
# i am 2 value = I
# write process end.
# parent process end.