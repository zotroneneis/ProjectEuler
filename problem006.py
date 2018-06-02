"""
Problem 6

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import numpy as np

def sum_of_squares(range_start, range_end):
    return sum(i**2 for i in range(range_start, range_end))

def square_of_sum(range_start, range_end):
    return sum(range(range_start, range_end)) ** 2

def compute_difference(range_start, range_end):
    a = sum_of_squares(range_start, range_end)
    b = square_of_sum(range_start, range_end)

    return np.abs(a - b)

print(compute_difference(1, 101))

