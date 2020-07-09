import threading
import os
def run(n):
    print('current task', n)
    print(f'pid: {os.getpid()}')


run(1)
run(2)

if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=('thread 1', ))
    t2 = threading.Thread(target=run, args=('thread 2', ))

    t1.start()
    t2.start()


# current task 1
# pid: 85873
# current task 2
# pid: 85873
# current task thread 1
# pid: 85873
# current task thread 2
# pid: 85873

# 调用方
# 阻塞 得到调用结果之前，线程会被挂起
# 非阻塞 不能立即得到结果，不会阻塞线程

# 被调用方
# 同步 得到结果之间，调用不会返回
# 异步 请求发出后，调用立即返回，没有返回结果，通过回调函数得到实际结果