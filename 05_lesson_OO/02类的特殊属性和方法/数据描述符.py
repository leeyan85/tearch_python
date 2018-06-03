class Foo:
    def __get__(self, instance, owner):
        print('触发get')

    def __set__(self, instance, value):
        print('触发set')

    def __delete__(self, instance):
        print('触发delete')


f1 = Foo()  # 描述符不能被实例化，只能在别的类中对某些属性进行处理
f1.name = 'egon'


class Bar:
    x = Foo()
    def __init__(self):
        pass


# b1 = Bar()
# b1.x = 1
# print(b1.__dict__)
#
# # 疑问: 何时,何地,会触发这三个方法的执行


# 描述符Str
class Str:
    def __get__(self, instance, owner):
        print('Str调用')
    def __set__(self, instance, value):
        print('Str设置...')
    def __delete__(self, instance):
        print('Str删除...')

# 描述符Int
class Int:
    def __get__(self, instance, owner):
        print('Int调用')

    def __set__(self, instance, value):
        print('Int设置...')

    def __delete__(self, instance):
        print('Int删除...')


class Type:
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


class People:
    name = Str()
    age = Int()

    def __init__(self, name, age):  # name被Str类代理,age被Int类代理,
        self.name = name
        self.age = age

# 何地？：将数据描述符，定义成另外一个类的类属性

# 何时？：且看下列演示


class Person:

    name = Type('name', str)
    age = Type('age', int)

    def __init__(self, name, age):  # name被Str类代理,age被Int类代理,
        self.name = name
        self.age = age


# p1=People('Allen',18)
#
# # 描述符Str的使用
# p1.name
# p1.name='Lee'
# del p1.name
# #
# #描述符Int的使用
# p1.age
# p1.age=18
# del p1.age
#
# #我们来瞅瞅到底发生了什么
# print(p1.__dict__)
# print(People.__dict__)
#
# #补充
# print(type(p1) == People) #type(obj)其实是查看obj是由哪个类实例化来的
# print(type(p1).__dict__ == People.__dict__)

p2 = Person(18, '18')

print(p2.__dict__)