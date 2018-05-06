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