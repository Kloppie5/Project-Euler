
"""
    The sum is n(1+1)/2, and the sum of squares is n(n+1)(2n+1)/6, so this is a simple calculation
"""

n = 100

sum_of_squares = n*(n+1)*(2*n+1)//6
square_of_sum = (n*(n+1)//2)**2

diff = abs(sum_of_squares - square_of_sum)

print(diff)
