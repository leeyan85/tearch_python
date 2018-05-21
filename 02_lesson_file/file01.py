#!/usr/local/bin/python
f = open('test.txt', 'r')
print(f.readline())
print(f.readline())  # 当文件较大时需要使用 readline操作文件，相当与一个迭代器


for line in f:
    print('adsfjkas', line)

f.close()
