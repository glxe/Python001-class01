
# 加了object 是显示继承 object。在2.2版本以上可以去掉object。
class Human(object):
    pass
    # 静态字段
    live = True

    def __init__(self, name):
        # 普通字段
        self.name = name


man = Human('adam')
woman = Human('Eve')

print(Human.__dict__)
print(man.__dict__)
print(woman.name)
print(woman.live)