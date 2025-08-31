
"""
    A palindromic number

    The largest palindrome made as a product of two 3-digit numbers is most likely 6-digit.
    To be palindromic, it should hold that n % 100001 % 10010 % 1100 = 0
"""

candidates = []
for l in range(999, 99, -1) :
    for r in range(999, l-1, -1) :
        n = l * r
        if n % 100001 % 10010 % 1100 == 0 :
            candidates.append((l, r, n))
(l, r, n) = max(candidates, key=lambda a: a[2])
print(f"{l} * {r} = {n}")