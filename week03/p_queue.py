# multiprocessing 支持进程间的两种通信
# 队列，来自官方文档中的一个简单的demo
# Queue是一个类似queue.Queue的克隆
# 现在有这样的一个需求：我们有两个进程，一个进程负责写（write），一个进程负责读（read）
# 当写的进程写完某部分以后要把数据交给读的进程进行使用
# write将写完数据交给队列，再由队列交给read

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()


# 如果是多个进程在进行写入的话，会进行阻塞状态，是需要一个写入后才会有下一个再继续写入
# 队列是线程和队列安全的
# 先入先出 
# blocked 