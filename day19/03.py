class Student:
    
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('wangdachui', 20)

stu.sex = 'nan'