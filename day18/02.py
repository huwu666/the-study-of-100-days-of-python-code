class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        print('f{self.name}正在玩游戏.')

stu1 = Student('jishengshi', 44)
stu2 = Student('wangdachui', 25)
stu1.study('python程序设计')
stu2.play()
