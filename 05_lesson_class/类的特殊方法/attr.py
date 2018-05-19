class Human(object):
    def __init__(self, name):
        self.name = name

    def __setitem__(self, key, value):
        print('setitem', key, "get", value)
        self.__dict__[key] = value

    def __setattr__(self, key, value):
        print("setattr",key, 'get', value)
        self.__dict__[key] = value

    '''
    def __str__(self):
        return "instance %s" % self.name
    '''

    def __repr__(self):
        return self.name



if __name__ == "__main__":
    P1 = Human('yangaofeng')
    P1.age = 18
    print(P1)
    #print(f)
