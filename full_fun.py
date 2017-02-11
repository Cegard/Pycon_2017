def generator_fizz_buzz(n):
	x = 0
	fizz = "Fizz"
	buzz = "Buzz"
	fizz_buzz = "{}{}".format(fizz, buzz)
	fizz_int = 3
	buzz_int = 5
	show_self = lambda result: result
	
	
	def get_from_if(expression, if_true_function, if_false_function,
					if_true_args, if_false_args):
		args = {True: if_true_args, False: if_false_args}
		functions = {True: if_true_function, False: if_false_function}
		
		return functions[expression](*args[expression])
	
	
	def get_answer(i, execute_if, show_function):
		is_fizz = i%fizz_int == 0
		is_buzz = i%buzz_int == 0
		args_for_true = [is_fizz, show_function, show_function,
						 [fizz_buzz], [buzz]]
		args_for_false = [is_fizz, show_function, show_function,
						  [fizz], [i]]
		result = execute_if(is_buzz, execute_if, execute_if,
							args_for_true, args_for_false)
		
		yield result
	
	
	def recursive(i, limit, execute_if, show_function):
		next_i = i+1
		is_in_limits = next_i < limit-1
		args_for_true = [next_i, limit, execute_if, show_function]
		args_for_false = [next_i, execute_if, show_function]
		
		yield from get_answer(i, execute_if, show_function)
		yield from execute_if(is_in_limits, recursive, get_answer,
							  args_for_true, args_for_false)
	
	
	yield from recursive(x, n, get_from_if, show_self)