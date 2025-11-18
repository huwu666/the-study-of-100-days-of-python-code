height = float(input('height '))
weight = float(input('weight '))

bmi = weight / (height / 100) ** 2

print(f'{bmi = :.1f}')

if bmi < 18.5:
    print('1')
elif bmi < 24:
    print('2')
elif bmi < 27:
    print('3')
elif bmi < 30:
    print('4')