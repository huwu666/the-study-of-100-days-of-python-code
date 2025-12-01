file = open('day21/01.txt', 'r', encoding = 'utf-8')
for line in file:
    print(line, end = '')
file.close()

file = open('day21/01.txt', 'r', encoding = 'utf-8')
lines = file.readlines()
for line in lines:
    print(line, end = '')
file.close()