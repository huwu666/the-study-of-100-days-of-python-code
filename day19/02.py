class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('wangdachui', 20)
stu.sex = 'nan'

print(stu.name)
print(stu.age)
print(stu.sex)