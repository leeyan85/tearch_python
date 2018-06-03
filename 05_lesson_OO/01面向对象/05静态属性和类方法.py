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

    @property #将函数作为静态属性
    def mianji(self):
        return self.width * self.length

    @classmethod # 当需要直接通过类名来访问类属性时使用，实例也可以调用到，但是无所谓
    def class_mianji(cls):
        print("这个房间是 %s"%(cls.name))


room1 = Room(10, 10, "restroom")
print('room1 的作用是', room1.name)

Room.class_mianji()
