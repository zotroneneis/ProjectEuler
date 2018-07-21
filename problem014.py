"""
Longest Collatz sequence

Rules:
    n => n /2 if n is even
    n => 3n + 1 if n is odd


Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

def collatz(n:int):
    """
    Computes and returns the collatz sequence for an integer n
    """
    sequence = []

    while True:
        sequence.append(n)
        if n == 1:
            return sequence

        elif n % 2 == 0:
            n = n // 2

        else:
            n = 3 * n + 1


if __name__ == "__main__":
    n = 999999
    current_best = 0

    for i in range(1, 999999):
        sequence = collatz(i)

        if len(sequence) > current_best:
            current_best = len(sequence)
            winner = i

    print(f"The number {winner} produces the longest Collatz sequence!")
    print(f"Length of longest chain: {current_best}")
