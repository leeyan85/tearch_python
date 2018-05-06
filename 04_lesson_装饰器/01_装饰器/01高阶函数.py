import time

# 高阶函数第一种情况 函数接受的方式是以个函数名

def timer(func):
    print("高阶函数第一种情况 函数接受的方式是以个函数名")
    starttime = time.time()
    res = func()
    stoptime = time.time()
    print("函数运行时间为%f"% (stoptime-starttime))
    return res


# 高阶函数第二种情况 函数的返回值是一个函数名

def timer2(func):
    print("高阶函数第二种情况，返回值是一个函数名")
    starttime = time.time()
    res = func()
    stoptime = time.time()
    print("函数运行时间为%f"% (stoptime-starttime))
    return func



def a():
    res = 0
    for i in range(1,20):
        time.sleep(0.1)
        res += i
    return res



res  = timer(a)
print(res)

a =  timer2(a)
print(a())


