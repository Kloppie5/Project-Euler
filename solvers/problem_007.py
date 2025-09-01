
prime_numbers = [2]
i = 3
while len(prime_numbers) < 10001 :
    if all(i % p != 0 for p in prime_numbers) :
        print(f"{len(prime_numbers)+1}: {i}")
        prime_numbers.append(i)
    i += 1

print(prime_numbers[10000])