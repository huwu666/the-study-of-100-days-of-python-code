#定义一个类描述数字时钟,提供走字和显示时间的功能

import time

class Clock:
    
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min == 0
                self.hour += 1
                if self.hour == 24:
                    self.hour =0

    def show(self):
        return f'{self.hour}:{self.min}:{self.sec}'
    
clock = Clock(23, 59, 58)
while True:
    print(clock.show())
    time.sleep(1)
    clock.run()