
def a(name):
    print("this is 1st level a %s"%name)
    def b():
        name = "Allen"
        print("this is 2nd level is b, my uplevel is a %s" %name)
        def c():
            name = "Marlon"
            print("this is 3rd level is c, my up one level is b %s" %name)
        c()
    b()
a("Lee")