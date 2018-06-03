class Human:
    __slots__ = ['name', 'age']


f1 = Human()
f1.name = 'Lee'
f1.age = 18  # 报错
print(f1.__slots__)
#print(f1.__dict__)  # f1不再有__dict__属性, 会报错


class People:
    __slots__ = 'name'


p1 = People()
p1.name = "Lee"
p1.age = 18  # 因为__slots__中没有了age属性，所以会报错
