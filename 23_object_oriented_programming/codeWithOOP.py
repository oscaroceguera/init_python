class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("OCEGUERA", (90, 90, 78, 90))
print(student.name)
print(student.grades)
print(student.average_grade())
print('-------------------------')
student2 = Student("BOBADILLA", (90, 90, 78, 90))
print(student2.name)
print(student2.grades)
print(student2.average_grade())
