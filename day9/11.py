'''
双色球随机选号程序

双色球是由中国福利彩票发行管理中心发售的乐透型彩票，
每注投注号码由6个红色球和1个蓝色球组成。
红色球号码从1到33中选择,蓝色球号码从1到16中选择。
每注需要选择6个红色球号码和1个蓝色球号码

知乎上有一段对国内各种形式的彩票本质的论述相当精彩，
这里分享给大家：“虚构一个不劳而获的人，
去忽悠一群想不劳而获的人，最终养活一批真正不劳而获的人”。
很多对概率没有概念的人，甚至认为彩票中与不中的概率都是 50%;
还有很多人认为如果中奖的概率是 1%，那么买 100 
次就一定可以中奖，这些都是非常荒唐的想法。所以，
珍爱生命，远离赌博，尤其是你对概率一无所知的情况下！
'''

import random

from rich.console import Console
from rich.table import Table

console = Console()

n = int(input('生成几注号码:'))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

table = Table(show_header = True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify = 'center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)

    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]', 
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

console.print(table)