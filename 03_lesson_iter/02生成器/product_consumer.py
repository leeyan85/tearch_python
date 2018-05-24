
def consumer(name):
    while True:
        x =  yield "%s开始吃包子" % name
        print('%s吃了第 %s 个包子' % (name, x))


def producer():
    c1 = consumer("Marlon")
    c1.__next__()
    for i in range(10):
        print("开始生产第%s个包子" % i)
        c1.send(i)

producer()