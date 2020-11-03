def summ(args):
	if isinstance(args, (int, float)):
		return args
	elif isinstance(args, (dict, str)):
		return "Invalid Input"	
	
	total = 0
	try:
		for value in args:
			total += value
		return total
	except TypeError:
		return "Invalid Input"

testing_set = [[15,'me'], {"a":58, "b":9}, 10, [78, 899, 67264], (537, 4823, 49732), 972.5, [121.12, 232.2, 898.7, 87], "COEP"]
	
check = 1

for each_case in testing_set:
	print("Testing for ", each_case)
	if isinstance(each_case, int) or isinstance(each_case, float):
		s = each_case
	else:
		try:
			s = sum(each_case)
		except TypeError:
			s = "Invalid Input"
	
	assert summ(each_case) == s, "Condition failed"
	print("Condition{} OK\n". format(check))
	check = check + 1
	

