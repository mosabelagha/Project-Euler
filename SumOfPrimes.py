__author__ = 'Administrator'

def primes(n):
    result, sieve = [], [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            result.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return result

from time import time
s = time()
print sum(primes(2000000))
print "time", time()-s