def dog(name,type,gender):

    def init():
        dog1={
            'name': name,
            'type': type,
            'gender': gender,
            'jiao': jiao,
        }
        return dog1

    def jiao(dog):
        print("有一条狗%s正在叫"%(dog['name']))

    res = init()

    return res


dog1=dog('Marlon','京巴','male')

dog1['jiao'](dog1)
