import math

for x in range(3,10000000):
	total = 0

	for c in str(x):
		total = total + math.factorial(int(c))

	if total == x:
		print x
