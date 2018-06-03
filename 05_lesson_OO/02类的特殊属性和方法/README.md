## 类的特殊属性和方法

### __new__方法
只是对类进行实例化时，调用了__new__创建对象，并不会对这个对象进行初始化操作，是类级别的方法

### __init__方法
在__new__方法创建一个对象后，__init__方法对这个对象进行初始化操作，是实例级别的方法

### __call__方法

当实例执行()时，会调用__call__方法

### __slots__属性

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
    
    def __delete__(self, instance):
        print('delete')

```
2. 非数据描述符，没有实现__set__()方法
```
class Foo:
    def __get__(self, instance, owner):
        print('get')
        
    def __delete__(self, instance):
        print('delete')        

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

p1=People('Allen',18)

#描述符Str的使用
p1.name
p1.name='Lee'
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

#### 数据描述符注意事项

一 描述符本身应该定义成新式类,被代理的类也应该是新式类

二 必须把描述符定义成这个类的类属性，不能为定义到构造函数中

三 要严格遵循该优先级,优先级由高到底分别是

可以参考函数的闭包来进行判断优先级

1. 类属性，类属性赋值时，会把数据描述符所代理的类属性覆盖掉
2. 数据描述符，在给实例属性赋值时，如果属性被数据描述符代理了，那么复制时会调用数据描述符
3. 实例属性，实例属性正常的赋值
4. 非数据描述符，调用类的方法,也可以说是调用非数据描述符，实例方法也可以理解一种非数据描述符描述符，在应用类方法的时候都是实例化成一个类属性，类方法就是一个由非描述符类实例化得到的对象
5. 最后，找不到的属性触发__getattr__()



### __enter__和__exit__上下文管理协议

1. 使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预

2. 在需要管理一些资源比如文件，网络连接和锁的编程环境中，可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处

#### 代码例子
代码示例
    
```
    class Open:
        def __init__(self, name):
            self.name = name      
    
        def  __enter__(self):
            print("执行了enter方法")
            return self
    
        def __exit__(self, exc_type, exc_val, exc_tb):
            print("执行了exit方法")
            print(exc_type)  # 对应了异常的类型
            print(exc_val)  # 异常的具体内容
            print(exc_tb)  # 异常的traceback
    
    
    with Open('a.txt') as f:  # with 触发__enter__方法，将返回Open实例化的对象，as f语句将对象赋值给f 等同于 f = obj.__enter__()
        print(f.__dict__)
    
        print(f.adfadsf)  # 当程序出错时，会调用
        print(f.name)
```

#### 执行代码块时

1. 没有异常的情况下，整个代码框运行完毕后执行__exit__
2. 有异常的情况下，从异常出现的位置触发__exit__方法
3. 果__exit__返回值为True, 代表吞了异常
4. 如果__exit__返回值部位True，代表吐出了异常
5. __exit__的运行完毕，代表了真个with与语句执行完毕
