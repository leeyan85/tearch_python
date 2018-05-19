## 面向对象
### 面向对象设计


### 面向对象编程

注意事项： 实例没有函数属性，调用的是类的函数属性

### 静态属性，类方法，静态方法


#### 静态属性
就是数据属性, 将函数作为静态属性
```
class Room:
    """
    这是一个Room的类
    """
    length = 10
    width = 10
    name = '客厅'

    def __init__(self, width, length, name):
        self.width = width
        self.length = length
        self.name = name

    @property #将函数作为静态属性
    def mianji(self):
        return self.width * self.length

```
#### 类方法
当需要直接通过类来访问类属性时使用类方法，实例也可以调用到类方法
主要的用处就是类通过类方法访问类的属性
```
class Room:
    """
    这是一个Room的类
    """
    length = 10
    width = 10
    name = '客厅'

    def __init__(self, width, length, name):
        self.width = width
        self.length = length
        self.name = name

    @classmethod # 当需要直接通过类名来访问类属性时使用，实例也可以调用到，但是无所谓
    def class_mianji(cls):
        print("这个房间是 %s"%(cls.name))

```

#### 静态方法
类的工具包，不与类绑定，也不与实例绑定，做与类和实例没有关系的方法，且类和实例都可以调用
```
class Room:
    """
    这是一个Room的类
    """
    length = 10
    width = 10
    name = '客厅'

    def __init__(self, width, length, name):
        self.width = width
        self.length = length
        self.name = name

    @staticmethod 
    def tenement(a, b, c):
        print("%s %s %s"%(a, b, c))
        
    def test(): # 这个不是一个静态方法，类类可以调用，但是实例不能调用
        print("这可不是静态方法，类可以调用，实例不能调用，因为实例调用类方法不许有self参数")
```



### 类的三大特性

#### 继承

##### 什么时候使用继承

1. 当多个类的属性和方法大部分都不同时，使用类组合的方式

2. 当多个类具有大多数相同的属性和方法时，使用继承

##### 继承的两种用途

1. 继承基类的方法，并且做出自己的改变或者扩展（代码重用）：实践中，继承的这种用途意义并不很大，甚至常常是有害的。因为它使得子类与基类出现强耦合。
    ```
    class Father:

    def __init__(self, name):
        self.name = name

    def hit_son(self):
        print("父亲%s西黄打他儿子 "%self.name)


    class Son(Father):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hit_son(self):
        print("父亲%s 从来不打儿子"%self.name)

    dad = Father("Lee")
    son = Son("Marlon", 25)
    son.hit_son()
    ```

2. 声明某个子类兼容于某基类，定义一个接口类（模仿java的Interface），接口类中定义了一些接口名（就是函数名）且并未实现接口的功能，子类继承接口类，并且实现接口中的功能python实现接口使用的是抽象类
    ###### 接口的好处
    接口提取了一群类共同的函数，可以把接口当做一个函数的集合。然后让子类去实现接口中的函数。这么做的意义在于归一化，什么叫归一化，就是只要是基于同一个接口实现的类，那么所有的这些类产生的对象在使用时，从用法上来说都一样。 

    归一化的好处在于：
    
    1. 归一化让使用者无需关心对象的类是什么，只需要的知道这些对象都具备某些功能就可以了，这极大地降低了使用者的使用难度。
    
    2. 归一化使得高层的外部使用者可以不加区分的处理所有接口兼容的对象集合
    
    ###### 定义一个接口
    ```
    class Interface:#定义接口Interface类来模仿接口的概念，python中压根就没有interface关键字来定义一个接口。
        def read(self): #定接口函数read
            pass

    def write(self): #定义接口函数write
        pass


    class Txt(Interface): #文本，具体实现read和write
        def read(self):
            print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')

    class Sata(Interface): #磁盘，具体实现read和write
        def read(self):
            print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')
    
    class Process(Interface):
        def read(self):
            print('进程数据的读取方法')

        def write(self):
            print('进程数据的读取方法')    
     ```
    ###### 什么是抽象类 ？ 
    抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化
    ###### 为什么要有抽象类 ？ 
     如果说类是从一堆对象中抽取相同的内容而来的，那么抽象类就是从一堆类中抽取相同的内容而来的，内容包括数据属性和函数属性。比如我们有香蕉的类，有苹果的类，有桃子的类，从这些类抽取相同的内容就是水果这个抽象的类，你吃水果时，要么是吃一个具体的香蕉，要么是吃一个具体的桃子。。。。。。你永远无法吃到一个叫做水果的东西。从设计角度去看，如果类是从现实对象抽象而来的，那么抽象类就是基于类抽象而来的。从实现角度来看，抽象类与普通类的不同之处在于：抽象类中只能有抽象方法（没有实现功能），该类不能被实例化，只能被继承，且子类必须实现抽象方法。这一点与接口有点类似，但其实是不同的。

    ###### 抽象类的实现
    ```
    import abc
    
    
    class AllFile(metaclass=abc.ABCMeta): #接口的定义方法继承
    
        @abc.abstractmethod
        def write(self):
            pass
    
        @abc.abstractmethod
        def read(self):
            pass
    
    
    class Mem(AllFile):
        device = "内存"
    
        def __init__(self):
            pass
    
        def write(self):
            print("%s 写文件" %self.device)
    
        def read(self):
            print("读文件")
    
    
    m1 = Mem()
    m1.write()
    ```
    ####### 抽象类和接口的不同
    抽象类的本质还是类，指的是一组类的相似性，包括数据属性（如all_type）和函数属性（如read、write），而接口只强调函数属性的相似性。抽象类是一个介于类和接口直接的一个概念，同时具备类和接口的部分特性，可以用来实现归一化设计 

##### 继承顺序
python3不区分新式类和经典类，继承方式采用广度优先，python2中有新式类和经典类，新式类使用广度优先，经典类是用深度优先
```

class A:
    def test(self):
        print('A')


class B(A):
    def test(self):
        print('B')


class C(A):
    def test(self):
        print('C')


class D(B):
    pass


class E(C):
    def test(self):
        print("E")


class F(D, E):
    pass


print(F.mro())

```

##### 在子类中调用父类
```

class Vehicle: #定义交通工具类
     city = '北京'

     def __init__(self, name):
         self.name = name

     def run(self):
         print('开动啦...')


class Subway(Vehicle): #地铁

    def __init__(self,name, speed, load, power, line):
        Vehicle.__init__(self, name) #这种调用方式并没有使用继承的方式调用
        self.line = line
        self.speed =speed
        self.load = load
        self.power = power

    def run(self):
        print('地铁%s号线欢迎您' % self.line)
        Vehicle.run(self)

    def show_info(self):
        print("这里是地铁%s号线"%self.line)


class Mobike(Vehicle):
    def __init__(self, name, speed):
        super(Mobike, self).__init__(name) # 使用继承的方式调用了父类的函数， 推荐使用这种调用方式
        self.speed = speed

    def run(self):
        print("骑着%s上班" % self.name)
        super(Mobike, self).run()


line13 = Subway('北京地铁', '180m/s', '1000人/箱', '电', 13)
line13.run()
line13.show_info()

mobike = Mobike('自行车', '10KM/h')
mobike.run()

```
#### 多态
多态指的是一类事物有多种形态，动物有多种形态：鸟，狗，猪

##### 多态是继承的一种体现方式
多态的基础就是继承，当子类继承了父类后，运行时就会产生多态，例如鸟，狗，猪的叫声各不相同
```
import abc


class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
    @abc.abstractmethod
    def talk(self):
        pass


class Duck(Animal): #动物的形态之一:人
    def talk(self):
        print('say gaga')


class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')


class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')

dog = Dog()
pig = Pig()
duck = Duck()

```

#### 封装

1. 类本身就是一种封装，将属性和方法进行了封装
2. 封装要明确的定义内部属性和外部属性, 外部无法直接访问内部的私有方法和属性
3. 封装真正的意义是把内部的逻辑提供一个接口给外部使用，用于程序扩展时使用
4. 双下滑开头定义了私有属性和私有方法，子类无法覆盖
    ```
    class People:
    
        _star = "earth"  # 单下划线开头的属性和方法，约定不能通过外部调用，实际是可以调用的
        __star = "earth"  # 私有属性只能在内部调用，外部调用时会出错
    
        def __init__(self, id, name, age, salary):
            print(self.__star)
            self.id = id
            self.name = name
            self.age = age
            self.salary = salary
    
        def get_id(self):
            print("我的身份证是%s" % self.__star)
    
        def get_star(self):
            self.__getstar()
    
        def __getstar(self):  #
            print(self.__star)
    
    
    print(People.__dict__)
    p1 = People("12121212121", 'Lee', 18, 100000)
    print(p1._star) #约定外部不能调用单下滑线开头的属性和方法
    p1.get_star()
    
    ```
 