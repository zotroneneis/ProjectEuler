"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3
"""

import numpy as np

# To determine if a number n is prime, we need to:
# 1. check whether n is evenly divisible by 2
# 2. check whether n is evenly divisible by one of the uneven numbers from 3 to sqrt(n) + 1
# 3. if neither 1 nor 2 apply, n is prime

# To find the largest prime factor of n, we repeatedly divide n by its smallest prime factor
# until we can't divide it further.

def find_smallest_prime_factor(number):
    upper_bound = int(np.sqrt(number)) + 1

    for i in range(2, upper_bound):
        if number % i == 0:
            return i

    return number


def find_largest_prime_factor(number):
    while True:
        smallest_factor = find_smallest_prime_factor(number)

        if smallest_factor < number:
            number //= smallest_factor
        else:
            return number


result = find_largest_prime_factor(600851475143)
print('result: ', result)




