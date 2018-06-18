
# 一个类如果没有申明自己的元类，那默认的元类就是type

# 元类是python中类对象的实现类，自己实现的的python类都元类的对象


class Foo:
    pass


f1 = Foo()

print(type(f1))
print(type(Foo))