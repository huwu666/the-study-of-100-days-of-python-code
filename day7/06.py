#craps 赌博游戏

import random

money = 1000
while money > 0:
    print(f'{money}')
    while True:
        debt = int(input('please enter your money'))
        if 0 < debt <= money:
            break
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'\n{first_point}')
    if first_point == 7 or first_point == 11:
        print('win \n')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('loster \n')
        money -= debt
    else:
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'{current_point}')
            if current_point == 7:
                print('loster \n')
                money -= debt
                break
            elif current_point == first_point:
                print('win \n')
                money += debt
                break
print('your are loster, game over')