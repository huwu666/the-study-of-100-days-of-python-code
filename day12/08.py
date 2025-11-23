fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))

print(fset1)
print(fset2)

print(fset1 & fset2)
print(fset1 | fset2)
print(fset1 - fset2)
print(fset1 < fset2)