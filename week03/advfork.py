import time
import os
from multiprocessing import Process

def run():
    print(f'子进程开启，pid: {os.getpid()}')
    print(f'子进程开启，ppid: {os.getppid()}')

    time.sleep(2)
    print('子进程结束')


if __name__ == '__main__':
    print(f'父进程启动，pid: {os.getpid()}')
    print(f'父进程启动，ppid: {os.getppid()}')

    p = Process(target=run)
    p.start()
    p.join()
    print('父进程结束')

# 父进程启动，pid: 75228
# 子进程开启，pid: 75229
# 子进程结束
# 父进程结束