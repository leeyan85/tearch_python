class Human(object):
    """
    这是一个关于人的类，这些注释信息将会在类的__doc__属性中显示
    """

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):  # 调用对象中不存在的属性时会触发这个函数
        print("当获取对象的属性不存在时，会触发函数__getattr__，当属性存在时不会触发")

    def __delattr__(self, item):  # 删除属性时会调用这个函数
        print("删除属性时会触发__delattr__函数")
        self.__dict__.pop(item)

    def __setattr__(self, key, value):  # 设置属性时会调用这个函数, 在这里将系统默认的重写了
        print("设置属性时，会触发__setattr__函数")
        self.__dict__[key] = value

    def __setitem__(self, key, value): # 当使用 p1['name'] = 'Lee' 这种方式赋值时会调用这个方法
        print('setitem', key, "get", value)
        self.__dict__[key] = value

    def __str__(self):  # 在程序运行是显示程序的返回显示
        return "instance %s" % self.name

    def __repr__(self):  # 在解释器中使用时，显示程序的返回显示
        return self.name

    def __del__(self):  # 析构方法，当对象被删除时，触发执行，通常不需要定义
        print("这是析构函数__del__")

    def __call__(self, *args, **kwargs):
        print("实例执行了()会调用__call__方法， 例如：obj()")


P1 = Human('Lee')
P1()
# print(P1.__dict__)
# print(P1.__class__)  # 显示对象是哪个类的实例化
# print(P1.__module__)  # __module__ 显示来自哪个module
# print(P1.asfd)  # 报错因为，不错存在这个

