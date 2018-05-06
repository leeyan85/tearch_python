
####实现自定filter函数
movie_people = ['sb_lee','marlon','sb_frank']
def sb(n):
    return n.startswith("sb")



def filter_test(func,array):
    ret = []
    for i in array:
        if sb(i):
            ret.append(i)
    return ret


print(list(filter_test(sb,movie_people)))



#### 和 lambda函数一起使用的filter函数
print(list(filter(lambda x:x.startswith("sb"), movie_people)))




