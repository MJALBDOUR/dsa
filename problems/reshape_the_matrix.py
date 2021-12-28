"""
    You are given an mat_m x mat_n matrix mat and two integers rows and c representing the
    number of rows and the number of columns of the wanted reshaped matrix.

    The reshaped matrix should be filled with all the elements of the original
    matrix in the same row-traversing order as they were.

    If the reshape operation with given parameters is possible and legal, output
    the new reshaped matrix; Otherwise, output the original matrix.
"""


def reshape_matrix(mat, rows, cols):
    """Without extra space"""
    mat_m, mat_n = len(mat), len(mat[0])

    if mat_m * mat_n != rows * cols:
        return mat

    ans = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows*cols):
        ans[i // cols][i % cols] = mat[i // mat_n][i % mat_n]

    return ans
