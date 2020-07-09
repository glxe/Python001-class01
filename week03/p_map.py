from multiprocessing import Pool
import time
import os


def f(x):
    return x*x

if __name__ == '__main__':
    count = os.cpu_count()
    with Pool(processes=count) as pool: # 进程包含cpu逻辑数量
        print(pool.map(f, range(10)))

        p = pool.imap(f, range(10)) # map 输出列表，imap输出迭代器
        print((p,))
        print(next(p))
        print(next(p))

        print(p.next(timeout=1))
