# only for linux mac

# fork()
import os

# a = os.fork()
# print(a)
# print(11111)

# 执行结果：
# 73866
# 11111
# 0
# 11111
# fork函数一旦运行就会生出一条新的进程，2个进程一起执行导致输出了2行 
# 一个是父进程执行的，一个是子进程执行的



import time
# 区分父子进程
res = os.fork()
print(f'res = {res}')

if res == 0:
    print(f'我是子进程，我的pid是：{os.getpid()}，我的父进程id是：{os.getppid()}')
else:
    print(f'我是父进程，我的pid是：{os.getpid()}')
    
# fork运行时，会有两个返回值，返回值大于0时，此进程为父进程，且返回值的数字为子进程的PID，当返回值为0时，此进程为子进程
# 注意：父进程结束时，子进程并不会随父进程立刻结束。同样，父进程不会等待子进程执行完。
# 注意：os.fork()无法在windows上运行