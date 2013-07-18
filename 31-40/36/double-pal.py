sum = 0

for x in range(1,1000000):
	n = str(x)
	b = str(bin(x)).replace('0b', '')

	if b == b[::-1] and n == n[::-1]:
		print str(x) + " = double palindrome"
		sum = sum + x

print sum
