class Newtype(type):  # 继承type类
    def __init__(self, a, b, c):
        print("元类的构造函数执行")

    def __call__(self, *args, **kwargs):
        print("类进行初始化时的()，首先调用的是元类的__call__方法")
        obj = object.__new__(self)
        # print(type(obj))
        self.__init__(obj, *args, **kwargs)
        return obj


class Bar(metaclass=Newtype):  # 可以理解为，class 关键字执行的操作是，实例化Newtype元类，实例化后的对象是Bar这个类，执行的是元类Newtype的__init__函数，
    def __init__(self, name):
        print("实例的初始化方法")
        self.name = name


f1 = Bar("Lee")
print(f1.__dict__)


