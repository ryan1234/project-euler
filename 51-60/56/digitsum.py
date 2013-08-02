max = 0

for a in range(1,101):
	for b in range(1,101):
		num = pow(a,b)
		sum = 0

		for c in str(num):
			sum = sum + (ord(c) - 48)

		if sum > max:
			max = sum

print max		
