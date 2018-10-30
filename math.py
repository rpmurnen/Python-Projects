# this file contains the answers to various problems

#11111111111111111111111111111111111111111111111111111111111111111111111111111
# calculate the sum of all numbers divisible y 3 or 5, from 0 to 1000

# def multiples_3_5():
# 	number_list = list(range(1000))
# 	sum_list = []
# 	for x in number_list:
# 		if x % 3 == 0 or x % 5 == 0:
# 			sum_list.append(x)
# 		else:
# 			continue
# 	print(sum_list)
# 	print(sum(sum_list))

# multiples_3_5()


#22222222222222222222222222222222222222222222222222222222222222222222222222222
# fibonacci set

# def fib(x):
# 	fib_set = []
# 	even_set = []
# 	fib_set.append(x)
# 	while max(fib_set) < 4000000:
# 		if len(fib_set) == 1:
# 			y = fib_set[-1]	
# 		else:
# 			y = fib_set[-1] + fib_set[-2]
# 		fib_set.append(y)

# 	for i in fib_set:
# 		if i % 2 == 0:
# 			even_set.append(i)
# 		else:
# 			pass
# 	print(sum(even_set))

# fib(1)


# def fibv2():
# 	x = 1











# 3333333333333333333333333333333333333333333
#largest prime number

# def is_prime(x):
# 	divisors = []
# 	numbers = list(range(1,x+1))
# 	for i in numbers:
# 		if x%i == 0:
# 			divisors.append(i)
# 	if len(divisors) == 2:
# 		return True
# 	else:
# 		return False
# # is_prime(100)


# def largest_prime(x,y):	
# 	primes = []
# 	divisors = []
# 	checklist = list(range(1,x))
# 	for i in checklist:
# 		if y%i==0:
# 			divisors.append(i)
# 		else:
# 			pass
# 	for i in divisors:
# 		if is_prime(i) == True:
# 			primes.append(i)
# 		else:
# 			pass

# 	print(max(primes))

# largest_prime(10000,600851475143)



# 444444444444444444444444444444444444444444444444444444444444444444444444444
#palindrome numbers

# from itertools import product

# def palindrome():

# 	answers=[]

# 	number1 = list(range(100,1000))
# 	number2 = list(range(100,1000))

# 	products = [x*y for x,y in product(number1,number2)]
# 	# products=[]

# 	# for a in number1:
# 		# products.append(a*b in number2)

# 	for i in products:
# 		if list(str(i)) == list(reversed(list(str(i)))):
# 			answers.append(i)
# 		else:
# 			continue

# 	print(answers)
# 	print(max(answers))
# palindrome()


#55555555555555555555555555555555555555555555555555555555555555555555555555555
#smallest number divisible by 1 through 20

# def problem_5(x):
# 	answers = []
# 	smallest=1000000000000000000000000000000000000000000000000
# 	for a in range(1,1000000000):
# 		for b in range(1,x+1):
# 			if a%b==0:
# 				answers.append(a)
# 				if len(answers)>x+1 and answers[-1] == answers[-x]:
# 					if answers[-1]>smallest:
# 						break
# 					else:
# 						smallest = answers[-1]
# 						print(smallest)	
# 				else:
# 					continue
# problem_5(20)



# 6666666666666666666666666666666666666666666666666666666666666666666666666666
#sum of square numbers

# def sum_squares(x):
# 	set1=[]

# 	while x <=100:
# 		set1.append(x**2)
# 		x+=1
# 	return sum(set1)

# def square_sum(x):
# 	set1=[]

# 	while x <=100:
# 		set1.append(x)
# 		x+=1
# 	return sum(set1)**2

# print(square_sum(1)-sum_squares(1))

# 777777777777777777777777777777777777777777777777777777777777777777777777777
# this script is slow af

# def is_prime(x):
# 	divisors = []
# 	numbers = list(range(1,x+1))
# 	for i in numbers:
# 		if x%i == 0:
# 			divisors.append(i)
	
# 	if len(divisors) == 2:
# 		# print('True')
# 		return True
		
# 	elif len(divisors) ==1:
# 		return False
# 	else:
# 		# print('False')
# 		return False
		

# def prime_list_maker():
# 	primes_list=[]
# 	i=1
# 	while len(primes_list) <10100:
# 		if is_prime(i) is True:
# 			primes_list.append(i)
# 		i+=1
# 	# 	print(i)
# 	# print(primes_list)
# 	print(primes_list[10001])

# prime_list_maker()

# 88888888888888888888888888888888888888888888888888888888888888888888888888888888

# from itertools import izip_longest

# number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
# number_list = list(str(number))
# number_list2 = []
# answers = []

# for i in number_list:
# 	number_list2.append(int(i))


# print(list(zip(*[iter(number_list2)]*4)))

# for a,b,c,d in zip(*[iter(number_list2)]*4):
# 	answers.append(a*b*c*d)

# print(max(answers))

# 99999999999999999999999999999999999999999999999999999999999999999999999999999999
# pythagorean triplets

# def pythagorean(t,g,guess):

# 	import itertools

# 	# g=500

# 	possible_c = list(range(guess,g))
# 	possible_b = list(range(guess,g-1))
# 	possible_a = list(range(guess,g-2))

# 	combinations = set(itertools.product(possible_a,possible_b,possible_c))
# 	# print(combinations)
# 	for x in combinations:
# 		if x[0] < x[1] < x[2] and x[0]**2 + x[1]**2 == x[2]**2 and x[0]+x[1]+x[2]==t:
# 			print(x[0]*x[1]*x[2])

# pythagorean(1000,500,100)

	
# 10101010101010101010101010101010101010101010101010101010101010101010101010101010


# def is_prime(x):
# 	divisors = []
# 	numbers = list(range(1,x+1))
# 	for i in numbers:
# 		if x%i == 0:
# 			divisors.append(i)
# 	# print(divisors)
# 	if i ==1:
# 		return False
# 	elif len(divisors) == 2:
# 		# print('True')
# 		return True
# 	else:
# 		return False
# is_prime(2000000)

# def is_prime2(x):
# 	divisors = []
# 	numbers = list(range(1,x+1))
# 	for i in numbers:
# 		if x%i == 0:
# 			divisors.append(i)
# 	# print(divisors)
# 	if i ==1:
# 		return False
# 	elif len(divisors) == 2:
# 		# print('True')
# 		return True
# 	else:
# 		return False
# # is_prime2(2000000)


# def sum_prime(x,y):
# 	largest = 0
# 	i = 2
# 	while i <= y and i >= x:
# 		if is_prime(i) == True:
# 			largest += i
# 		i +=1
# 	print(largest)	
# sum_prime(1,2000000)


# def largest_number(x):
# 	i=1
# 	largest = None
# 	while i <= x:
# 		if i % 3 == 0:
# 			largest = i
# 		i+=1
# 	print(largest)
# largest_number(100000000)


# 121212121212121212121212121212121212121212121212121212121212121212121212

# highly divisible triangular number

def triangle(x):
	i = 0
	largest = 0
	divisors = []
	while i < x:
		i+=1
		largest += i
	print(largest)
	for j in range(1,largest+1):
		if largest % j==0:
			divisors.append(j)
	print(len(divisors))

triangle(7)



def triangle():
	i = 0
	j = 1
	largest = 0
	divisors = []
	while i < 7:
		i+=1
		largest += i
		for j in range(1,largest+1):
			if largest % j==0:
				divisors.append(j)
			print(len(divisors))

triangle()


# for a in range()



#  def problem_5(x):
# 	answers = []
# 	smallest=100000000000000000000000
# 	for a in range(1,1000000000):
# 		for b in range(1,x+1):
# 			if a%b==0:
# 				answers.append(a)
# 				if len(answers)>x+1 and answers[-1] == answers[-x]:
# 					if answers[-1]>smallest:
# 						break
# 					else:
# 						smallest = answers[-1]
# 						print(smallest)	
# 				else:
# 					continue
# problem_5(20)









