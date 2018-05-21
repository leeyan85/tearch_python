## 类的特殊属性和方法

### \_\_slots\_\_ 属性

1. 类实例化一个对象后，每个对象都会有__dict__属性字典，\_\_dict__占用的内存较大，如果你有一个属性很少的类,但是有很多实例，为了节省内存，可以使用__slots__取代实例的__dict__，实例将不能通过__dict__来查看属性字典了，实例添加新的属性时,只能使用在__slots__中定义的那些属性名。

2. __slots__可以是元组，列表，也可以是字符串，字符串意味着只有一个数据属性

2. 关于__slots__的一个常见误区是它可以作为一个封装工具来防止用户给实例增加新的属性。尽管使用__slots__可以达到这样的目的,但是这个并不是它的初衷，更多的作用就是用来节省内存

示例代码如下，也可以参考slots属性.py 
```
class Human:
    __slots__ = ['name','age']

f1 = Human()
f1.name = 'Lee'
f1.age = 18  # 报错
print(f1.__slots__) 
print(f1.__dict__)  #f1不再有__dict__属性, 会报错

class People:
    __slots__ = name
    
p1 = People()
p1.name = "Lee"
P1.age = 18  # 因为__slots__中没有了age属性，所以会报错
```

## 数据描述符
### 描述符是什么
描述符本质就是一个新式类,在这个新式类中,至少实现了__get__(),\_\_set__(),\_\_delete__()中的一个,这也被称为描述符协议
1. \_\_get__():调用一个属性时,触发
2. \_\_set__():为一个属性赋值时,触发
3. \_\_delete__():采用del删除属性时,触发

由这个类产生的实例进行属性的调用/赋值/删除,并不会触发这三个方法

### 描述符的分类
1. 数据描述符，至少实现了__get__()和__set__()
```
class Foo:
    def __set__(self, instance, value):
        print('set')
    def __get__(self, instance, owner):
        print('get')

```
2. 非数据描述符，没有实现__set__()方法
```
class Foo:
    def __get__(self, instance, owner):
        print('get')

```

### 如何使用描述符

何时何地会使用描述符，请看下面的例子
```
#描述符Str
class Str:
    def __get__(self, instance, owner):
        print('Str调用')
    def __set__(self, instance, value):
        print('Str设置...')
    def __delete__(self, instance):
        print('Str删除...')

#描述符Int
class Int:
    def __get__(self, instance, owner):
        print('Int调用')
    def __set__(self, instance, value):
        print('Int设置...')
    def __delete__(self, instance):
        print('Int删除...')

class People:
    name=Str()
    age=Int()
    def __init__(self,name,age): #name被Str类代理,age被Int类代理,
        self.name=name
        self.age=age

#何地？：定义成另外一个类的类属性

#何时？：且看下列演示

p1=People('alex',18)

#描述符Str的使用
p1.name
p1.name='egon'
del p1.name

#描述符Int的使用
p1.age
p1.age=18
del p1.age

#我们来瞅瞅到底发生了什么
print(p1.__dict__)
print(People.__dict__)

#补充
print(type(p1) == People) #type(obj)其实是查看obj是由哪个类实例化来的
print(type(p1).__dict__ == People.__dict__)

描述符应用之何时?何地?
```
