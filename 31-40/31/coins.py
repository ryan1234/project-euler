count = 0

for one in range(0,201):
	for two in range(0,101):
		for five in range(0,41):
			for ten in range(0,21):
				for twenty in range(0,11):
					for fifty in range(0,5):
						for hundred in range(0,3):
							for twohundred in range(0,1):
								if (one + (two * 2) + (five * 5) + (ten * 10) + (twenty * 20) + (fifty * 50) + (hundred * 100) + (twohundred * 200)) == 200:
									count = count + 1

print count								 
