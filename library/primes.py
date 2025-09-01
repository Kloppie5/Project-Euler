

odd_numbers_which_are_prime = [False]

def find_prime_numbers_below(n) :
    global odd_numbers_which_are_prime

    old_odd_numbers_which_are_prime = odd_numbers_which_are_prime
    n_old = len(old_odd_numbers_which_are_prime)
    odd_numbers_which_are_prime = [True] * (n//2)
    odd_numbers_which_are_prime[:n_old] = old_odd_numbers_which_are_prime

    for i in range(3, int(n**0.5)+1, 2):
        if odd_numbers_which_are_prime[i//2]:
            odd_numbers_which_are_prime[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
def get_prime_numbers_below(n) :
    global odd_numbers_which_are_prime
    return [2] + [2*i+1 for i in range(1, n//2) if odd_numbers_which_are_prime[i]]
