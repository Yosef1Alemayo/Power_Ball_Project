import random
from game import Game

class Lottery(Game):
    def __init__(self, name, age, start, end):
        super().__init__(name, age)
        self.start = start
        self.end = end
        self.user = self.user_balls()
        self.machine = self.machine_balls()
        self.white = 0
        self.gold = 0

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

    def random(self):
        nums = []
        for i in range(5):
            num = random.randint(self.start, self.end)
            while num in nums:
                num = random.randint(self.start, self.end)
            nums.append(num)
        new_list = sorted(nums)

        power_ball = random.randint(1, 10)
        new_list.append(power_ball)
        return new_list

    def user_balls(self):
        x = self.random()
        self.user = x
        return self.user

    def machine_balls(self):
        x = self.random()
        self.machine = x
        return self.machine

    def compare(self):
        machine = self.machine
        user = self.user
        new_user = user[0:5]
        new_machine = machine[0:5]
        for i in new_machine:
            for j in new_user:
                if i == j:
                    self.white += 1
        if machine[-1] == user[-1]:
            self.gold += 1
        return self.white, self.gold

    def __str__(self):
        return super().__str__() + f'\nToday Numbers:{str(self.machine_balls())}'\
               + f'\nYour Numbers:{str(self.user_balls())}'\
               + f'\nWhite & Gold Balls:{str(self.compare())}\n--------------------------------'
