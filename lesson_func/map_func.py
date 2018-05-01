### map函数
#### 自己实现map函数map_test
def add_one(n):
    return n+1

def map_test(func,array):
    ret=[]
    for i in array:
        res = func(i)
        ret.append(res)
    return ret

print(map_test(add_one,[3,4,5,6,7,8]))


#### map函数详解
res = map(lambda x:x+1,[1,2,3,4,5,6])
print(list(res))
