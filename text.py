from lottery_logic import Lottery
class Text(Lottery):
    def message(self):
        white = self.white
        gold = self.gold
        if gold == 0:
            if white == 5:
                return 'You Get {} White Balls Without The Power Ball: \nPrize :150000 $'.format(white)
            if white == 4:
                return 'You Get {} White Balls Without The Power Ball: \nPrize :1500 $'.format(white)
            if white == 3:
                return 'You Get {} White Balls Without The Power Ball: \nPrize :150 $'.format(white)
            if white == 2:
                return 'You Get {} White Balls Without The Power Ball: \nPrize :15 $'.format(white)
            else:
                return 'No Prize, Sorry ☺'

        if gold == 1:
            if white == 5:
                return 'You Get {} White Balls and The Power Ball: \nPrize :1500000000000000 $'.format(white)
            if white == 4:
                return 'You Get {} White Balls and The Power Ball: \nPrize :1520000000 $'.format(white)
            if white == 3:
                return 'You Get {} White Balls and The Power Ball: \nPrize :122500000 $'.format(white)
            if white == 2:
                return 'You Get {} White Balls and The Power Ball: \nPrize :1225 $'.format(white)
            else:
                return 'No Prize, Sorry ☺'

    def __str__(self):
        return super().__str__() + f'\nMessage:{str(self.message())}'


