
# 加了object 是显示继承 object。在2.2版本以上可以去掉object。
class MyFirstClass(object):
    pass



a = MyFirstClass()
b = MyFirstClass()
# 不同内存的地址，两个不同的对象
# print(type(a))
# print(type(b))
# print(id(a))
# print(id(b))
c = a.__class__()
d = b.__class__()
print(c)
print(d)

print(a.__class__())
pass
print(b.__class__())




# 类也是对象
c = MyFirstClass
d = c()
# print(d.__class__())