### reduce用来将列表中的元素统一计算，最后统一为一个结果

#### 自己写一个reduce函数

num01 = [1,2,3,4,5]

def add(x,y):
    return x+y

def reduce_test(func,array,init=None):
    if init is None:
        res = array.pop(0)
    else:
        res = init
    for i in array:
        res = func(res,i)
    return res

print(reduce_test(add,num01,20))



#### 使用reduce函数
from functools import reduce
print(reduce(lambda x, y: x+y, num01, 10))