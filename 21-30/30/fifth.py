answer = 0

for x in range(2, 1000001):
	num = str(x)

	sum = 0;
	for c in num:
		sum = sum + (pow(ord(c) - 48, 5))

	if (sum == x):
		print x
		answer = answer + x

print answer
