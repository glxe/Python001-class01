

# 让实例方法成为类的方法
class Kls1(object):
    bar = 1
    def foo(self):
        print(self)
        print('in foo')
    
    # 使用类属性、类方法
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()

Kls1.class_foo()


############
class Story(object):
    snake = 'Python'
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake