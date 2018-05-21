class Fib:
    def __init__(self, n):
        self._begin = 1
        self._begin2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._begin > 100:
            raise StopIteration("终止")
        else:
            self._begin, self._begin2 = self._begin2, self._begin2 + self._begin
            return self._begin


h1 = Fib(1)

for i in h1:
    print(i)