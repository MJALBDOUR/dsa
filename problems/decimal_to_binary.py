"""
    Convert a decimal number to binary.
"""


def decimal_to_binary(num):
    """Using recursion"""
    if num == 0:
        return 0
    rem = num % 2
    return rem + decimal_to_binary(num // 2) * 10
