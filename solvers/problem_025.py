
fibonacci_cache = {
    1 : 1,
    2 : 2,
}

def fibonacci(n:int):
    global fibonacci_cache
    if n not in fibonacci_cache:
        fibonacci_cache[n] = fibonacci(n-2) + fibonacci(n-1)
    return fibonacci_cache[n]

fibonaccis = []
for i in range(1,10000):
    fib = fibonacci(i)
    fibonaccis.append(fib)
    if fib > 10**999-1:
        break

print(len(fibonaccis)+1)
