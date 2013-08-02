def get_triangles():
	nums = []

	for x in range(1,1000001):
		nums.append((x * (x + 1)) / 2)

	return nums

def get_pentagons():
	nums = []

	for x in range(1,1000001):
		nums.append((x * (3*x - 1)) / 2)

	return nums

def get_hexagons():
	nums = []

	for x in range(1,1000001):
		nums.append(x * (2*x - 1))

	return nums


triangles = get_triangles()
pentagons = get_pentagons()
hexagons = get_hexagons()

for triangle in triangles:
	if triangle in pentagons and triangle in hexagons:
		print triangle
