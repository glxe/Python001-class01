# # 全局变量在多个进程中不能共享，在子进程中修改全局变量对父进程中的全局变量没有影响
# # 因为父进程在创建子进程时对全局变量做了一个备份，
# # 在子进程中的全局变量与子进程的全局变量完全是不同的两个变量
# # 全局变量在多个进程中是不能被共享的。

# import time
# import os
# from multiprocessing import Process

# num = 1000

# def run():
#     print(f'我是子进程，PID：{os.getpid()}')
#     global num
#     num += 1
#     print(f'子进程num = {num}')
#     print('子进程end')



# if __name__ == '__main__':
#     print(f'我是父进程，PID：{os.getpid()}')
#     num += 2
#     p = Process(target=run)
#     p.start()
#     p.join()
#     # 在子进程中修改全局变量num，父进程没有任何变化
#     print(f'父进程结束，num = {num}')


# # 我是父进程，PID：78309
# # 我是子进程，PID：78310
# # 子进程num = 1001
# # 子进程end
# # 父进程结束，num = 1000


import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(4)
    r = s.connect(('80.101.49.5', 899))
    print(r)