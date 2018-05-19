class ChinesePeople:
    dang = "共产党"

    def __init__(self):
        self.name = "Lee"

    def play_ball(self):
        print("")


p1 = ChinesePeople()
p1.gender = "male"
print(p1.__dict__)
