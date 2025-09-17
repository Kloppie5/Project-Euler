factorial_cache = {0: 1}
def factorial(n) :
    if n not in factorial_cache :
        factorial_cache[n] = n * factorial(n-1)
    return factorial_cache[n]