outsider = "Outside"


def show_procedence():
	print ("\tI come from... {}".format(outsider))


show_procedence()


#non functional
n = 50


def non_functional_fizz_buzz():
	
	for x in range(n):
		
		if (x%5 == 0) and (x%3 == 0):
			print ("FizzBuzz")
		
		elif x%3 == 0:
			print ("Fizz")
		
		elif x%5 == 0:
			print ("Buzz")
		
		else:
			print (x)


#functional
def functional_fizz_buzz(n):
	result_list = []
	
	for x in range(n):
		result = x
		
		if (x%5 == 0) and (x%3 == 0):
			result = "FizzBuzz"
		
		elif x%3 == 0:
			result = "Fizz"
		
		elif x%5 == 0:
			result = "Buzz"
		
		result_list.append(result)
	
	return result_list


#optimized
def generator_fizz_buzz(n):
	x = 0
	
	while x < n:
		result = x
		
		if (x%5 == 0) and (x%3 == 0):
			result = "FizzBuzz"
		
		elif x%3 == 0:
			result = "Fizz"
		
		elif x%5 == 0:
			result = "Buzz"
		
		yield result
		x += 1


#functions can go anywhere
def outer_fizz_buzz(n):
	x = 0
	
	
	def get_module(x, mod):
		
		return x%mod
	
	
	while x < n:
		result = x
		mod_five = get_module(x, 5)
		mod_three = get_module(x, 3)
		
		if mod_five == 0 and mod_three == 0:
			result = "FizzBuzz"
		
		elif mod_three == 0:
			result = "Fizz"
		
		elif mod_five == 0:
			result = "Buzz"
		
		yield result
		x += 1


def get_module(module):
	
	
	#clousure
	def is_multiple(x):
		
		return x%module == 0
	
	
	return is_multiple


#functions can go anywhere
def outer_fizz_buzz(n, module_function):
	x = 0
	module_five = module_function(5)
	module_three = module_function(3)
	
	while x < n:
		result = x
		
		if mod_five(x) and mod_three(x):
			result = "FizzBuzz"
		
		elif mod_three(x):
			result = "Fizz"
		
		elif mod_five(x):
			result = "Buzz"
		
		yield result
		x += 1


def outer_fizz_buzz(n):
	x = 0
	
	
	def module_function (module):
		# lambda expressions
		result_function = lambda x: x%module == 0
		
		return result_function
	
	
	module_five = module_function(5)
	module_three = module_function(3)
	
	while x < n:
		result = x
		
		if mod_five(x) and mod_three(x):
			result = "FizzBuzz"
		
		elif mod_three(x):
			result = "Fizz"
		
		elif mod_five(x):
			result = "Buzz"
		
		yield result
		x += 1