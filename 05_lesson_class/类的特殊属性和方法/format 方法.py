
class Date:

    format_dict = {
        "ymd": '{0.year}.{0.month}.{0.day}'
    }

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        fm = self.format_dict[format_spec]
        return fm.format(self)


d1 = Date(2018, 1, 5)

print(format(d1, 'ymd'))