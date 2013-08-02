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

primes = primesfrom2to(1000)

print "generated primes"

candidates = []

for x in range(1,10001):
	for prime in primes:
		candidates.append(prime + (2 * pow(x,2)))

print "generated candidates"

for x in range(1,10001):
	if x % 2 == 1 and not x in primes:
		if not x in candidates:
			print x
