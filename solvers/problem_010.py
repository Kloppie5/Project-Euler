import os
import sys
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__))+'/../')

from library import primes

primes.find_prime_numbers_below(2000000)

print(sum(primes.get_prime_numbers_below(2000000)))
