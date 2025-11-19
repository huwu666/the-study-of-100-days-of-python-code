t1 = (35, 12, 98)
t2 = ('a', 45, True, 'yancheng')

print(type(t1))
print(type(t2))

print(len(t1))
print(len(t2))

print(t1[0])
print(t2[2])
print(t2[-1])

print(t2[:2])
print(t2[::3])

for elem in t1:
    print(elem)

print(12 in t1)
print(99 in t1)
print('hao' not in t2)

t3 = t1 + t2
print(t3)

print(t1 == t3)
print(t1 >= t3)
print(t1 <= (35, 11, 99))