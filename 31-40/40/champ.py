s = ""

for x in range(1,1000001):
	s = s + str(x)

print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999])
