from itertools import permutations

perms = [''.join(p) for p in permutations("0123456789")]

total = 0

for p in perms:
	perm = str(p)	
	num1 = int(perm[1:4]) # 2,3,4
	num2 = int(perm[2:5]) # 3,4,5
	num3 = int(perm[3:6])
	num4 = int(perm[4:7])
	num5 = int(perm[5:8])
	num6 = int(perm[6:9])
	num7 = int(perm[7:10])

	if num1 % 2 == 0 and num2 % 3 == 0 and num3 % 5 == 0 and num4 % 7 == 0 and num5 % 11 == 0 and num6 % 13 == 0 and num7 % 17 == 0:
		print perm
		total = total + long(perm)

print total
