# 列表和元组
li = [1, 2, 3]
for i in li:
    print(i)

index = 0
iter_li = li.__iter__()


# 字符串
x = 'hello'
print(dir(x))
iter_x = x.__iter__()
print(iter_x.__next__())
print(iter_x.__next__())
print(iter_x.__next__())
print(iter_x.__next__())
print(iter_x.__next__())

# 系统的next()方法调用的就是，可迭代对象的 __next__方法
l2 = ['father', 'son', 'grandson']
iter_l2 = l2.__iter__()
print(iter_l2.__next__())
print(next(iter_l2))



# 用while模拟for循环的工作
while True:
    try:
        iter_li.__next__()
    except StopIteration as error:
        print('迭代完毕了')
        break


