class Foo:
    def __init__(self, x):

        self.x =  x

    def __getattr__(self, item):  # 当属性不存在时触发这个函数
        print("get attr")


class Bar(Foo):
    pass


print(isinstance(Foo, object))
print(issubclass(Bar, Foo))


F1 = Foo("Lee")
print(F1.y)


