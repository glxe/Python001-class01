import threading
import os
import time

def condition():
    ret = False
    r = input('>>>')
    if r == 'yes' or r == 'y':
        ret = True
    return ret


def f(conn, i):
    print(i)
    conn.acquire()
    conn.wait_for(condition) # 这个方法接受一个函数的返回值
    print(i+100)
    conn.release()

c = threading.Condition()
for i in range(5):
    t = threading.Thread(target=f, args=(c, i,))
    t.start()
    t.join()
# 条件锁的原理跟设计模式中的生产者/消费者(Producer/Consumer)模式类似
