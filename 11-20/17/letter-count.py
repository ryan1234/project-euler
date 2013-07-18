words = {
	0 : '',
	1 : 'one',
	2 : 'two',
	3 : 'three',
	4 : 'four',
	5 : 'five',
	6 : 'six',
	7 : 'seven',
	8 : 'eight',
	9 : 'nine',
	10 : 'ten',
	11 : 'eleven',
	12 : 'twelve',
	13 : 'thirteen',
	14 : 'fourteen',
	15 : 'fifteen',
	16 : 'sixteen',
	17 : 'seventeen',
	18 : 'eighteen',
	19 : 'nineteen',
	20 : 'twenty',
	30 : 'thirty',
	40 : 'forty',
	50 : 'fifty',
	60 : 'sixty',
	70 : 'seventy',
	80 : 'eighty',
	90 : 'ninety'
}

letters = 0

for x in range(1, 1001):
	num = str(x)

	if len(num) == 1:
		ones = ord(num[0]) - 48

		print str(x) + ": " + words[ones]
		letters = letters + len(words[ones])

	if len(num) == 2:
		if x >= 10 and x <= 19:
			print str(x) + ": " + str(words[x])
			letters = letters + len(words[x])
		else:
			tens = (ord(num[0]) - 48) * 10
			ones = ord(num[1]) - 48

			print str(x) + ": " + words[tens] + " " + words[ones]
			letters = letters + len(words[tens])
			letters = letters + len(words[ones])
	
	if len(num) == 3:
		hundreds = ord(num[0]) - 48
		tens = ord(num[1]) - 48
		ones = ord(num[2]) - 48

                if x % 100 == 0:
                        print str(x) + ": " + words[hundreds] + " hundred"
			letters = letters + len(words[hundreds])
			letters = letters + len("hundred")
		else:
                        if tens == 0 and ones > 0:
                                print str(x) + ": " + words[hundreds] + " hundred and " + words[ones]
				letters = letters + len(words[hundreds]) 
				letters = letters + len(words[ones])
				letters = letters + len("hundredand")

			if tens == 1:
				newTens = (tens * 10) + ones

				print str(x) + ": " + words[hundreds] + " hundred and " + words[newTens]
				letters = letters + len(words[hundreds])
				letters = letters + len(words[newTens])
				letters = letters + len("hundredand")

			if tens > 1:
				tens = tens * 10

				print str(x) + ": " + words[hundreds] + " hundred and " + words[tens] + " " + words[ones]
				letters = letters + len(words[hundreds])
				letters = letters + len(words[tens])
				letters = letters + len(words[ones])
				letters = letters + len("hundredand")

	if len(num) == 4:
		letters = letters + len('onethousand')

print letters
