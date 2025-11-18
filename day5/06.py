score = int(input('score = '))

if score > 90:
    grade = 'a'
elif score > 80:
    grade = 'b'
elif score > 70:
    grade = 'c'
elif score > 60:
    grade = 'd'
else:
    grade = 'e'

print(f'{grade = }')