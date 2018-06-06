"""
Problem 7:

What is the 10001st prime number?
"""

import numpy as np

# We will solve this using the sieve of Eratosthenes
# The pseudocode can be found at https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode

n = 200000
sieve = np.array([True for _ in range(n)])
sieve[0:2] = False
upper_bound = int(np.sqrt(n))

for i in range(2, upper_bound+1):
    if sieve[i]:
        j = i * i
        counter = 0
        while j < n:
            sieve[j] = False
            j = (i * i) + (counter * i)
            counter += 1

primes = np.where(sieve == True)[0]

# The solution is at index 10000 since we start at index 0
solution = primes[10000]
print('solution: ', solution)

