"""
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import functools

# The formula given on Wikipedia for computing the LCM is:
# lcm(a, b) = |a * b| / gcd(a, b)
# Where gcd(a, b) denotes the greatest common divisor of a and b

# When computing the LCM of more than two numbers it can be computed by
# iteratively computing the lcm of the current value and the next element of the list
# Example: lcm(a, b, c, d) = lcm(a, lcm(b, lcm(c, d)))

def find_lcm(*args):
    # We want to repeatedly apply the lcm function to
    # This is exactly what the functools.reduce function is doing
    # Example: functools.reduce(lcm, (a, b, c, d)) = lcm(lcm(lcm(a, b), c), d)
    return functools.reduce(lcm, args)

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    """
    GCD according to the Euclidean algorithm
    """
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


solution = find_lcm(*range(1, 20))
print('solution: ', solution)





















