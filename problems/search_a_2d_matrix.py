"""
    Write an efficient algorithm that searches for a value in an mid x cols matrix.
    This matrix has the following properties:
        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.
"""


def search_2d_matrix(matrix, target):
    """Using binary search"""
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1
    while low <= high:
        mid = (low + high) // 2
        num = matrix[mid//cols][mid % cols]
        if target > num:
            low = mid + 1
            continue
        if target < num:
            high = mid - 1
            continue
        return True

    return False
