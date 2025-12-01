class Student:

    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def study(self, course_name):
        print(f'{self.__name},{course_name}')
#__name一般表示私有的,_name一般表示受保护的


stu = Student('wangdachui', 20)
stu.study('python')
#print(stu.__name)
print(stu._age)

