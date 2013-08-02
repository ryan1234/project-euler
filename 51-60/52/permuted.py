def is_perm(a,b):
	return sorted(str(a)) == sorted(str(b))

for x in range(1,1000001):
	num2 = 2*x
	num3 = 3*x
	num4 = 4*x
	num5 = 5*x
	num6 = 6*x

	if is_perm(x, num2) and is_perm(x, num3) and is_perm(x, num4) and is_perm(x, num5) and is_perm(x, num6):
		print x
