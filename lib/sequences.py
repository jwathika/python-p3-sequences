#!/usr/bin/env python3


def print_fibonacci(length):
    """
    Print the Fibonacci sequence up to the specified length.
    """
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        num = [0, 1]
        for i in range(2, length):
            num.append(num[i - 1] + num[i - 2])
        print(num)


print_fibonacci(9)
