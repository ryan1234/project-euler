with open("unique-sums.txt", "r") as f:
	data = f.read()
	sums = data.split('\n')
	sums = filter(None, sums)
	sums = [int(sum) for sum in sums]

	total = 0

	for x in range(1,28123):
		if not (x in sums):
			total = total + x

	print total
