import random

red_balls = [i for i in range(1, 34)]
blue_ball = [i for i in range(1, 17)]

selected_balls = random.sample(red_balls, 6)
selected_balls.sort()

for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

blud_ball = random.choice(blue_ball)

print(f'\033[034m{blud_ball:0>2d}\033[0m')