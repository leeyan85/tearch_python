class LeeException(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg



try:
    raise LeeException("异常")

except LeeException as e:
    print(e)

finally:
    print("有无异常都执行 finally")

