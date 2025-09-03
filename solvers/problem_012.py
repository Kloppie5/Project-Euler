import os
import sys
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__))+'/../')

import math
from library import primes

prime_factors_cache = {}
def prime_factors_with_cache(n):
    global prime_factors_cache
    if n not in prime_factors_cache :
        prime_factors_cache[n] = primes.prime_factors(n)
    return prime_factors_cache[n]
def combine_prime_factors(l, r):
    return {k : (l[k] if k in l else 0) + (r[k] if k in r else 0) for k in set(l).union(set(r))}

for i in range(3, 100000) :
    if i % 2 == 0 :
        tn = (i+1) * i//2
        factors = combine_prime_factors(prime_factors_with_cache(i+1), prime_factors_with_cache(i//2))
    else :
        tn = i * (i+1)//2
        factors = combine_prime_factors(prime_factors_with_cache(i), prime_factors_with_cache((i+1)//2))

    divisor_count = math.prod([f+1 for f in factors.values()])
    print(f"{i:3}: {tn} | {factors} | {divisor_count}")
    if divisor_count > 500 :
        exit(1)