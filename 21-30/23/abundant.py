with open("abundant.txt", "r") as f:
	data = f.read()
	nums = data.split('\n')

	sums = []

	for num1 in nums:
		for num2 in nums:
			if not (num1 == '' or num2 == ''):
				print long(num1) + long(num2)

