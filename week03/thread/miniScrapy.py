import threading
import queue
import requests
import json
from lxml import etree



class CrawlThread(threading.Thread):
    '''
    爬虫类
    '''
    def __init__(self, thread_id, queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue

    def run(self):
        '''
        重写run方法
        '''
        print(f'启动线程：{self.thread_id}')
        self.scheduler()
        print(f'结束线程：{self.thread_id}')

    def scheduler(self):
        '''
        模拟任务调度
        '''
        while True:
            if self.queue.empty():
                break
            else:
                page = self.queue.get()
                print(f'下载线程为：{self.thread_id}，下载页面：{page}')
                url = f'https://book.douban.com/top250?start={page*25}'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
                }
                try:
                    response = requests.get(url, headers = headers)
                    dataQueue.put(response.text)
                except Exception as e:
                    print('下载异常', e)




class ParserThread(threading.Thread):
    '''
    页面内容分析
    '''
    def __init__(self, thread_id, queue, file):
        super().__init__(self)   # super() == threading.Thread  ????  或者说就是父类
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self):
        print(f'启动线程：{self.thread_id}')
        while not flag:
            try:
                item = self.queue.get(False) # 参数为false时队列为空，抛出异常
                if not item:
                    pass

                self.parse_data(item)
                self.queue.task_one() # get 之后检测是否会阻塞
            except Exception as e:
                pass

        print(f'结束进程：{self.thread_id}')


    def parse_data(self, item):
        print('parse data')




dataQueue = queue.Queue()
flag = ''

if __name__ == '__main__':
    pass