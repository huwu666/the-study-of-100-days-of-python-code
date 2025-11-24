#判断三条边的长度能否构成三角形

def make_judgement(a, b, c):
    return a + b > c and b + c > a and a + c > b

print(make_judgement(3, 4, 5))
print(make_judgement(1, 2, 3))