"""
   Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

   Return the running sum of nums.
"""


def running_sum(nums):
    """Doing it in place"""
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
