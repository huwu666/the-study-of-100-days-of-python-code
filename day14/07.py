#使用可变位置参数实现对任意多个数求和的add函数

def add(*args):
    total = 0
    for val in args:
        if type(val) in (int, float):
            total += val
    return total

print(add())
print(add(1))
print(add(1, 2, 3))
print(add(1, 2, 'hello', 3.45, 6))