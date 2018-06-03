class List(list):
    def show_middle(self):
        return self[int(len(self)/2)]

    def append(self, item):
        print('----->', item)
        if type(item) is str:
            super().append(item)
        else:
            print("只能添加字符串")


l2 = List("hello,world")
print(l2.show_middle())

l2.append(1)
print(l2)