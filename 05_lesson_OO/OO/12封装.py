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
print(p1._star)  #约定外部不能调用单下滑线开头的属性和方法
p1.get_star()
