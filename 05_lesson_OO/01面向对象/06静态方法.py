class Room:
    """
    这是一个Room的类
    """
    length = 10
    width = 10
    name = '客厅'

    def __init__(self, width, length, name):
        self.width = width
        self.length = length
        self.name = name

    @staticmethod #类的工具包，不与类绑定，也不与实例绑定，做与类和实例没有关系的方法
    def tenement(a, b, c):
        print("%s %s %s"%(a, b, c))

    def test():
        print("这可不是静态方法，类可以调用，实例不能调用")


print(Room.__dict__)

room1 = Room(10, 10, "restroom")
print('room1 的作用是', room1.name)
room1.tenement("Allen", "Marlon", "Frank")
Room.tenement("Allen", "Marlon", "Frank")
Room.test()

