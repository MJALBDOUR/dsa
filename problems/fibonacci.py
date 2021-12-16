"""
   Calculate the nth fibonacci number
"""


def fibonacci(nth_term: int) -> int:
    """Using recursion"""
    if nth_term == 0:
        return 0
    if nth_term in (1, 2):
        return 1
    return fibonacci(nth_term - 1) + fibonacci(nth_term - 2)
