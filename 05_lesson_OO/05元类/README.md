## 元类

元类是什么 ？ 
 
1. 一个类如果没有申明自己的元类，那默认的元类就是type

2. 元类是python中类对象的实现类，自己实现的的python类都元类的对象

可以从下面的代码得知，Foo类是元类type产生的一个对象
```
class Foo:
    pass


f1 = Foo()

print(type(f1))
print(type(Foo))
```

## 自定义元类

```
class Newtype(type):  # 继承type类
    def __init__(self, a, b, c):
        print("元类的构造函数执行")

    def __call__(self, *args, **kwargs): 
        print("类进行初始化时的()， 调用的是远元类的__call__方法")
        obj = object.__new__(self)
        print(type(obj))
        self.__init__(obj, *args, **kwargs)
        return obj


class Bar(metaclass=Newtype):  # 使用元类Newtype实例化Bar这个类，执行元类Foo的__init__函数
    def __init__(self, name):
        self.name = name


f1 = Bar("Lee")
print(f1.__dict__)

```

