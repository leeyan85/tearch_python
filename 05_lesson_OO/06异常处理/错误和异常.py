a = "asdfasdf"

try:
    int(a)

except Exception as e:
    print(e)

else:
    print("没有异常执行我")

finally:
    print('无论有无异常，执行我')