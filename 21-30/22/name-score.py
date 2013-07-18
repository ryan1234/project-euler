with open("names.txt", "r") as f:
	data = f.read().replace('\n', '')
	names = data.split(',')
	names.sort()
	
	total = 0

	for index, name in enumerate(names):
		clean_name = name.replace('"', '')
		
		score = 0;

		for c in clean_name:
			score = score + (ord(c) - 64)

		total = total + (score * (index + 1))

	print total
				 
