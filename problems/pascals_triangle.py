"""
    Given an integer num_rows, return the first num_rows of Pascal's triangle.
"""


def pascals_triangle(num_rows):
    """Without DP"""
    if num_rows == 1:
        return [[1]]
    ans = [[1], [1, 1]]
    if num_rows > 2:
        for i in range(1, num_rows - 1):
            temp = []
            for j in range(i):
                temp.append(ans[i][j] + ans[i][j + 1])

            temp.insert(0, 1)
            temp.append(1)
            ans.append(temp)
    return ans
