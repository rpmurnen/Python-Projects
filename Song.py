# song.py

def intro():
	print('I don\'t know why she swallowed that fly,')
	print('Perhaps she\'ll die.')

def woman(animal):
	print(f'there was an old woman who swallowed a {animal}')

def swallowed(animal1, animal2):
	(f'she swallowed the {animal1} to catch the {animal2}')

def song():

	fly = 'I don\'t know why she swallowed that fly,'
	die = 'Perhaps she\'ll die.'
	spider1 = 'There was an old woman who swallowed a spider,'
	spider2 = 'That wriggled and iggled and jiggled inside her.'
	spider3 = 'She swallowed the spider to catch the fly,'
	bird1 = 'There was an old woman who swallowed a bird,'
	bird2 = 'how absurd to swallow a bird'
	bird3 = 'She swallowed the bird to catch the spider,'
	cat1 = 'There was an old woman who swallowed a cat,'
	cat2 = 'Imagine that to swallow a cat.'
	cat3 = 'She swallowed the cat to catch the bird,'
	dog1 = 'There was an old woman who swallowed a dog,'
	dog2 = 'What a hog to swallow a dog.'
	dog3 = 'She swallowed the dog to catch the cat,'

	
	first_lines = ['spider','bird','cat','dog']
	# verses = [spider1,spider2,spider3,bird1,bird2,bird3,cat1,cat2,cat3,dog1,dog2,dog3]
	verses1 = [spider2,spider3]
	verses2 = [bird2,bird3]
	verses3 = [cat2,cat3]
	verses4 = [dog2,dog3]

	stacked = []

	print('There was an old woman who swallowed a fly.')
	# y = 0
	# while y <5:
	for i in first_lines:
		intro()
		woman(i)
		if i == 'spider':
			for c in verses1:
				print(c)
				stacked.append(verses1[-1])
				# stacked.append(swallowed('spider','dog'))	
				# print(stacked)
		elif i == 'bird':
			for c in verses2:
				print(c)
				stacked.append(verses2[-1])
				# print(stacked)
			print(verses1[-1])
		elif i == 'cat':
			for c in verses3:
				print(c)
				stacked.append(verses3[-1])
				# print(stacked)
			print(verses2[-1])
			print(verses1[-1])
		elif i == 'dog':
			for c in verses4:
				print(c)
				stacked.append(verses4[-1])
			print(verses3[-1])
			print(verses2[-1])
			print(verses1[-1])
			intro()
				# print(stacked)
		else:
			return intro()
		
song()
		
