#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys, getopt, socket
import re
import struct




def params(argv):
    ip = '' # ip地址
    port = 80 # 端口号
    way = '' # 扫描方式
    num = 0 # 并发数量
    result = 'result.json' # 扫描结果的保存文件
    v = '' # 运行时间
    m = 'thread' # 使用多线程方式扫描，或者多进程方式扫描
    try:
        options, args = getopt.getopt(argv,"hn:i:p:f:v:w:m:",["help", "num=","ip=", "port=", "way=", "v=", "result=", "m="])
    except getopt.GetoptError:
        print('pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100 or pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json')
        sys.exit(2)

    for option, value in options:
        if option in ("-h", "--help"):
            print('pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100 or pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json')
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


def check_ip(host):
    print(f'ip: {host}')
    result = host
    return result


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

if __name__ == "__main__":
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
    strat_ip_int = ip2int(ip.split('-')[0])
    end_ip_int = ip2int(ip.split('-')[1])
    if (end_ip_int < strat_ip_int):
        print('Invalid IP range!')
        sys.exit()
    ip_range_max = end_ip_int - strat_ip_int
    for i in range(0, ip_range_max + 1 ):
        host = int2ip(strat_ip_int + i)
        print(check_ip(host))

    print(strat_ip_int)
    print(end_ip_int)

    print(end_ip_int - strat_ip_int)

    print(f"ip: {ip}, port: {port}, way: {way}, num: {num}, result: {result}, v: {v}, m: {m}")

