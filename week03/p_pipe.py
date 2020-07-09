# 管道
# 官方文档
# Pipe() 函数返回一个由管道链接的连接对象，默认情况下是双工的（双向）

from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    p = Process(target=f, args=(child_conn,))
    p.start()

    print(parent_conn.recv())  # prints [42, None, 'hello']
    p.join()


# 返回的两个连接对象是Pipe() 表示管道的两端
# 每个连接对象都有send和recv方法（相互之间）
# 请注意，如果两个进程或两个线程同时尝试读取或写入管道的同一端，则管道中的数据可能会损坏



# 传统的方式的变量是写在自己进程的内存中的，