import math

odd_numbers_which_are_prime = [False]
found_below = 0

def find_prime_numbers_below(n : int) :
    global odd_numbers_which_are_prime
    global found_below

    if found_below >= n :
        return

    old_odd_numbers_which_are_prime = odd_numbers_which_are_prime
    n_old = len(old_odd_numbers_which_are_prime)
    odd_numbers_which_are_prime = [True] * (n//2)
    odd_numbers_which_are_prime[:n_old] = old_odd_numbers_which_are_prime

    for i in range(3, int(n**0.5)+1, 2):
        if odd_numbers_which_are_prime[i//2]:
            odd_numbers_which_are_prime[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    found_below = n

def get_prime_numbers_below(n : int) :
    global odd_numbers_which_are_prime
    return [2] + [2*i+1 for i in range(1, n//2) if odd_numbers_which_are_prime[i]]

def prime_factors(number) :
    factors = {}
    find_prime_numbers_below(number+2)
    primes_below_number = get_prime_numbers_below(number+2)
    while number > 1 :
        divisors = [prime for prime in primes_below_number if number % prime == 0]
        # print(f"{number}: {divisors}")
        if len(divisors) == 0 :
            exit(1)
        for divisor in divisors :
            if divisor in factors :
                factors[divisor] += 1
            else :
                factors[divisor] = 1
            number //= divisor
    return factors