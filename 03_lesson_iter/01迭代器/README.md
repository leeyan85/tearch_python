
#### 迭代器协议

1. 迭代器协议是指：对象必须提供一个__next__方法，执行该方法要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代 （只能往后走不能往前退）

2. 可迭代对象：实现了迭代器协议的对象（如何实现：对象内部定义一个__iter__()方法）

3. 协议是一种约定，可迭代对象实现了迭代器协议，python的内部工具（如for循环，sum，min，max函数等)使用迭代器协议访问对象。

注: 迭代器,python3可以通过__next__取值，python2中为next方法



#### for循环遵循迭代器协议

1. 循环所有的项，全都是使用迭代器协议，首先使用对象的__iter__方法将对象变为可迭代对象
2. for循环做了异常处理StopIteration

注: 列表，元组，字符串这些序列类型，都不是可迭代对象,For循环机制，调用了这些对象的__iter__方法，把他们变成了可迭代对象



##### 用while模拟for循环的工作
```
li = [1, 2, 3]
while True:
    try:
        iter_li.__next__()
    except StopIteration as error:
        print('迭代完毕了')
        break
```

注：字典，集合，文件都不是序列类型，所以不能用while来进行循环

