import random

def dice_roll(sides=6):
	print(num_rolled = random.randint(1,6))
	return num_rolled

def game():
	rolling=True
	while rolling:
		roll_again = input("Ready_to_Roll?")
		num_rolled = dice_roll(sides)
		print("you_rolled_a",num_rolled)

print ("Roll_Again?")

