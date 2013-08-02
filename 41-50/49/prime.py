import numpy as np

def is_perm(a,b):
	return sorted(str(a)) == sorted(str(b))

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

primes = primesfrom2to(10000)

for prime in primes:
	if is_perm(prime, prime + 3330) and (prime + 3330) in primes and is_perm(prime, prime + 6660) and (prime + 6660) in primes:
		print prime

print "2969" + "6299" + "9629"	
