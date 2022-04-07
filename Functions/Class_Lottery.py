import random
import colorama
from Functions.Class_Game import Game
# Create a Lottery Class where all calculations will be like: get Random Numbers and The Compare:

# This Class inheritance from The last Class 'Game':
class Lottery(Game):
    def __init__(self, player='Israel Israeli', ID=123456):
        super().__init__(player, ID)

# This Method Give us The Random Numbers:
    def lucky_numbers(self):
        # Empty List
        value = []
        # Run Over 5 times on Random numbers in range 1 - 20:
        for i in range(5):
            num = random.randint(1, 20)
            # while Loop checking if the 5 Numbers are The Same:
            while num in value:
                # If The 5 Numbers The same we'll add a new number that doesn't appear.
                num = random.randint(1, 20)
            # Add The 5 Numbers To The List:
            value.append(num)
        # Arrange the numbers in ascending order
        new_value = sorted(value)

        # Now I do the Same Thing For the Gold Ball
        gold_num = random.randint(1, 10)
        # Add the Gold Number To the List Above
        new_value.append(gold_num)
        return new_value

# This Method Gives us The Second List Of Random Numbers:
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

# This Method Compare Between The 2 Lists:
    def is_match(self):
        # 2 Counters One For The White, And one For The Gold:
        counter_white = 0
        counter_gold = 0
        # Create 2 New Variables and Use The methods above:
        luck_number = Lottery().lucky_numbers()
        user_number = Lottery().user_number()
        # Create  2 lists with The 5 Numbers:
        new_luck_number = luck_number[0:5]
        new_user_number = user_number[0:5]
        # Run On loop  The Lists with The 5 numbers:
        for i in new_luck_number:
            for j in new_user_number:
                # Compare Between The Iterators :
                if i == j:
                    # If The Iterators are The Same , The Counter increases by 1:
                    counter_white += 1

        # Return To The 2 Lists with The 6 Numbers:
        # Compare Between The Last Value in The Lists:
        if luck_number[-1] == user_number[-1]:
            # Counter increases by 1:
            counter_gold += 1
        # Print Message:
        print('\nToday Lucky Numbers:')
        print('-----------------------')
        # using in colorama Library for the colors:
        print(colorama.Fore.BLUE, luck_number[0:5], colorama.Style.RESET_ALL, colorama.Fore.YELLOW,
              luck_number[-1], colorama.Style.RESET_ALL)
        print('-----------------------')
        print('\nYour Numbers:')
        print('-----------------------')
        print(colorama.Fore.BLUE, user_number[0:5], colorama.Style.RESET_ALL, colorama.Fore.YELLOW,
              user_number[-1], colorama.Style.RESET_ALL)
        print('-----------------------')
        # Return The counters.
        return counter_white, counter_gold
    # print Function:
    def __str__(self):
        return super().__str__()

