class Student:
    def __init__(self, name, course, school):
        self.name = name
        self.course = course
        self.school = school

    def learning(self):
        print("%s 正在 %s 学习 %s课程" %(self.name, self.school.name, self.course.name))


class School:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    sc1 = School("清华")
    c1 = Course("计算机科学与技术")
    st1 = Student("Lee", c1, sc1)
    st1.learning()