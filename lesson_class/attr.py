class Foo:
    def __init__(self,name):
        self.name = name

    def __setitem__(self, key, value):
        print('setitem',key,"获得",value)

    def __setattr__(self, key, value):
        print("setattr",key, '获得', value)

    def __str__(self):
        return "Foo实例"

    def __repr__(self):
        return "Foo是咧"

f = Foo('yangaofeng')
f['name']= "egon" #复制给类变量
f.age = 18 #赋值对象变量
print(f)
