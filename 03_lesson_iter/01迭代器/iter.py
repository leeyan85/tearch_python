# 列表
li = [1, 2, 3]
for i in li:
    print(i)

index = 0
while index < len(li):
    print(li[index])
    index = index+1

# 字符串
x = 'hello'
print(dir(x))
iter_x = x.__iter__()
print(iter_x.__next__())
print(iter_x.__next__())
print(iter_x.__next__())
print(iter_x.__next__())
print(iter_x.__next__())

l2 = ['father', 'son', 'grandson']
iter_l2 = l2.__iter__()
print(iter_l2.__next__())
print(next(iter_l2))



