
### 递归函数

#### 递归函数的要求
1. 有明确的停止条件
2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少

#### 递归的缺陷
1. 递归效率不高，递归层次过多会导致栈溢出（在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出）


#### 递归问路

```
__author__ = 'Linhaifeng'
import time

person_list=['Marlon','Allen','Frank','Lee']
def ask_way(person_list):
    print('-'*60)
    if len(person_list) == 0:
        return '没人知道'
    person=person_list.pop(0)
    if person == 'Lee':
        return '%s说:我知道,老男孩就在沙河汇德商厦,下地铁就是' %person
    print('hi 美男[%s],敢问路在何方' %person)
    print('%s回答道:我不知道,但念你慧眼识猪,你等着,我帮你问问%s...' %(person,person_list))
    time.sleep(3)
    res=ask_way(person_list)
    print('%s问的结果是: %res' %(person,res))
    return res

if __name__ == "__main__":
    res=ask_way(person_list)
    print(res)
```



#### 举个类似于递归的过程


```
def a():
    print("this is a")
    def b():
        print("this is b")
        def c():
            res = "C func is the last func"
            return res
        res = c()
        print(res)
        return res
    res=b()
    print(res)
    return res

a()
```
