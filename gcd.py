"""
    Finding the greatest common divisor
"""


def gcd_recursive(num_1, num_2):
    """Using recursion"""
    if num_2 == 0:
        return num_1
    return gcd_recursive(num_2, num_1 % num_2)


def gcd_loops(num_1, num_2):
    """Using loops"""
    smaller = num_1
    gcd = 1

    if num_2 > num_1:
        smaller = num_2

    for i in range(1, smaller + 1):
        if (num_1 % i == 0) and (num_2 % i == 0):
            gcd = i

    return gcd


def gcd_euclidean(num_1, num_2):
    """Using the Euclidean algorithm"""
    while num_2:
        num_1, num_2 = num_2, num_1 % num_2

    return num_1
