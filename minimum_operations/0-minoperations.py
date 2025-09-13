#!/usr/bin/python3
"""
This module contains a function to calculate the minimum number of
operations required to get exactly n 'H' characters in a file using
only 'Copy All' and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: Minimum number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
