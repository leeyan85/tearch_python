class Foo:
    def __init__(self, x):
        self.x = x


class Bar(Foo):
    pass


print(isinstance(Foo, object))
print(issubclass(Bar, Foo))



