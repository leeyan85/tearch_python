import abc


class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
    @abc.abstractmethod
    def talk(self):
        pass


class Duck(Animal): #动物的形态之一:人
    def talk(self):
        print('say gaga')


class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')


class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')


duck = Duck()
duck.talk()