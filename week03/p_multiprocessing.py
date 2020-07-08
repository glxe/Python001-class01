
# 参数
# multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={})

# - group: 分组，实际上很少使用，
# - target: 表示调用对象，你可以传入方法的名字，或者函数名称
# - name: 别名，相当于给这个进程取一个名字
# - args: 表示调用对象的位置参数元祖，比如target是函数a，他有两个参数m，n，那么args就传入（m，n）即可
# - kwargs：表示调用对象的字典

from multiprocessing import Process


def f(name):
    print(f'hello {name}')

if __name__ == '__main__':
    p = Process(target=f, args=('john',))
    p.start()
    p.join() # 等待子进程结束，父进程才能结束

# join(timeout) # 超过多少秒 子进程不结束，则父进程也会立即结束
# 如果可选参数 timeout 是None（默认值），则该方法将阻塞
# 知道调用join() 方法的进程终止。如果timeout是一个正数，它最多会阻塞 timeout 秒。
# 请注意，如果进程终止或方法超时，则该方法返回 None。
# 检查进程的exitcode以确定它是否终止
# 一个进程可以合并多次
# 进程无法并入自身，因为这会导致死锁。
# 尝试在启动进程之前合并进程是错误的