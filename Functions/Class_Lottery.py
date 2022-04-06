import random
from Functions.Class_Game import Game

class Lottery(Game):
    def __init__(self, player='Israel Israeli', ID=123456):
        super().__init__(player, ID)

    def lucky_numbers(self):
        value = []
        for i in range(5):
            num = random.randint(1, 20)
            while num in value:
                num = random.randint(1, 20)
            value.append(num)
        new_value = sorted(value)

        gold_num = random.randint(1, 10)
        new_value.append(gold_num)
        return new_value

    def user_number(self):
        value2 = []
        for i in range(5):
            num1 = random.randint(1, 20)
            while num1 in value2:
                num1 = random.randint(1, 20)
            value2.append(num1)
        new_value2 = sorted(value2)

        gold_num1 = random.randint(1, 10)
        new_value2.append(gold_num1)
        return new_value2

    def is_match_white(self):
        counter_white = 0
        counter_gold = 0
        luck_number = Lottery().lucky_numbers()
        user_number = Lottery().user_number()
        new_luck_number = luck_number[0:5]
        new_user_number = user_number[0:5]
        for i in new_luck_number:
            for j in new_user_number:
                if i == j:
                    counter_white += 1
        if luck_number[-1] == user_number[-1]:
            counter_gold += 1
        print('Today Lucky Numbers:\n')
        print(luck_number)
        print('\nYour Numbers:\n')
        print(user_number)
        print('----------------------')
        return counter_white, counter_gold
