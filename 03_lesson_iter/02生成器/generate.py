# 三元表达式
## if else

name = "Lee"
res = "帅" if name == "Lee" else "挫"
print(res)

##  列表解析
li = ["鸡蛋%s"%i for i in range(10) if i > 5 ]
print(li)

##生成器

### 生成器表达式
li_iter = ("鸡蛋%s"%i for i in range(10) if i > 5 )

print(next(li_iter))
print((li_iter.__next__()))
##生成器表达式比列表解析省内存

### 生成器函数
def my_generater():
    for i in range(10):
        yield i

li2_iter = my_generater()
print(li2_iter.__next__())
print(li2_iter.__next__())


#yield 3相当于return 控制函数的返回值
#x=yield 接受send传过来的值，赋值给x

def test():
    print("begin")
    firt = yield 1
    print('first', firt)
    yield 2
    print('second')

t = test()
res = t.__next__()
print(res)
res = t.send('将这个值，返回给yield') #send函数将值返回给 yield，赋值给了 x = yield 的x
print(res)