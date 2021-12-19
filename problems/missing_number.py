"""
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
"""


def missing_number(nums):
    """Using arithmetic & O(n) time, O(1) space"""
    length = len(nums)
    expected_sum = int(length * (length + 1) / 2)
    actual_sum = 0
    for num in nums:
        actual_sum += num
    return expected_sum - actual_sum
