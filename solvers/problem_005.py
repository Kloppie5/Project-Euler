import math

"""
    For a number to be evenly divisible by a whole bunch of numbers, it has to have all the prime factors
"""

target = 20

prime_numbers_below_target = [2]
for i in range(3, target+1, 2) :
    if all(i % p != 0 for p in prime_numbers_below_target) :
        prime_numbers_below_target.append(i)

def prime_factors(number) :
    factors = {}
    while number > 1 :
        divisors = [prime for prime in prime_numbers_below_target if number % prime == 0]
        for divisor in divisors :
            if divisor in factors :
                factors[divisor] += 1
            else :
                factors[divisor] = 1
        number //= divisor
    return factors

total_factors = {}
for i in range(2, target+1) :
    factors = prime_factors(i)
    for factor in factors :
        if factor in total_factors :
            total_factors[factor] = max(total_factors[factor], factors[factor])
        else :
            total_factors[factor] = factors[factor]

total = 1
for factor in total_factors :
    total *= factor ** total_factors[factor]
print(total)