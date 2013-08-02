def is_palin(i):
	return str(i)[::-1] == str(i)

def is_lychrel(i):
	total = i

	for x in range(1,51):
		total_reverse = str(total)[::-1]
		total = total + int(total_reverse)
		if is_palin(total):
			return True

	return False

total = 0

for x in range(1,10001):
	if not is_lychrel(x):
		total = total + 1

print "Total: " + str(total)
