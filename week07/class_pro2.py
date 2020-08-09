
# 加了object 是显示继承 object。在2.2版本以上可以去掉object。
class Human(object):
    # 人为约定不可修改
    _live = True

    # 私有属性
    __fly = False

    def __init__(self, name):
        # 普通字段
        self.name = name
