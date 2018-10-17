# Hangman

import random

# 
def hangman():

	playing = True
	while playing == True:

		wordlist = ['python','ideal','cobra','ghost']
		letterlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		targetword = str(random.choice(wordlist))
		num_letters = (len(targetword))
		# print(targetword)
		
		print('welcome to hangman')
		print()
		print('There are '+ str(num_letters) +' characters in the word!')
		print()

		

		i = 0
		incorrect_guesses = []
		correct_guesses = []
		previous_guesses = []
		
		while i < 10:
			

			if len(set(correct_guesses) & set(targetword)) == len(set(targetword)):
				# print()
				print(targetword)
				# print()		
				print('You win!')
				i=10
	

			elif len(set(correct_guesses) & set(targetword)) != len(set(targetword)):
				guess = input('please enter a letter')	
				checker = bool(guess in letterlist)				
				if guess not in previous_guesses:
					if checker == True:
						if guess in targetword:
							print('You got it!')
							i += 1
							previous_guesses.append(guess)
							correct_guesses.append(guess)
							print(f'correct guesses:  {correct_guesses}')
							print(f'incorrect guesses:  {incorrect_guesses}')
							# print(list(targetword))
							guesses_left = str(10 - i)
							print(guesses_left + ' guesses left!')
							
						elif guess not in targetword:
							print('Incorrect!!!')
							i += 1
							previous_guesses.append(guess)
							incorrect_guesses.append(guess)
							print(f'correct guesses:  {correct_guesses}')
							print(f'incorrect guesses:  {incorrect_guesses}')
							# print(previous_guesses)
							guesses_left = str(10 - i)
							print(guesses_left + ' guesses left!')
				
					else: 
						print('invalid guess, please try again')
				else: 
						print('you already guessed that letter, please try again')
			 
		y = input('Play again!?'' y/n')
		if str.lower(y) not in ('yes','y'):
			playing = False



hangman()
