height = float(input('height'))
weight = float(input('weight'))

bmi = weight / (height / 100) ** 2

print(f'{bmi = :.1f}')

if 18.5 <= 24:
    print('good')
else:
    print('bad')
