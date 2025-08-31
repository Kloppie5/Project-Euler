import math
"""
    Prime factorization

    Going over all* the numbers up to the root of the number to build a list of prime numbers first sounds very slow; though I will likely need prime numbers quite often, so maybe I should just slowly build up a nice prime number lookup for generic use later.

    To shorten the search, the goal should be moved closer whenever a factor is found.

    * skipping all non-2 even numbers
"""

target_number = 600851475143
target_primes = []
lim = math.sqrt(target_number)

prime_numbers = [2]
i = 3
while i < lim :
    if all(i % p != 0 for p in prime_numbers) :
        prime_numbers.append(i)
        if target_number % i == 0 :
            target_primes.append(i)
            target_number //= i
            lim = math.sqrt(target_number)
    i += 2
if target_number != 1 :
    target_primes.append(target_number)

print(target_primes)
print(f"Largest factor being {max(target_primes)}")