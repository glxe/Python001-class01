
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



man.live = False


print(man.live)
# 类可以使用静态字段
Human.live

# 可为类添加静态字段
Human.newattr = 1

print(dir(Human))
print(Human.__dict__)

# 内置类型是不能添加属性和方法的
setattr(Human, 'newattr1', 'value')

print(dir(Human))
print(Human.__dict__)