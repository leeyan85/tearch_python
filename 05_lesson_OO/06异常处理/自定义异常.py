class LeeException(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

    def get_info(self):
        print(self.msg)


try:
    raise LeeException("这是一个异常")

except LeeException as e:
    print(e)

# finally:
#     print("有无异常都执行 finally")

