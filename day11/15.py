#使用print函数输出字符串时，可以使用下面的方式来完成字符串的格式化

a = 321
b = 123
print('%d * %d = %d ' % (a, b, a*b))

print('{0} * {1} = {2}'.format(a, b, a*b))

print(f'{a} * {b} = {a * b}')