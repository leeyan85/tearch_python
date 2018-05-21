### 装饰器

#### 装饰器的本质
装饰器的本质就是函数，为其他函数提供附加功能

#### 装饰器的原则
1. 不修改被修饰函数的源代码
2. 不修改被修饰函数的调用方式

#### 装饰器的知识储备

装饰器 =  高阶函数 + 函数嵌套 + 闭包



#### 高阶函数
1. 函数接受的方式是以个函数名
2. 函数的返回值是一个函数名
3. 以上两种满足一种即为高阶函数


#### 函数嵌套
1. 在函数中有定义了一个函数


#### 闭包
闭包就是函数的作用域


#### 装饰器的框架
```
def derator(func):  # 接收的参数为一个函数名
    def wrapper(*args,**kwargs):  # 接收函数所需要的参数 
        # 输入你所需要的功能   
        res = func(*args,**kwargs)  #  运行所接受的函数
        return res # return 传入函数的返回值
    return wrapper  # 返回值是一个函数名 

```





