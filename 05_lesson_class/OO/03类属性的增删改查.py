class ChinesePeople:
    dang = "共产党"

    def __init__(self):
        pass

    def play_ball(self):
        print("")

    def __setitem__(self, key, value):
        print("调用了setitem方法")
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setattr__(self, key, value):
        print("调用了setattr方法")
        self.__dict__['key'] = value

    def __repr__(self):
        return self.dang

print(ChinesePeople.__dict__)

p1 = ChinesePeople()

print(p1.dang)

ChinesePeople.skin = "黄色"

print(p1.skin)

p1['hello'] = "hello"

print(p1['hello'])

p1.name = "Lee"


print(ChinesePeople.__dict__)

print(p1)
