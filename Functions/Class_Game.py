# Create a Class called Game with The Attributes:
class Game:
    def __init__(self, player='Israel Israeli', ID=123456):
        self.player = player
        self.ID = ID
# Get And Set For All The Attributes:
    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = player

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    # Print Function
    def __str__(self):
        return '------------------------'+'\nName:' + ' ' + self.player + '  ' + '\nID:' + ' ' + str(self.ID) +\
               '\n------------------------'

