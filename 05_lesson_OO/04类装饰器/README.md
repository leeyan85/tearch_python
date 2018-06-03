## 类装饰器

装饰器可以是函数，同时也可以是类


### 类的装饰器
1. 利用类装饰器和数据描述符给类动态增加数据类型限制

```
class Type:  # 这是一个数据描述符
    def __init__(self, key, expect_type):
        self.key = key
        self.expect_type = expect_type

    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        print("触发了set方法")
        if not isinstance(value, self.expect_type):
            raise TypeError("需要传入的参数的类型为%s" % self.expect_type)
        else:
            instance.__dict__[self.key] = value

    def __delete__(self, instance):
        pass


def Typed(**kwargs):  # 这是一个装饰器
    def deco(obj):
        for key, value in kwargs.items():
            setattr(obj, key, Type(key, value))  # 给obj的属性设置为数据描述符， Type为数据描述符
        return obj
    return deco


@Typed(name=str, age=int)  # 给类增加装饰器，相当于deco = Typed(deco),Typed可以传入参数，Person = deco(Person)， 用装饰器的方式，给参数设置数据描述符相当于,
class Person:
    def __init__(self, name, age):  # name被Str类代理,age被Int类代理,
        self.name = name
        self.age = age


p1 = Person('Lee', 13)
print(p1.__dict__)
```
