def is_pan(i):
	return len(i) == 9 and len(i) == len(set(i)) and not "0" in i

for x in range(1, 10000):
	for y in range(1,10):
		total = x * y
		if is_pan(str(total) + str(x) + str(y)):
			print str(total) + " = " + str(x) + "*" + str(y)
		
for x in range(1, 1000):
	for y in range(1, 100):
		total = x * y
		if is_pan(str(total) + str(x) + str(y)):
			print str(total) + " = " + str(x) + "*" + str(y)

for x in range(1, 100):
        for y in range(1, 1000):
                total = x * y
                if is_pan(str(total) + str(x) + str(y)):
                        print str(total) + " = " + str(x) + "*" + str(y)

for x in range(1, 10):
        for y in range(1, 10000):
                total = x * y
                if is_pan(str(total) + str(x) + str(y)):
                        print str(total) + " = " + str(x) + "*" + str(y)
