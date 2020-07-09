# 进程锁Lock
# 不加锁

import multiprocessing as mp

import time

def job(v, num, p):
    for _ in range(5):
        time.sleep(0.1) # 暂停0.1秒让输出效果更明显
        v.value += num # v.value获取共享变量值
        print(f'{p}-value = {v.value}')


if __name__ == '__main__':
    v = mp.Value('i', 0) # 定义共享变量 
    p1 = mp.Process(target=job, args=(v, 1, 'p1'))
    p2 = mp.Process(target=job, args=(v, 3, 'p2')) # 设定不同number，看看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()


# 在上面的代码中我们定义了一个共享变量v，两个进程都可以对它进行操作，
# 在job中，我们想让V每隔0.1秒输出一次累加num的结果，但是两个进程设置的不同累加值，so 接下来看看这两个进程会不会出现冲突
# 进程1和进程在互相抢着使用共享内存