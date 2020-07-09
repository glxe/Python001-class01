from multiprocessing import Pool
import time
import os


def f(x):
    return x*x

if __name__ == '__main__':
    count = os.cpu_count()
    with Pool(processes=count) as pool: # 进程包含cpu逻辑数量
        result = pool.apply_async(f, args=(10,)) # 执行一个子进程
        print(result.get(timeout=1)) # 显示执行结果

        result = pool.apply_async(time.sleep, args=(10, ))
        print(result.get())