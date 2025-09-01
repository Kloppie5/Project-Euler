
"""
    a^2 + b^2 = c^2
    a < b < c
    a + b + c = 1000
    -> a < 1000/3
    -> b < (1000-a)/2
"""

for a in range(1, 1000//3) :
    for b in range(a+1, (1000-a)//2) :
        c = 1000 - a - b
        a2pb2 = a**2 + b**2
        c2 = c**2
        print(f"{a} | {b} | {c} : {a2pb2} {c2}")
        if a2pb2 == c2 :
            print(a*b*c)
            exit(1)
