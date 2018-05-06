

## 三元表达式
### x if a else b
```
name = "Lee"
res = "帅" if name == "Lee" else "挫"
print(res)
```
###  列表解析 [i for i in x]
```
li = ["鸡蛋%s"%i for i in range(10) if i > 5 ]
print(li)
```

## 生成器

### 什么是生成器

生成器可以理解为一种数据类型，自动实现了迭代器协议，是一种可迭代对象

### 生成器表达式
```li_iter = ("鸡蛋%s"%i for i in range(10) if i > 5 )

print(next(li_iter))
print((li_iter.__next__()))
```

注：生成器表达式比列表解析省内存


```
### 生成器函数
def my_generater():
    for i in range(10):
        yield i

li2_iter = my_generater()
print(li2_iter.__next__())
print(li2_iter.__next__())
```




