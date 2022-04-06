
class Game:
    def __init__(self, player='Israel Israeli', ID=123456):
        self.player = player
        self.ID = ID

    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = player

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def __str__(self):
        return self.player + ' : ' + str(self.ID)
