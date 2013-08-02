def get_pentagons():
	pentagons = []

	for x in range(1,10001):
		pentagons.append((x * (3*x -1)) / 2)

	return pentagons

pentagons = get_pentagons()

print "done generating..." + str(len(pentagons))

for i in pentagons:
	for j in pentagons:
		sum = i + j
		diff = j - i
		if sum in pentagons:
			if diff in pentagons:
				print str(i) + "," + str(j)

