import importlib

from m1.reflact import test1

# 根据字符串找到模块

module_name = "m1.reflact"

m = __import__(module_name)  # __import__ 只能导入最顶级的模块
print(m)
m.reflact.test1()
m.reflact.__test2()

m = importlib.import_module('m1.reflact')  # 可以导入指定的那一级模块
m.test1()
m.__test2()











