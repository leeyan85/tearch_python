

"""
函数作用域讲解
"""
def level1():
    global a
    a="hello,world"
    print ('hello,world')
    def level2():
        print("bar")
        def level3():
            print ()
            return "level3"
        return level3
    return level2




