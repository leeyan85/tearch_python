class Open:
    def __init__(self, name):
        self.name = name


    def  __enter__(self):
        print("执行了enter方法")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("执行了exit方法")
        print(exc_type)
        print(exc_val)
        print(exc_tb)


with Open('a.txt') as f:  # with 触发__enter__方法，将返回Open实例化的对象，as f, 赋值给f 等同于 f = obj.__enter__()
    print(f.__dict__)

    print(f.adfadsf)  # 当程序出错时，会调用
    print(f.name)





