
def proper_divisors(n : int) -> set[int] :
    divisors = set()
    divisors.add(1)
    for i in range(2, int(n**0.5)) :
        if n % i == 0 :
            divisors.add(i)
            divisors.add(n//i)
    return divisors

r = 0
for i in range(1, 10001) :
    s = sum(proper_divisors(i))
    if s > i :
        si = sum(proper_divisors(s))
        if i == si :
            r += i + s
print(r)





