num1 = 1
num2 = 1

for x in range(1,1000000):
	temp = num1 + num2
	num1 = num2
	num2 = temp
	
	if len(str(num2)) == 1000:
		print x + 2
