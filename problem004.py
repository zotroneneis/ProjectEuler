"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Brute force: multiply all 3 digit numbers and check whether the result is a palindromic number.

def find_palindrome():
    # We will go backwards to make sure that we return the result ASAP
    all_palindromes = (i * j
                       for i in reversed(range(100, 1000))
                       for j in reversed(range(100, 1000))
                       if str(i * j) == str(i * j)[::-1]
                       )

    return max(all_palindromes)

result = find_palindrome()
print('result: ', result)




