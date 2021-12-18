"""
    Merge 2 sorted lists with O(M + N) time complexity
"""


def merge(nums1, len_1, nums2, len_2):
    """
    In place where len(nums1) = len_1 + len_2
    """
    right_p_nums1 = len_1 + len_2 - 1
    i = len_1 - 1
    j = len_2 - 1
    while i >= 0 and j >= 0:
        if nums2[j] < nums1[i]:
            nums1[right_p_nums1] = nums1[i]
            i -= 1
        else:
            nums1[right_p_nums1] = nums2[j]
            j -= 1
        right_p_nums1 -= 1
    while j >= 0:
        nums1[right_p_nums1] = nums2[j]
        j -= 1
        right_p_nums1 -= 1
