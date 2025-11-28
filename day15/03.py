#最大公约数与最小公倍数

def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)

def gcd(x: int, y:int) -> int:
    while y % x != 0:
        x, y = y % x, x
    return x