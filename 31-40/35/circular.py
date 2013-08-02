import numpy as np

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def getCircularShifts(s):
	strings = []
	temp = s

	i = 0

	while (i < len(s)):
		temp = temp[1:] + temp[0]
		strings.append(int(temp))
		i = i + 1

	return strings


primes = primesfrom2to(1000000)

total = 0

for x in primes:
	shifts = getCircularShifts(str(x))

	count = 0

	for shift in shifts:
		if shift in primes:
			count = count + 1	

	if count == len(shifts):
		print x
		total = total + 1

print total
