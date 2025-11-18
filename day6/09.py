import random

answer = random.randrange(1, 101)
counter = 0
while True:
    counter += 1
    num = int(input('请输入 '))
    if num < answer:
        print('大一点')
    if num > answer:
        print('小一点')
    else:
        print('good')
        break
print(f'{counter}')