## 学习笔记(week three) -- Scrapy框架深度解析
***
## week three 作业  

* [作业一]()
* [作业二]()

***

## Scrapy框架深度解析  

### Scrapy 并发参数优化原理  
requests 是同步请求，在请求的时候，在等着一件事做完，再做下一件事。scrapy可以是异步，同时处理多个事情。当然是需要调优的。  
***Scrapy参数调优***  
```python
#setting.py 参数调优  
# Configure maximum concurrent(并发) requests performed by Scrapy(default:16)
CONCURRENT_REQUESTS = 32

# Configure a delay(延迟） for requests for the same website (default:0)
DOENLOAD_DELAY = 3

# The download delay setting will honor only one of: 
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

```
### 多进程：进程的创建  

### 多进程：多进程程序调试技巧  

### 多进程：使用队列实现进程间的通信  

### 多进程：管道共享内存

### 多进程：锁机制解决资源抢占  

### 多进程：进程池  

### 多线程：创建线程  

### 多线程：线程锁  

### 多线程：队列  

### 多线程：线程池  

### 多线程：GIL 锁与多线程的性能瓶颈  

### 迷你 Scrapy 项目实践  