from lottery_logic import Lottery
from game import Game
from text import Text

''' Create Instances '''
''' This Is Return Only The Name and The Age'''
Joe = Game('Joe', 15)
Chris = Game('Chris', 15)

''' This Is Return The Name,Age, Range Of Numbers, And The Results'''
Yosef = Lottery('Yosef', 25, 1, 12)
Raz = Lottery('Raz', 25, 1, 6)

''' This Is Return The Name,Age, Range Of Numbers, And The Results and The appropriate message'''
Lili = Text('Lili', 24, 1, 7)
Joni = Text('Joni', 1, 1, 12)

print(Joe)
print('-------------------------------------------------------------------------------')
print(Raz)
print('-------------------------------------------------------------------------------')
print(Lili)