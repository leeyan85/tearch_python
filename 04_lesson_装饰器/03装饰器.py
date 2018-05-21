import time

def time_deractor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print("函数运行时间为%f" %(stop_time - start_time))
        return res
    return wrapper

@time_deractor # 这个就等于 test = timmer_deractor(test)
def test(number):
    res = 0
    for i in range(number):
        res += i
    return res

b = test(20)
print(b)

