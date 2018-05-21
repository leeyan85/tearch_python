
import abc  #利用abc模块实现抽象类


class AllFile(metaclass=abc.ABCMeta): #接口的定义方法继承

    @abc.abstractmethod
    def write(self):
        pass

    @abc.abstractmethod
    def read(self):
        pass


class Mem(AllFile):
    device = "内存"

    def __init__(self):
        pass

    def write(self):
        print("%s 写文件" %self.device)

    def read(self):
        print("读文件")


m1 = Mem()
m1.write()

