Scrapy 原生不支持分布式，多机之间需要实现redis队列和管道共享，而scrapy-redis很好的实现了Scrapy和redis的集成
使用scrapy-redis之后Scrapy主要的变化：
1.使用RedisSpider类替代了Spider类
2.Scheduler的queue由Redis实现
3.item pipeline 由redis实现

安装并开启 ```pip install scrapy-redis```