#扑克游戏

from enum import Enum

class Suite(Enum):
    '''花色(枚举)'''
    SPADE, HEART, CLUB, DIAMOND = range(4)

for suite in Suite:
    print(f'{suite}:{suite.value}')

class Card:
    '''牌类'''

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[suite.value]}{faces[self.face]}'
    
'''
card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1)
print(card2)
'''

#接着定义扑克类
import random

class Poker:
    '''扑克'''

    def __init__(self):
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        '''洗牌'''
        random.shuffle(self.cards)

    def deal(self):
        '''发牌'''
        card = self.cards[self.current]
        self.current += 1
        return card
    
    @property
    def has_next(self):
        '''还没有牌可以发'''
        return self.current < len(self.cards)
    
Poker = Poker()
print(Poker.cards)
Poker.shuffle()
print(Poker.cards)