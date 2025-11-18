items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['python', 'java', 'go', 'kotlin']
items3 = [100, 12.3, 'python', True]
print(items1)
print(items2)
print(items3)

items4 = list(range(1, 10))
items5 = list('hello')
print(items4)
print(items5)

items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['python', 'java', 'javascript']
print(items5 + items6)
print(items6 + items7)
items5 += items6
print(items5)

print(items6 * 3)
print(items7 * 2)

print(29 in items6)
print(99 in items6)
print('c++' not in items7)
print('python' not in items7) 

items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])
print(items8[2])
print(items8[4])
items8[2] = 'durian'
print(items8)
print(items8[-5])
print(items8[-4])
print(items8[-1])
items8[-4] = 'strawberry'
print(items8)

print(items8[1: 3: 1])
print(items8[0: 3: 1])
print(items8[0: 5: 2])
print(items8[-4: -2: 1])
print(items8[-2: -6: -1])

print(items8[1: 3])
print(items8[: 3: 1])
print(items8[: : 2])
print(items8[-4: -2])
print(items8[-2:: -1])

items8[1: 3] = ['x', 'o']
print(items8)

