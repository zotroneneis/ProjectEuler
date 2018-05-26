"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

https://projecteuler.net/problem=2
"""

def fib(limit):
    a, b = 0, 1
    fib_sequence = []
    while b < limit:
        a, b = b, a + b
        fib_sequence.append(a)

    return fib_sequence

def sum_even_numbers(sequence):
    return sum(num for num in sequence if num % 2 == 0 )

fib_sequence = fib(4000000)
result = sum_even_numbers(fib_sequence)
print('result: ', result)

