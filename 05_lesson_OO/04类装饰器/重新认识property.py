class Shoe:
    def __init__(self, name, price):
        self.name = name
        self.origin_price = price

    @property  # get时运行
    def price(self):
        return self.origin_price * 0.8

    @price.setter  # set时运行   # 可以利用property来实现类型检测功能
    def price(self, value):
        if isinstance(value, float):
            self.origin_price = value
        else:
            raise TypeError("price必须为浮点数")

    @price.deleter
    def price(self):
        print("删除我时运行这个函数")
        del self.origin_price


shoe = Shoe("nike", 1000)
shoe.price = 900.01
print(shoe.price)
del shoe.price