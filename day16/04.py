import functools

int2 = functools.partial(int, base = 2)
int8 = functools.partial(int, base = 8)
int16 = functools.partial(int, base = 16)

print(int('1001'))
print(int2('1001'))
print(int8('1001'))
print(int16('1001'))