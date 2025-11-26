import functools
import operator

fac = lambda n: functools.reduce(operator.mul, range(2, n +1), 1)
is_prime = lambda x:all(map(lambda f: x % f , range(2, int(x ** 0.5) + 1)))

print(fac(6))
print(is_prime(37))