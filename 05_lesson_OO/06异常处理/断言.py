def test1():
    res = 1
    return 1


res1 = test1()
assert res1 == 1

print("如果没有断言异常，则会执行后边的额代码")
