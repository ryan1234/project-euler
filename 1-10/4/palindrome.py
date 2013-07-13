largest = 0

for x in range(100, 999):
	for y in range(100, 999):
		s = str(x * y)
		if (x * y > largest and s[::-1] == s):
			largest = x * y

print largest
