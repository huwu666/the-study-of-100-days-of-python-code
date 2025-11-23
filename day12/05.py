set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}

print(set1 < set2)
print(set1 <= set2)
print(set2 < set3)
print(set2 <= set3)
print(set2 > set1)
print(set2 == set3)

print(set1.issubset(set2))
print(set2.issuperset(set1))