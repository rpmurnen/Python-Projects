# Dice rolling Simulator!

import random


def diceroll():
    x = input('ready to roll? y/n')
    if str.lower(x) in ('yes','y'):
        rolling = True
        while rolling == True:
            roll = random.randint(1,6)
            if roll == 1:
                print('1, that stinks')
            else:
                print(roll)
            y = input('Roll Again? y/n')
            if str.lower(y) not in ('yes','y'):
                rolling = False
            
diceroll()

