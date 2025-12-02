#让我们来用列表的知识重构上面统计骰子每种出现次数的代码

import random

counters = [0] * 6

for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1

for face in range(1, 7):
    print(f'{face} {counters[face - 1]}')
