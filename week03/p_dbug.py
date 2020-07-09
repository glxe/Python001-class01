# 显示所涉及的各个进程ID，这是有一个扩展示例

from multiprocessing import Process
import os
import multiprocessing

def debug_info(title):
    print('-'*20)
    print(title)
    print('模块名称', __name__)
    print('父进程：', os.getppid())
    print('子进程：', os.getpid())
    print('-'*20)

def f(name):
    debug_info('function f')
    print('hello', name)



if __name__ == '__main__':
    debug_info('main')
    p = Process(target=f, args=('bob',))
    p.start()

    for p in multiprocessing.active_children():
        print(f'子进程：{p.name} id:{str(p.pid)}')

    print('进程结束')
    print(f'CPU核心数量:{str(multiprocessing.cpu_count())}')

    p.join()



# --------------------
# main
# 模块名称 __main__
# 父进程： 74957
# 子进程： 75744
# --------------------
# 子进程：Process-1 id:75745
# 进程结束
# CPU核心数量:8
# --------------------
# function f
# 模块名称 __main__
# 父进程： 75744
# 子进程： 75745
# --------------------
# hello bob
# 在程序运行时，每一个进程将会占用一个cpu核心的
# 一般创建子进程的数量和cpu核心数量相等的时候，效率相对较高