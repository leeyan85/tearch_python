class Father:

    def __init__(self, name):
        self.name = name

    def hit_son(self):
        print("父亲%s喜欢打他儿子 "%self.name)


class Son(Father):

    def __init__(self, name, age):
        super(Son, self).__init__(name)
        self.age = age

    def hit_son(self):
        print("父亲%s从来不打儿子"%self.name)


father = Father("Lee")
father.hit_son()

son = Son("Marlon", 25)
son.hit_son()
