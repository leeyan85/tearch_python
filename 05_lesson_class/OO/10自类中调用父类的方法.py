
class Vehicle: #定义交通工具类
     city = '北京'

     def __init__(self, name):
         self.name = name

     def run(self):
         print('开动啦...')


class Subway(Vehicle): #地铁

    def __init__(self,name, speed, load, power, line):
        Vehicle.__init__(self, name) #这种调用方式并没有使用继承的方式调用
        self.line = line
        self.speed =speed
        self.load = load
        self.power = power

    def run(self):
        print('地铁%s号线欢迎您' % self.line)
        Vehicle.run(self)

    def show_info(self):
        print("这里是地铁%s号线"%self.line)


class Mobike(Vehicle):
    def __init__(self, name, speed):
        super(Mobike, self).__init__(name) # 使用继承的方式调用了父类的函数， 推荐使用这种调用方式
        self.speed = speed

    def run(self):
        print("骑着%s上班" % self.name)
        super(Mobike, self).run()


line13 = Subway('北京地铁', '180m/s', '1000人/箱', '电', 13)
line13.run()
line13.show_info()

mobike = Mobike('自行车', '10KM/h')
mobike.run()