
factorial_cache = {0: 1}
def factorial(n) :
    if n not in factorial_cache :
        factorial_cache[n] = n * factorial(n-1)
    return factorial_cache[n]

def n_choose_k(n, k) :
    return factorial(n) // factorial(k) // factorial(n-k)

print(n_choose_k(40, 20))