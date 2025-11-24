def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(3, 2.1, True, name = 'jishengshi', age = 21, gpa = 4)
