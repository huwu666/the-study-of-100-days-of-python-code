import itertools

a = itertools.permutations('abcd')
b = itertools.combinations('abcde', 3)
c = itertools.product('abcd', '123')
d = itertools.cycle(('a', 'b', 'c', 'd'))

print(a)
print(b)
print(c)
print(d)
print(3)