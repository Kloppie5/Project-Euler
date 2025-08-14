
"""
    n_1 = 1
    n_2 = 2
    n_i = n_{i-1} + n_{i-2}
"""

fibonacci_cache = {
    1 : 1,
    2 : 2,
}

def fibonacci(n:int):
    global fibonacci_cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    return fibonacci(n-2) + fibonacci(n-1)

fibonaccis = []
for i in range(1,100):
    fib = fibonacci(i)
    if fib > 4000000:
        break
    fibonaccis.append(fib)

print(sum([fib for fib in fibonaccis if fib % 2 == 0]))


