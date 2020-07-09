# 在 进行并发编程时，通常最好尽量避免使用共享状态，
# 共享内存 shared memory可以使用Value Array将数据存储在共享内存映射中
# 这里的 Array和numpy中的不同，它只能是一维，不能是多维的。
# 同样 和 Value 一样，要定义数据类型，否则会报错

from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415926
    for i in a:
        a[i] = -a[i]


if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    p = Process(target=f, args=(num, arr))

    p.start()
    p.join()

    print(num.value)
    print(arr[:])

# 3.1415926
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# 创建 num 和 arr 时使用 ‘d’ 和 ‘i’，参数是array模块使用的类型 ‘typecode’：‘d’表示双精度浮点数，‘i’表示有符号整数
# 这些共享对象将是进程和线程安全的