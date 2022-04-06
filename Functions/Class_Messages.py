from Functions.Class_Lottery import Lottery
from Functions.Class_Game import Game
class Prizes(Game):
    def __init__(self, player='Israel Israeli', ID=123456):
        super().__init__(player, ID)
        self.x, self.y = Lottery().is_match_white()

    def s(self):
        if self.x == 0:
            print('159$')
        else:
            print('15425555555')
a  = Prizes()
print(a.s())