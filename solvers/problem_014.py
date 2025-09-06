
collatz_cache = {1 : 1}

def collatz(n) :
    global collatz_cache
    if n not in collatz_cache :
        if n % 2 == 0 :
            nn = n//2
        else :
            nn = 3*n + 1
        next_step = collatz(nn)
        collatz_cache[n] = next_step + 1
    return collatz_cache[n]

for i in range(1, 1000000) :
    collatz(i)

max_steps = max(collatz_cache.values())
max_steps_start = [n for n in collatz_cache if collatz_cache[n] == max_steps]
print(f"{max_steps_start} : {max_steps}")