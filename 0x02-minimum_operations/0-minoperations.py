#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
 only two operations in this file: Copy All and Paste. Given a number n, write
 a method that calculates the fewest number of operations needed to result in
 exactly n H characters in the file.
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    returns the fewest number of operation need to result in exactly
    n H characters in the file
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
        b += 1
    return a
