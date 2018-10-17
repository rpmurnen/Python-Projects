# Number Guesser! in Python

import random


def Average(lst): 
    return sum(lst) / len(lst) 

def number_guess():


    all_game_guesses = []

    playing = True
    while playing == True: 
        target = random.randrange(1,100)
        # print(target)
        guesses = []
        guessing = True
        while guessing == True:
            
            guess = int(input('input your guess'))
            guesses.append(guess)
            if guess == target:
                all_game_guesses.append(len(guesses))
                print(f'you got it in {len(guesses)} guess(es)!')
                break
            if guess > target:
                print('too high!')
            elif guess < target:
                print('too low!')

        y = input('Play Again? y/n')
        if str.lower(y) in ('yes','y'):
            continue
        else:
            break
        
    print('Overall Results:')
    print(f'you played {len(all_game_guesses)} game(s)')
    print()
    print(f'your average guess count was {Average(all_game_guesses)} guess(es)')
    print()
    print(f'your best game was {min(all_game_guesses)} guess(es)')            

number_guess()

