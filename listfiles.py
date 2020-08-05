import os

import time


def walk(pwd, i):
    for d in os.listdir(pwd):
        filename = pwd + '/' + d
        mtime = time.localtime(os.path.getmtime(filename))
        ctime = time.localtime(os.path.getctime(filename))
        if os.path.isfile(filename):
            print(f"{filename} is file, modify time: {time.strftime('%Y-%m-%d %H:%M:%S', mtime)}, create time: {time.strftime('%Y-%m-%d %H:%M:%S', ctime)}")
        else:
            e = ''
            for _ in range(0, i):
                e = e + '-'
            i += 1
            walk(filename, i)
            print(f"{e}{filename} is dir, modify time: {os.path.getmtime(filename)}, create time: {os.path.getctime(filename)}")


if __name__ == '__main__':
    i = 0
    current = os.getcwd()
    walk(current, i)