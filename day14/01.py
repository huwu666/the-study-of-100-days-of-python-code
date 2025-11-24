#计算组合数

m = int(input('m = '))
n = int(input('n = '))

fm = 1
for num in range(1, m + 1):
    fm *= num

fn = 1
for num in range(1, n + 1):
    fn *= num

fk = 1
for num in range(1, m - n + 1):
    fk *= num

print(fm // fn // fk)
