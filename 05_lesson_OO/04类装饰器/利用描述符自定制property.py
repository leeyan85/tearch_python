class Lazyproperty:  # 非数据描述符的优先级会低于实例属性
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print("执行get方法")
        if instance is None:
            return self
        res = self.func(instance)
        setattr(instance, self.func.__name__, res)
        return res


class Room:
    """
    这是一个Room的类
    """
    #length = 10
    #width = 10
    name = '客厅'

    def __init__(self, width, length, name):
        self.width = width
        self.length = length
        self.name = name

    @Lazyproperty  # 装饰器 mianji = Lazyproperty(mianji) 给类增加一个非数据描述符
    def mianji(self):
        return self.width * self.length

    @property
    def mianji1(self): # 装饰器 mianji = property(mianji1) 给类增加一个非数据描述符
        return self.width * self.length


print(Room.__dict__)
r1 = Room(10, 10, '卧室')
print(r1.__dict__)
print(r1.mianji)
print(r1.__dict__)
print(r1.mianji1)



