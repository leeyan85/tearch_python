class BalckMedium:

    feature = "Ugly"

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print("%s 正在出售房子" % self.name)

    def rent_house(self):
        print("%s 正在出租房子" % self.name)


b1 = BalckMedium("万成置地", "天露园")
b1.sell_house()


# 这四种方法适用于类和对象

print(hasattr(b1, 'sell_house'))
print(getattr(b1, 'sell_house1', '不存在在这个方法'))
setattr(b1, 'age', '19')
print(b1.age)
delattr(b1, 'age')
print(b1.age)
