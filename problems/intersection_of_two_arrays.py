"""
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must appear as many times as it shows in both arrays
    and you may return the result in any order.
"""


def intersect(nums1, nums2):
    """Using 3 dictionaries"""
    ans = []
    dc1, dc2, dc3 = {}, {}, {}
    for num in nums1:
        if num not in dc1:
            dc1[num] = 1
        else:
            dc1[num] += 1

    for num in nums2:
        if num not in dc2:
            dc2[num] = 1
        else:
            dc2[num] += 1

    for num in nums1:
        if num in dc1 and num in dc2:
            dc3[num] = min(dc1[num], dc2[num])

    for num in nums2:
        if num in dc1 and num in dc2:
            dc3[num] = min(dc1[num], dc2[num])

    for key, value in dc3.items():
        ans.extend([key] * value)

    return ans
