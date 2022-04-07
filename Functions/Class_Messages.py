from Functions.Class_Lottery import Lottery
# Create a New Class That Print The Messages:
class Messages(Lottery):
    def __init__(self, player='Israel Israeli', ID=123456):
        super().__init__(player, ID)

    # The is_match Method Return 2 Values , on the two values that come back we will receive appropriate messages
    def prizes(self):
        self.white, self.gold = Lottery().is_match()
        # First Condition : gold ball = 1
        if self.gold == 1:
            if self.white == 5:
                return'\n5 White Balls and The PowerBall : 324,000,000 $'
            elif self.white == 4:
                return'\n4 White Balls and The PowerBall : 10,000 $'
            elif self.white == 3:
                return'\n3 White Balls and The PowerBall : 100 $'
            elif self.white == 2:
                return'\n2 White Balls and The PowerBall : 7 $'
            elif (self.white == 0) or (self.white == 1):
                return'\nYou Won Just a 4 $'
            else:
                return'\nTry Again'
        # first condition gold ball = 0
        if self.gold == 0:
            if self.white == 5:
                return'\n5 White Balls Without The PowerBall : 1,000,000 $'
            elif self.white == 4:
                return'\n4 White Balls Without The PowerBall : 100 $'
            elif self.white == 3:
                return'\n3 White Balls Without The PowerBall : 7 $'
            else:
                return'\nTry Again'
    # Print Function with The Messages:
    def __str__(self):
        return super().__str__() + str(self.prizes())
