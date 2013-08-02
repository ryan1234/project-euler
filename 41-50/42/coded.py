def get_string_value(s):
	sum = 0

	for c in s:
		sum = sum + (ord(c) - 64)
		
	return sum * 1.0

def get_triangle_numbers(n):
	nums = []

	for x in range(1,n):
		num = (0.5 * x) * (x + 1)
		nums.append(num)

	return nums

triangles = get_triangle_numbers(1000000)
wc = 0

with open ("words.txt", "r") as myfile:
	data = myfile.read().split(',')
	for d in data:
		str_value = get_string_value(d.replace('"', ''))
		
		if d.replace('"', '') == "SKY":
			print str_value

		if str_value in triangles:
			wc = wc + 1

print wc			
