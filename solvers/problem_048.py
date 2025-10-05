
r = 0

for i in range(1, 1001) :
    v = i**i % (10**10)
    r = (r + v) % (10**10)

print(r)