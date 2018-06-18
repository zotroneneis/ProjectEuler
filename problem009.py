"""
Problem 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import numpy as np

# Brute force: start computing triplets until the correct one has been found
def find_triplet():
    for a in range(1, 500):
        for b in range(1, 500):

            c = np.sqrt(a**2 + b**2)

            if a + b + c == 1000:
                print(f"Triplet found!")
                print(f"a: {a}, b: {b}, c: {c}")
                print(f"a + b + c = {a + b + c}")
                print(f"Product abc = {a*b*c}")
                return


find_triplet()
