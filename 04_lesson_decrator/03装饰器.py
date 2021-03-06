import time

def time_deractor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print("函数运行时间为%f" %(stop_time - start_time))
        return res
    return wrapper

def check_info(info):
    print(info)
    def check_arg(func):
        def wrapper(*args, **kwargs):
            if isinstance(*args, int):
                result = func(*args, **kwargs)
                return result
            else:
                print("参数错误")
                return "参数错误，只接受整形"
        return wrapper
    return check_arg


#@check_info("hello")   ## 相当于 check_arg = check_info('hello'), test =  check_arg(test), 如下所示
def test(number):
    res = 0
    for i in range(number):
        res += i
    return res


# test 之前加@ 的过程类似于这样一下的流程
check_arg = check_info('hello')
test = check_arg(test)
b = test(10)
print(b)



