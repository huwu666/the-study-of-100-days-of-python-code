#CRAPS赌博游戏
'''
CRAPS又称花旗骰,是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，
如果玩家摇出了 7 点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。为了增加代码的趣味性，
我们设定游戏开始时玩家有 1000 元的赌注，每局游戏开始之前，
玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，
如果庄家获胜，玩家就会输掉自己下注的金额。
游戏结束的条件是玩家破产（输光所有的赌注）。
'''

import random

money = 1000
while money > 0:
    print(f'你的总资产为{money}元')
    while True:
        debt = int(input('请下注:'))
        if 0 < debt <= money:
            break

    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    if first_point == 7 or first_point == 11:
        print('玩家胜')
        money += debt
        print(first_point)
    elif first_point == 2 or first_point == 12:
        print('庄家胜')
        money -= debt
        print(first_point)
    else:
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            if current_point == 7:
                print('庄家胜')
                money -= debt
                print(current_point)
                break
            elif current_point == first_point:
                print('玩家胜')
                money += debt
                print(current_point)
                break

print('你破产了,游戏结束')

'''
分支结构与循环结构都非常重要,是构造程序逻辑的基础,一定要
通过大量的练习来达到融合贯通
'''