__author__ = 'leeyan'
import time

person_list=['Frank','Marlon','Allen','Lee']
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
    print('%s问的结果是: %res' %(person, res))
    return res

res=ask_way(person_list)
print(res)


# 一个类似于递归调用的函数
def a():
    print("this is a")
    def b():
        print("this is b")
        def c():
            res = "this is c"
            return res
        res = c()
        print(res)
        return res
    res=b()
    print(res)
    return res


