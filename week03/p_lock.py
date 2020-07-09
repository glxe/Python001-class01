# 进程锁Lock
# 不加锁

import multiprocessing as mp

import time

# 在这里设置进程锁的使用，保证在一个进程在运行时对锁内内容的独占
def job(v, num, l, p):
    l.acquire() #  锁住
    for _ in range(5):
        time.sleep(0.1) # 暂停0.1秒让输出效果更明显
        v.value += num # v.value获取共享变量值
        print(f'{p}-value = {v.value}')
    l.release()


if __name__ == '__main__':
    v = mp.Value('i', 0) # 定义共享变量 
    l = mp.Lock() # 定义一个进程锁
    # 进程锁传入各个进程中
    p1 = mp.Process(target=job, args=(v, 1, l, 'p1'))
    p2 = mp.Process(target=job, args=(v, 3, l, 'p2')) # 设定不同number，看看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()

# p1-value = 1
# p1-value = 2
# p1-value = 3
# p1-value = 4
# p1-value = 5
# p2-value = 8
# p2-value = 11
# p2-value = 14
# p2-value = 17
# p2-value = 20

# 上面的结果就是进程锁保证进程p1的完整运行，然后才进行了p2进程的运行



# 在某些特定的场景下要共享string类型，方式如下：
from ctypes import c_char_p
str_val = mp.Value(c_char_p, b"Hello World")