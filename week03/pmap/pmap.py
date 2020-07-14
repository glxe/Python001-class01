#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, getopt, socket, queue
import re
import struct
import ping
import threading





def params(argv):
    ip = '' # ip地址
    port = 80 # 端口号
    way = '' # 扫描方式
    num = 1 # 并发数量
    result = 'result.json' # 扫描结果的保存文件
    v = '' # 运行时间
    m = 'thread' # 使用多线程方式扫描，或者多进程方式扫描
    try:
        options, args = getopt.getopt(argv,"hn:i:p:f:v:w:m:",["help", "num=","ip=", "port=", "way=", "v=", "result=", "m="])
    except getopt.GetoptError:
        print('pmap.py -n 4 -f ping -i 192.168.0.1-192.168.0.100 or pmap.py -n 10 -f tcp -i 192.168.0.1 -w result.json')
        sys.exit(2)

    for option, value in options:
        if option in ("-h", "--help"):
            print('pmap.py -n 4 -f ping -i 192.168.0.1-192.168.0.100 or pmap.py -n 10 -f tcp -i 192.168.0.1 -w result.json')
        if option in ("-n", "--num"):
            num = value
        if option in ("-i", "--ip"):
            ip = value
        if option in ("-p", "--port"):
            port = value
        if option in ("-f", "--way"):
            way = value
        if option in ("-v", "--v"):
            v = value
        if option in ("-w", "--result"):
            result = value
        if option in ("-m", "--m"):
            m = value
    return ip, port, way, num, result, v, m


def scan_ip(ip, port):
    try:
        print(f'ip: {ip}:{port}')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(5)
        result = s.connect_ex((ip, port))
        return result == 0
    except:
        # 记录错误
        return False


def ip2int(ip):
    return struct.unpack("!I",socket.inet_aton(ip))[0]


def int2ip(i):
    return socket.inet_ntoa(struct.pack("!I",i))






class CheckIpThread(threading.Thread):
    def __init__(self, start_ip, end_ip, queue):
        super().__init__()
        self.start_ip = start_ip
        self.end_id = end_ip
        self.queue = queue
        self.active_total = 0
    
    def run(self):
        print('check ip start...')
        strat_ip_int = ip2int(self.start_ip)
        end_ip_int = ip2int(self.end_id)
        if (end_ip_int < strat_ip_int):
            raise Exception('Invalid IP range! end need gt start')
        ip_range_max = end_ip_int - strat_ip_int
        for i in range(0, ip_range_max + 1 ):
            host = int2ip(strat_ip_int + i)
            print(f'ip: {host}')
            if self.check_ip(host):
                if not self.queue.full():
                    self.queue.put(host)
                    self.active_total += 1
                    print(f'ip: {host} is active')
                else:
                    pass

        print('check ip end.')
        
    def check_ip(self, host):
        result, _ = ping.ping(host, 1)
        return result


class ScanIpThread(threading.Thread):
    def __init__(self, queue, num):
        super().__init__()
        self.queue = queue
        self.num = num

    def run(self):
        print(f'scan thread {self.num} ip start...')
        while True:
            try:
                if not self.queue.empty():
                    data = self.queue.get()
                    if data == 'check_is_done':
                        q.put('check_is_done') # 告诉其他线程，检查ip线程已经结束
                        break
                    print(f'scan active ip from queue: {data}, by thread {self.num}')
                    self.scan_port(data)
                    self.queue.task_done()
            except Exception as e:
                print(e)
                pass
        print(f'scan ip end. thread {num}')

    def scan_port(self, ip):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(4)
                for port in range(1, 1025):
                    result_code = s.connect_ex((ip, port)) #开放放回0
                    print(f'ip: {ip}, port: {port}, result code: {result_code}. by thread {self.num}')
                    if (result_code == 0):
                        print(f'is openning. by thread {self.num}')
        except Exception as e:
            print(e)
        
if __name__ == "__main__":

    hostname=socket.gethostname()
    # 获取本机IP
    ip=socket.gethostbyname(hostname)
    print(f'hostname: {hostname}, ip: {ip}')
    '''
    ip: 192.168.0.1 [-192.168.0.100]
    prot: 80 [1-1024]
    way: ping [tcp]
    num: 并发数量
    result: 存储结果的文件
    v: 显示运行时间
    m: 使用什么方式
    '''
    ip, port, way, num, result, v, m = params(sys.argv[1:])

    if not re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)-(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        print('Invalid IP address!')
        sys.exit()
    # strat_ip_int = ip2int(ip.split('-')[0])
    # end_ip_int = ip2int(ip.split('-')[1])
    # if (end_ip_int < strat_ip_int):
    #     print('Invalid IP range!')
    #     sys.exit()
    # ip_range_max = end_ip_int - strat_ip_int


  # 任务队列，存放网页的队列
    q = queue.Queue(200)
    check = CheckIpThread(ip.split('-')[0], ip.split('-')[1], q)
    check.start()
    num = int(num)
    scan_threads = []
    # 将并发数量限制在 1和逻辑cpu数量一致
    max_threads = os.cpu_count()
    print(max_threads)
    if int(num) > int(max_threads):
        num = int(max_threads)
    elif int(num) < 1:
        num = 1
    for n in range(1, num + 1):
        scan = ScanIpThread(q, n)
        scan.start()
        scan_threads.append(scan)
        # pass
    
    check.join()
    q.put('check_is_done') # 告诉其他线程，检查ip线程已经结束
    # while True:
    #     if (q.empty()):
    #         break;

    #     data = q.get()
    #     print(f'from queue ip: {data}')
    #     q.task_done()


    for scan in scan_threads:
        scan.join()
    print(f"ip: {ip}, port: {port}, way: {way}, num: {num}, result: {result}, v: {v}, m: {m}")

