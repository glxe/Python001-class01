
异常的例子：
```python
def f1():
    1/0

def f2():
    list1 = []
    # 这里会出现异常 list index out of range 被捕获输出，
    list1[1]
    #这里将不会运行
    f1()

def f3():
    f2()

try:
    f3()
except (ZeroDivisionError, Exception) as e:
    print(e)  
```

自定义异常类：
```python

class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    # 魔术函数
    def __str__(self):
        return self.errorinfo

userInput = 'a';

try:
    if (not userInput.isdigit()):
        raise UserInputError('用户输入错误') # 主动抛出错误
except UserInputError as ue:
    print(ue)
finally:
    del userInput
```

读取文件处理：
```python
# 传统的打开文件写法
file1 = open('a.txt', encoding='utf8')
try:
    data = file1.read()
finally:
    file1.close()

# with
with open('a.txt', encoding='utf8') as file1: #自动close文件流
    data = file1.read()
```

customer with exemple:
```python

class Open:
    def __init__(self):
        pass
    
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, type, value, trace):
        print('eixt')
        return self

    def __call__(self, a):
        print('call')
        print(a)
        pass

with Open() as f: # 这里的 f 其实是Open类中__enter__返回的值，
    f('a')
    pass
```

错误示例：
```python
class Open:
    def __enter__(self):
        print('enter')

    def __exit__(self, type, value, trace):
        print('eixt')

    def __call__(self, a):
        print('call')
        print(a)
        pass

with Open() as f:
    f('a')
    pass

#上面的这个代码运行会报下面的错误

# error.py 49 <module>
# f('a')

# TypeError:
# 'NoneType' object is not callable
# 因为f的值是__enter__的返回值，而上面这段代码是没有返回值的，即None，则运行的代码是None('a')，所以这是错误的
```



```
python3 -m pip install PyMySQL
```

pymysql操作示例：
```python
import pymysql

dbInfo = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'test'
}

sqls = ['select 1', 'select VERSION()']

result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls ):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )

        # 游標建立的時候就開啟了一個隱形的事務
        cur = conn.cursor()
        print(cur)
        try:
            for command in sqls:
                cur.execute(command)
                result.append(cur.fetchone())
                
            #關閉游標
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()

if __name__ == "__main__":
    db = ConnDB(dbInfo=dbInfo, sqls=sqls)
    db.run()
    print(result);
```